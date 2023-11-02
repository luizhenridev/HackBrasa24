import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv
from prompts import *
from services.goog import main
#from prompts.intention import intentions

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY=os.environ.get("REQUESTER_TOKEN")
LINK = os.environ.get("LINK")

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def gen(text, userId ,id_model = "gpt-4", max_tokens = 1000):

    context1 = f"""
CONTEXT: 
1. You are Aurora, the virtual assistant designed to help the user keep their financial organized
2. You will chat with the user - in Portuguese - 
4. Consider this {main(userId)} to be your database
6. Based on your database answer financial advices
7. Just give advices when the user request
8. Give summarized answers above 100 tokens to avoid incomplete answers
9. Answer straight wit

### Examples
        NOTE: These examples are for you undestand how to work.   

        Example 1: 
            user message: 
            Quanto eu gastei no mês de Janeiro?
            recommended answer:
            Você gastou um total de R$3.074,47 --- algo nesse sentido

        Example 2: 
            user message: 
            Me diga as áreas que eu mais gastei no mês de janeiro
            recommended answer:
            Imposto: Você gastou R$885,98 
            Educação: Você gastou R$778,66 
            Outros: Você gastou R$678,24 
            
 """
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : context1},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens,
        "temperature": 0.2
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]
    
    return responseMessage

def summarize(text, id_model = "gpt-4", max_tokens = 100):
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : summarize.contextSummarize},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens,
        "temperature": 0.0
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]
    
    return responseMessage

def intention(text = "Como você pode me ajudar?", id_model = "gpt-4", max_tokens = 1000):
    intentions = f"""
CONTEXT: 
    1. You will answer 0 or 1 based in your input.

TASKS: 
    1. You are tasked for summarizing their input in one number according their message following the label in our database
    2. Your objective is understand what is the intention of user
    3. There are 2 intentions 
        0 - Explorer
        1 - Not Explorer

EXAMPLES:
    ##note: These examples are for you undestand how to work.   

        Example 1: 
            user message: 
            Como você pode me ajudar?
            recommended answer:
            0
        
        Example 2: 
            user message: 
            Como você foi criado
            recommended answer:
            0
        
        Example 3: 
            user message: 
            Quanto gastei na no mês de dezembro?
            recommended answer:
            1

        Example 4: 
            user message: 
            Liste um top 3 áreas que mais gastei
            recommended answer:
            1
 """

    body_message = {
        "model" : id_model,
        "messages" : [{"role" : "system", "content" : intentions},
                      {"role" : "user", "content" : text}],
        "max_tokens" : max_tokens,
        "temperature" : 0.2
    }

    body_message = json.dumps(body_message)
    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]

    print(responseMessage)
    return responseMessage


def explorer(text, userId ,id_model = "gpt-4", max_tokens = 1000):

    context1 = """
CONTEXT: 
1. You are Aurora, the virtual assistant designed to help the user keep their financial organized
2. You will chat with the user - in Portuguese - 
4. Consider this to be your database
6. Based on your database answer financial advices
7. Just give advices when the user request
8. Give summarized answers above 100 tokens to avoid incomplete answers
9. Answer straight wit

### Examples
        NOTE: These examples are for you undestand how to work.   

        Example 1: 
            user message: 
            Quanto eu gastei no mês de Janeiro?
            recommended answer:
            Você gastou um total de R$3.074,47 --- algo nesse sentido

        Example 2: 
            user message: 
            Me diga as áreas que eu mais gastei no mês de janeiro
            recommended answer:
            Imposto: Você gastou R$885,98 
            Educação: Você gastou R$778,66 
            Outros: Você gastou R$678,24 
            
 """
    
    body_message = {
        "model": id_model,
        "messages":[{"role": "system", "content" : context1},
                    {"role": "user", "content": text}],
        "max_tokens":max_tokens,
        "temperature": 0.2
    }

    body_message = json.dumps(body_message)

    requisition = requests.post(LINK, headers=headers, data=body_message)
    response = requisition.json()
    responseMessage = response["choices"][0]["message"]["content"]
    
    return responseMessage

if __name__ == '__main__':
    intention()