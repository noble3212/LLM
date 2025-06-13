from flask import Flask, render_template, request, jsonify
from chatbot.model import ChatbotModel
from chatbot.conversation import ConversationManager

from datasets import load_dataset

# Load datasets (for exploration or preprocessing, not for direct inference)
owt = load_dataset("openwebtext", split="train", streaming=True, trust_remote_code=True)
c4 = load_dataset("c4", "en", split="train", streaming=True, trust_remote_code=True)
wiki = load_dataset("wiki40b", "en")
books = load_dataset("bookcorpus", trust_remote_code=True)
code = load_dataset("codeparrot/codeparrot-clean")
gsm8k = load_dataset("gsm8k", "main", split="train")
csqa = load_dataset("commonsense_qa")
piqa = load_dataset("piqa", trust_remote_code=True)


app = Flask(__name__)
chatbot_model = ChatbotModel()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = chatbot_model.generate_response(user_input)
    return jsonify({"response": response})


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
    app.run(debug=True, port=7854)
    main()
