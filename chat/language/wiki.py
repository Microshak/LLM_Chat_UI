from flask import Flask, redirect, url_for, request, Blueprint

from flask import Blueprint
from langchain.agents import initialize_agent, Tool
from langchain.utilities import WikipediaAPIWrapper
from chat.common import common

from chat import app

common =  common()
llm = common.llm


wk = Blueprint('wk', __name__)


@wk.route('/wiki', methods=['POST'])
def wiki():
    data = request.json
    dat =  data
    msg = dat["txt"]
    id=dat["id"]
    chatNum = dat["chatNum"]
    wikipedia = WikipediaAPIWrapper()
    
    tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Useful for when you need to get information from wikipedia about a single topic",
        
    ),
]
#    llm(msg,tags=[id,chatNum])
    llm.temperature = 0
    agent_executor = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)
    output = agent_executor.run(f"Can you concisely summarize {msg}? ", tags=[id,chatNum])
    return ""

