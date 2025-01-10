import random
import spacy

nlp = spacy.load("en_core_web_sm")

responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "No problem! Glad I could help!"],
    "fallback": ["I'm sorry, I didn't understand that.", "Can you please rephrase?"],
    "general": [
        "That's interesting!",
        "I see. Tell me more.",
        "Could you elaborate on that?",
        "Why do you think so?",
    ],
}

def detect_intent(user_input):
    doc = nlp(user_input.lower())

    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greeting"
        if token.lemma_ in ["bye", "goodbye", "see you"]:
            return "goodbye"
        if token.lemma_ in ["thank", "thanks"]:
            return "thanks"

    return None

def chatbot_response(user_input):
    intent = detect_intent(user_input)

    if intent:
        return random.choice(responses[intent])
    else:
        return random.choice(responses["general"])


def chatbot():
    print("Chatbot: Hi! I'm here to chat with you. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()