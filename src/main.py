from chatbot.model import ChatbotModel
from chatbot.conversation import ConversationManager

def main():
    conversation_manager = ConversationManager()
    chatbot_model = ChatbotModel()

    print("Welcome to the Advanced Chatbot! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        
        response = chatbot_model.generate_response(user_input)
        print("AI:", response)

if __name__ == "__main__":
    main()