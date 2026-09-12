import os
from google import genai
from google.genai import types
from utilit_functions import read_txt_file , write_code_file , analyse_data_csv_source
from dotenv import load_dotenv

# 1. Initialize the client using your project ID.
# It automatically picks up the ADC credentials you configured with the setup script!

load_dotenv()

project_id = os.getenv("project")
location = os.getenv("location")

if not project_id or not location:
    raise RuntimeError("PROJECT_ID and LOCATION must be set in the .env file")

client = genai.Client(
    vertexai=True,
    project=project_id,
    location=location
)


# 3. Create an interactive chat session with the tool enabled
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=""" You are a HelpFull Agent which help in Reading the business requirent and analyse the data source and generate the Pandas code to generate the required CSV file as per the business requirenment for helping you out you have following tools 
        
        1. read_txt_file -- to read any text file if required
        2. analyse_data_csv_source -- If the data source is the CSV then it will help you with the required details for analysis
        3. write_code_file -- to dump the code file directly into the required path 

        """,
        tools=[read_txt_file , write_code_file , analyse_data_csv_source],
        tool_config=types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(
                mode="AUTO" # Fix: Using string 'AUTO' is the most robust way
            )
        )
    )
)

# 4. Start the conversation
print("==================================================")
print("Gemini Agent is online. Ask it to count characters!")
print("==================================================")

user_message = """Business Requirements -- business_requirement.txt 
                  Data Source -- book.csv
                  Final code Path -- Data_transformation.py"""

print(f"User: {user_message}")

response = chat.send_message(user_message)
print(f"Agent: {response.text}")


# print(response)