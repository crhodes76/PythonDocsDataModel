from transformers import pipeline

class Chatbot:
    def __init__(self, documents):
        self.documents = documents
        self.qa_pipeline = pipeline("question-answering")

    def get_response(self, query):
        context = ' '.join(self.documents)
        result = self.qa_pipeline(question=query, context=context)
        return result['answer']
