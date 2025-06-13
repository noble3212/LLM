# "Advanced" Chatbot Project

This project contains a weak. But, general ai that trains off conversations and data. The data implentmentation i haven't updated yet 

## Project Structure

```
advanced-chatbot
├── src
│   ├── main.py
│   ├── chatbot
│   │   ├── __init__.py
│   │   ├── model.py
│   │   ├── conversation.py
│   │   └── utils.py
│   └── config
│       └── settings.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd advanced-chatbot (i didnt upload the folder GL)
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate` (linux mainly. I just use VSCODE in windows)
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt (its like one line)
   ```

## Usage

To run the chatbot, execute the following command:

```
python src/main.py
```

Follow the prompts to interact with the chatbot. Type 'quit' to exit the conversation.

## Features

- Engaging and context-aware conversations. (in 10 years)
- Ability to handle multiple user inputs and maintain conversation history. (it's reaction to anything hard was Meow.)
- Customizable settings for model parameters and behavior. (this is good )
- Please note there might be a loop with the new HTML. But, its due to a sleep mode in the code or sum. + training data you'll see

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
