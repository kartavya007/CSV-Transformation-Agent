# CSV Transformation Agent

This project uses a Google Gemini agent on Vertex AI to analyze a CSV source and generate Python transformation code. The generated transformation prepares business-ready sales data from `book.csv`.

## Project Files

- `main.py` - Starts the Gemini agent and asks it to use the business requirements and CSV source to generate `Data_transformation.py`.
- `Data_transformation.py` - Applies the sales transformations and writes `transformed_book.csv`.
- `utilit_functions.py` - Provides the agent tools for reading text files, analyzing CSV files, and writing generated code.
- `business_requirement.txt` - Defines the transformation rules and final output schema.
- `book.csv` - Input sales data.
- `transformed_book.csv` - Generated business-ready output.

## Requirements

- Python 3.9 or later
- A Google Cloud project with Vertex AI access
- Google Application Default Credentials configured locally

Install the Python dependencies:

```bash
python3 -m pip install google-genai python-dotenv pandas
```

Authenticate with Google Cloud if Application Default Credentials are not already configured:

```bash
gcloud auth application-default login
```

## Configuration

Create a `.env` file in the project root. The application currently reads these lowercase variable names:

```dotenv
project=your-google-cloud-project-id
location=us-central1
```

Keep `.env` private. It is excluded by `.gitignore`.

## Usage

To start the Gemini transformation agent:

```bash
python3 main.py
```

The agent reads `business_requirement.txt` and `book.csv`, then can write the generated code to `Data_transformation.py`.

To run the transformation directly against the current input file:

```bash
python3 Data_transformation.py
```

The script filters to completed orders, calculates gross and net sales, normalizes customer and payment data, assigns regions, derives delivery status, and writes the result to `transformed_book.csv`.

## Output

The output contains business-ready fields including:

- Order and customer details
- Region and product information
- Gross amount, discount amount, and net sales
- Order value segment and payment group
- Delivery days and delivery status
- Reporting month and reporting key

The detailed transformation rules and output schema are documented in `business_requirement.txt`.