# Groq Chatbot with LangChain

This project provides an interactive chatbot interface using **Groq's API** and **LangChain** for processing user queries. The chatbot allows users to select a model from the available Groq models and engage in a conversational loop until they exit.

## Features
- Retrieves available models from Groq API.
- Allows users to select a model dynamically.
- Maintains conversational history for better AI responses.
- Uses **LangChain** for chatbot interactions.
- ANSI color formatting for improved CLI readability.

## Prerequisites
Ensure you have Python installed (Python 3.7+ recommended).

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Setup
1. **Clone the Repository**
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```

2. **Set up Environment Variables**
   - Create a `.env` file in the root directory and add:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```
   - Alternatively, you can enter the API key manually when prompted.

## How to Use
1. Run the script:
   ```sh
   python chatbot.py
   ```
2. The script will prompt you to select a model from the list of available Groq models.
3. Enter messages to interact with the AI.
4. Type `bye` to exit the conversation.

## Code Structure
- **`helper.py`**: Contains utility functions like fetching models.
- **`chatbot.py`**: Main script for running the chatbot.
- **`colors.py`**: ANSI color formatting for CLI.

## Dependencies
- [LangChain](https://python.langchain.com/docs/get_started/introduction)
- [Groq API](https://groq.com/)

## Example Output
```
Checkout: https://groq.com/

Please enter a model name from the above list:
- groq-llama3
- groq-gpt
Selected Model: groq-llama3

Ask: Hello!
AI: Hello! How can I assist you today?
Ask: What's the weather like?
AI: I'm unable to check live weather but you can check on a weather site!
Ask: bye
Thanks for availing the services.
```

## Error Handling
- If the API key is missing, the script will prompt for manual entry.
- If an invalid model is entered, it will ask for a valid one.
- Any unexpected error will be caught and displayed.

## License
This project is open-source. Feel free to modify and improve!

---
Developed with ❤️ using Python & LangChain 🚀

