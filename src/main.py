from chatbot.model import ChatbotModel
from chatbot.conversation import ConversationManager

from datasets import load_dataset

# Load datasets (for exploration or preprocessing, not for direct inference)
owt = load_dataset("openwebtext", split="train", streaming=True, trust_remote_code=True)
c4 = load_dataset("c4", "en", split="train", streaming=True, trust_remote_code=True)
wiki = load_dataset("wiki40b", "en")
books = load_dataset("bookcorpus", trust_remote_code=True)
code = load_dataset("codeparrot/codeparrot-clean")

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
