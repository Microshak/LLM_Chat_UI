from flask import Flask, redirect, url_for, request, Blueprint

from flask import Blueprint
from langchain.agents import initialize_agent, Tool
from langchain.utilities import WikipediaAPIWrapper
from chat.common import common

from chat import app

common =  common()
llm = common.llm


cat = Blueprint('cat', __name__)


@app.route('/catalog', methods=['POST'])
def catalog():
    data = request.json
    prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
    dat = data
    msg = dat["txt"]
    id=dat["id"]
    chatNum = dat["chatNum"]
    chain = LLMChain(llm=llm, prompt=prompt)
    chain.run(product=msg, tags=[id,chatNum])
    return ""

