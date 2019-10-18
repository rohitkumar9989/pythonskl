#!/bin/python3 

import os
import slack
from config import Bot_User_OAuth_Access_Token
client = slack.WebClient(token=Bot_User_OAuth_Access_Token)

response = client.chat_postMessage(
    channel='#random',
    text="Hello world!")
assert response["ok"]
assert response["message"]["text"] == "Hello world!"