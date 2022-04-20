import os

API_TOKEN = os.environ.get(API_TOKEN)
USER_ID = os.environ.get(USER_ID)

agecalculator:
  bottoken: API_TOKEN
  errorid: USER_ID
  debug: True
