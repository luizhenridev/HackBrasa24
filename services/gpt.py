import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv
#from promptFinancialAdvisor import context
from prompts.summarize import contextSummarize
#from promptFinancialresumido import context2
from services.goog import main

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY=os.environ.get("REQUESTER_TOKEN")
LINK = os.environ.get("LINK")

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def gen(text, userId ,id_model = "gpt-3.5-turbo", max_tokens = 100):

    context1 = f"""
CONTEXT: 
1. You are Aurora, the virtual assistant designed to help the user keep their financial organized
2. You will chat with the user - in Portuguese - 
3. Maintain a fun and light-hearted tone throughout the conversation
4. Consider this {main(userId)} to be your database
5. Each column is from a specific month
6. Each row is from a specific kind of spend
7. Based on your database answer financial advices
8. Just give advices when the user request
9. Give advices when the based the income and how much was spend in that month.
10. Give summarized answers to avoid incomplete answers
 """
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : context1},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]
    
    return responseMessage

def summarize(text, id_model = "gpt-3.5-turbo", max_tokens = 100):
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : contextSummarize},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]
    
    return responseMessage
if __name__ == '__main__':
    gen()