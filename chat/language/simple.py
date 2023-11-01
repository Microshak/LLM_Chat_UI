from flask import Flask, redirect, url_for, request, Blueprint

from flask import Blueprint
from langchain.agents import initialize_agent, Tool
from langchain.utilities import WikipediaAPIWrapper
from chat.common import common

from chat import app

common =  common()
llm = common.llm


simp = Blueprint('simp', __name__)


@simp.route('/simple', methods=['POST'])
def simple():
    data = request.json
    dat = data
    print(dat)
    msg = dat["txt"]
    id=dat["id"]
    chatNum = dat["chatNum"]
    ret = llm(msg,tags=[id,chatNum])
    return ret
