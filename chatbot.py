import os
from colors import Colors
from dotenv import load_dotenv

load_dotenv()

print(Colors.BOLD + "Checkout: https://groq.com/\n")

if not os.environ.get("GROQ_API_KEY"):
    import getpass
    os.environ['GROQ_API_KEY'] = getpass.getpass(Colors.RED + "Enter API key for Groq\n")


from helper import get_models
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

def select_model():
    supported_models = []
    for model in get_models():
        print(model)
        supported_models.append(model)

    selected_model = input(Colors.LIGHT_BLUE+ "Please enter a model name from above list\n")
    selected_model = selected_model.lower().strip()
    if selected_model.lower().strip() not in supported_models:
        print(Colors.RED + "Please enter a valid model name")
        return 

    return selected_model

MODEL = select_model()

if MODEL:
    try:
        model = init_chat_model(MODEL, model_provider="groq")
    
        user_input = "Hi"
        ai_response = ""
        prev_user_text = HumanMessage("")

        while user_input.strip().lower() != "bye":
            user_text = HumanMessage(user_input)
            ai_response = model.invoke(
                [
                    prev_user_text,
                    ai_response if isinstance(ai_response, AIMessage) else AIMessage(""),
                    user_text
                ]
            )
            print(Colors.ITALIC+ai_response.pretty_repr(False))
            user_input = input(Colors.GREEN+"Ask: ")
            prev_user_text = user_text

        print(Colors.END + "Thanks for availaing the services")
    except Exception as e:
        print(Colors.CROSSED + "Something went wrong : " + str(e))
        exit(-1)
