def read_txt_file(path:str) -> str:
    """Read the Text File content and return it in String Format
    
    Args:
        path: File path needed to be read (string)
    
    Output:
        File Content (string)
    """

    print(f"[System Triggerd] : Read the File {path}")
    content = ""
    with open(path , encoding='UTF-8') as file:
        content = file.read()
    return content


def write_code_file(file_path:str , code:str) -> bool:
    """Write code to the python file and return True if code is written or False if any error occured
    
    Args:
        file_path: File path needed to be read (string)
        code: code generate 
    
    Output:
        True/False
    """
    print(f"[System Triggerd] : Write the File {file_path}")

    try:
        with open(file_path ,  'w',  encoding='UTF-8' ) as file:
                file.write(code)
        return True
    
    except Exception as e:
        print(e)
        return False

def analyse_data_csv_source(path:str) -> dict:
    """This Function will help in Analysing the CSV data source to understand the data and help in code building
    
    Args:
        file_path: File path needed to be read (string)
    Output:
        A dictonary with the details like datatype , Sample Data , Summary of the data
    """

    import pandas as pd

    df = pd.read_csv(path)
    dtypes = df.dtypes.astype(str).to_dict()
    data = df.head(3).to_dict(orient="list")
    describe = df.describe().to_dict()

    return {
         'dtypes' : dtypes , 
         'Data' : data , 
         'Summary' : describe
    }


print(analyse_data_csv_source('book.csv'))