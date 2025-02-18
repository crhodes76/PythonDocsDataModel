import os
from document_processor import DocumentProcessor
from chatbot import Chatbot

def main():
    folder_path = 'D:/Documents'
    processor = DocumentProcessor(folder_path)
    documents = processor.process_documents()

    chatbot = Chatbot(documents)
    while True:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
