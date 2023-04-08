# Create a conversation with GPT that involves pulling the data from market_data.json and asking GPT for 2-3 market-making strategies for each ticker along with rationale for why those strategies are good.
#
# The conversation should be structured as follows:
# I will provide you with a JSON of crypto market data. You will use this data to generate 2-3 market-making strategies for each ticker along with rationale for why those strategies are good.
#
# <json data>

import openai
import os
from dotenv import load_dotenv
import json
import yaml

load_dotenv()

openai.organization = "org-VAzYa2yfTTttUMNvCBhluUKn"
openai.api_key = os.getenv("OPENAI_API_KEY")

system_instructions = [
    "Your name is Abacus. You channel the intuitions of KJ and Omar along with analyzing market data.",
    " The output of your processing is a yaml file that contains configurations for a market-making bot (Hummingbot).",
    " The users will provide you with some examples of market data as well as examples of Hummingbot yamls.",
    # " Respond to this instruction set with an affirmation, and provide the top 5 questions you have about the task.",
]

# user instructions; pass the market_data.json into the chat
with open('market_data_TRAINING.json', 'r') as file:
    data = json.load(file)
    market_json_TRAINING = json.dumps(data)

with open('conf_pure_market_making_strategy_TEMPLATE.yml', 'r') as file:
    yaml_hb_config = yaml.safe_load(file)
    hb_yaml_TRAINING = yaml.dump(yaml_hb_config)


user_instructions = [
    'the following is a JSON file of market data:\n\n:',
    market_json_TRAINING,
    '\n\n The following is a Hummingbot yaml configuration file:\n\n',
    hb_yaml_TRAINING,

]

# live data generation; pass the market_data_LIVE.json into the chat

with open('market_data_LIVE.json', 'r') as file:
    data = json.load(file)
    market_json_LIVE = json.dumps(data)

entelechy_instructions = [
    'generate a hummingbot pure market making config for the following market data:\n\n',
    market_json_LIVE,
]

# https://platform.openai.com/docs/api-reference/chat/create#chat/create-messages
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": '\n'.join(system_instructions)},
    {"role": "user", "content": '\n'.join(user_instructions)},
    # {"role": "system", "content": 'Acknowledge what you just received. Summaraize the data and provide a high-level overview of the data.'},
    {"role": "user", "content": '\n'.join(entelechy_instructions)},

  ]
)

print(completion.choices[0].message)