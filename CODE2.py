import nltk
import string
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# FAQ Data
faq_data = {
    "What is Python?": "Python is a programming language.",
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is Machine Learning?": "Machine Learning enables computers to learn from data.",
    "What is NLP?": "NLP stands for Natural Language Processing.",
    "What is GitHub?": "GitHub is a platform used to store and manage code.",
    "What is Data Science?": "Data Science is the study of data to gain insights.",
    "What is a chatbot?": "A chatbot is a program that can answer user questions."
}

# Separate questions and answers
questions = list(faq_data.keys())
answers = list(faq_data.values())

# Text Preprocessing using NLTK
def preprocess(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    return " ".join(tokens)

# Preprocess all FAQ questions
processed_questions = [preprocess(q) for q in questions]

# Convert text into vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot Response Function
def chatbot_response(user_input):
    user_input = preprocess(user_input)

    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]

    if best_score > 0.2:
        return answers[best_match_index]
    else:
        return "Sorry, I could not find a matching answer."

# Chat Interface
print("=" * 40)
print("      FAQ CHATBOT")
print("Type 'exit' to quit")
print("=" * 40)

while True:
    user_question = input("\nYou: ")

    if user_question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_question)

    print("Chatbot:", response)
    