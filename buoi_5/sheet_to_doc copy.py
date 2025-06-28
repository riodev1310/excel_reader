import os 
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
from docx import Document 


creds = Credentials.from_service_account_file("google_service.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
# Kết nối Google Sheets
client = gspread.authorize(creds)

def connect_google_sheet(SHEET_ID, SHEET_NAME):
    sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    return data 


def fill_word_template(data, template_path, output_path): 
    doc = Document(template_path)
    for p in doc.paragraphs:
        for key, val in data.items():
            text_format = "{" + key + "}"
            p.text = p.text.replace(text_format, str(val))
    doc.save(output_path)
    
    
def create_date_folder_and_save(doc_name):
    now = datetime.now() 
    folder_path = os.path.join('don_hang_output', now.strftime("%m-%Y"), now.strftime("%d"))
    os.makedirs(folder_path, exist_ok=True) 
    return os.path.join(folder_path, doc_name) 


def process_orders():
    orders = connect_google_sheet("106JuailxrkgjNxzb5jzNjucXRxe8uLNVqybSGz6KQAU", "Sheet1")
    for i, order in enumerate(orders, start=1):
        file_path = create_date_folder_and_save(f"don_hang{i}.docx")
        fill_word_template(order, 'don_hang_template.docx', file_path)
        print(f"Done: {file_path}") 
    


process_orders()