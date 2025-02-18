from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from document_reader import read_documents

# Initialize chatbot
chatbot = ChatBot('DocumentBot')

# Read documents and prepare training data
folder_path = '/path/to/your/documents'
documents_data = read_documents(folder_path)
training_data = []
for filename, content in documents_data.items():
    training_data.append(content)

# Train chatbot
trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Chatbot response
def get_response(query):
    return chatbot.get_response(query)

if __name__ == "__main__":
    while True:
        query = input("You: ")
        response = get_response(query)
        print(f"Bot: {response}")
