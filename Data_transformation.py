
import pandas as pd

# Load the dataset
df = pd.read_csv('book.csv')

# --- Data Type Conversion ---
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

# --- BR-01 & BR-02: Filter Orders ---
df = df[df['order_status'] == 'Completed']

# --- BR-03: Calculate gross line amount ---
df['gross_amount'] = df['quantity'] * df['unit_price']

# --- BR-04: Calculate discount amount ---
df['discount_amount'] = df['gross_amount'] * df['discount_pct'] / 100

# --- BR-05: Calculate net sales ---
df['net_sales'] = df['gross_amount'] - df['discount_amount']

# --- BR-06: Classify order value ---
def classify_order_value(net_sales):
    if net_sales >= 10000:
        return 'High'
    elif net_sales >= 5000:
        return 'Medium'
    else:
        return 'Low'
df['order_value_segment'] = df['net_sales'].apply(classify_order_value)

# --- BR-07: Normalize payment methods ---
def normalize_payment_method(method):
    if method in ['Credit Card', 'Debit Card']:
        return 'CARD'
    elif method == 'UPI':
        return 'UPI'
    elif method == 'Cash':
        return 'CASH'
    return None # Or handle as 'Other'
df['payment_group'] = df['payment_method'].apply(normalize_payment_method)

# --- BR-08: Create customer region ---
def assign_region(state):
    south_states = ['Telangana', 'Karnataka', 'Tamil Nadu', 'Kerala']
    west_states = ['Gujarat', 'Maharashtra']
    north_states = ['Delhi', 'Haryana', 'Punjab', 'Uttar Pradesh', 'Rajasthan']
    east_states = ['West Bengal']

    if state in south_states:
        return 'South'
    elif state in west_states:
        return 'West'
    elif state in north_states:
        return 'North'
    elif state in east_states:
        return 'East'
    return None # Or handle unknown states

df['region'] = df['state'].apply(assign_region)

# --- BR-09: Create delivery days ---
df['delivery_days'] = (df['ship_date'] - df['order_date']).dt.days

# --- BR-10: Flag delayed deliveries ---
def flag_delivery_status(row):
    if pd.isna(row['ship_date']):
        return 'Not Shipped'
    elif row['delivery_days'] > 3:
        return 'Delayed'
    else:
        return 'On Time'
df['delivery_status'] = df.apply(flag_delivery_status, axis=1)

# --- BR-11: Standardize customer name ---
df['customer_name'] = df['customer_name'].str.strip().str.title()

# --- BR-12: Standardize email ---
df['customer_email'] = df['customer_email'].str.strip().str.lower()

# --- BR-13: Create reporting month ---
df['reporting_month'] = df['order_date'].dt.strftime('%Y-%m')

# --- BR-14: Create final output key ---
df['reporting_key'] = df['region'] + '-' + df['product_category'] + '-' + df['reporting_month']

# --- BR-15: Output should contain only business-ready fields ---
output_columns = [
    'order_id', 'order_date', 'customer_name', 'customer_email', 'state',
    'region', 'product_category', 'product', 'quantity', 'unit_price',
    'gross_amount', 'discount_amount', 'net_sales', 'order_value_segment',
    'payment_group', 'delivery_days', 'delivery_status', 'reporting_month',
    'reporting_key'
]

df_output = df[output_columns]

# --- Save the transformed data to a new CSV file ---
# For demonstration, saving to 'transformed_book.csv'
# In a real scenario, this might be specified in requirements or an argument.
# Adding a print statement to confirm completion.
df_output.to_csv('transformed_book.csv', index=False)
print("Data transformation complete. Output saved to 'transformed_book.csv'")
