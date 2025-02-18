import os
import docx
import PyPDF2
import pandas as pd

class DocumentProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def process_documents(self):
        documents = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.docx'):
                documents.append(self._process_docx(os.path.join(self.folder_path, filename)))
            elif filename.endswith('.pdf'):
                documents.append(self._process_pdf(os.path.join(self.folder_path, filename)))
            elif filename.endswith('.xlsx'):
                documents.append(self._process_excel(os.path.join(self.folder_path, filename)))
        return documents

    def _process_docx(self, filepath):
        doc = docx.Document(filepath)
        return '\n'.join([para.text for para in doc.paragraphs])

    def _process_pdf(self, filepath):
        try:
            with open(filepath, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except PyPDF2.errors.PdfReadError:
            print(f"Error reading PDF file: {filepath}")
            return ''

    def _process_excel(self, filepath):
        df = pd.read_excel(filepath)
        return df.to_string()
