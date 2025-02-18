import os
import docx
import pandas as pd
import PyPDF2

def read_word(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_string()

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extract_text()
        return text

def read_documents(folder_path):
    data = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith('.docx'):
            data[filename] = read_word(file_path)
        elif filename.endswith('.xlsx'):
            data[filename] = read_excel(file_path)
        elif filename.endswith('.pdf'):
            data[filename] = read_pdf(file_path)
    return data
