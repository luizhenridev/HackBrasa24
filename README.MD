# Python Project

This repository contains a Python project designed to [brief description of what your project does]. The main file of the project is `main.py`, which is located in the root directory.

## Table of Contents

- [Installation](#installation)

- [Usage](#usage)
- [Dependencies](#dependencies)
- [Environment Variables](#environment-variables)

## Installation

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/luizhenridev/HackBrasa24.git
cd HackBrasa24/

python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```
## Usage

It is a bot developed to help business to grow and assist their clients

## Dependencies
- requests
- flask
- pandas
- python-dotenv
- openai
- python-telegram-bot
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- gspread
- psycopg2


## Environment Variables
Create a .env file with these values

Telegram
- TOKEN_BOT
- BOT_USERNAME
Follow this to get your own TOKEN_BOT and BOT_USERNAME https://core.telegram.org/bots/features#creating-a-new-bot

GPT
- REQUESTER_TOKEN : It is necessary to create your own GPT API KEY. Folow this documentation https://platform.openai.com/docs/api-reference/chat/create or this Youtube Video https://www.youtube.com/watch?v=aVog4J6nIAU
- LINK= "https://api.openai.com/v1/chat/completions"





