#!/usr/bin/python
from flask import Flask, redirect, url_for, request, Blueprint
from chat import app
from flask import render_template
from langchain.llms import LlamaCpp
from flask_sock import Sock
from langchain.callbacks.streaming_aiter import AsyncIteratorCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
import time
import json
from langchain.memory.chat_message_histories import RedisChatMessageHistory
import os
from dotenv import load_dotenv
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from chat.language.wiki import wk
from chat.language.simple import simp
from chat.common import common
from chat.vision.image import im
from chat.domain.catalog import cat


load_dotenv()
sock = Sock(app)
settings = {}
common =  common()
llm = common.llm
redis = common.chatredis

app.register_blueprint(wk)
app.register_blueprint(im)
app.register_blueprint(simp)
app.register_blueprint(cat)


@app.route('/')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Chat'   )


@app.route('/image')
def image():
    """Renders the home page."""
    return render_template(
        'image.html',
        title='Chat'   )

@app.route('/test')
def test():
    """Renders the home page."""
    return render_template(
        'test.html',
        title='Chat'   )



@sock.route('/echos')
def echos(sock):
    while True:
        data = sock.receive()
        sock.send(data)

@sock.route('/socket')
def socket(sock):
    data = sock.receive()
    dat =  json.loads(data)
    id=dat["id"]
    while True :
        time.sleep(1)
        resp = redis.getdel(id)
        if resp is not None:
            sock.send(resp)




@app.route('/marketingEmail', methods=['POST'])
def me():
    data = request.json
    dat = data
    
    msg = f'''You are a chat bot named {data["from"]} working for a the BHG Money.  
    Create an email to {data["to"]} who works for {data["company"]} telling him that the current bid is ${data["currentBid"]} 
    and he needs to put in a higher bid.  Their last bid was {data["theirbid"]}. 
    The final answer should be in the following JSON format only:
    '''
    sch = '{"to":"","subject":"","body":""}'
    ret = llm(msg+sch)
    return ret

    

@app.route('/marketing', methods=['POST'])
def marketing():
 
    _DEFAULT_TEMPLATE = """The following is a professional conversation between a human and an AI. The AI helps the human brainstorm ideas. The AI comes up with innovative ideas.  If the AI needs to know more information it asks the human.

    Current conversation:
    {chat_history_lines}
    Human: {input}
    AI:"""

    data = request.json
    PROMPT = PromptTemplate(
        input_variables=["input", "chat_history_lines"],
        template=_DEFAULT_TEMPLATE,
    )
    dat = data
    msg = dat["txt"]
    id=dat["id"]
    chatNum = dat["chatNum"]
    history = RedisChatMessageHistory(
        url="redis://localhost:6379/1", ttl=600, session_id=id
    )

    memory = ConversationSummaryBufferMemory(
        memory_key="chat_history_lines", llm=llm, max_token_limit=10, chat_memory=history
    )

    conversation = ConversationChain(llm=llm, verbose=True, memory=memory, prompt=PROMPT)
    ret = conversation.run(msg, tags=[id,chatNum])
    memory.save_context({"input": msg}, {"output": ret})
    return ""

@app.route('/health', methods=['GET'])
def health():
	# Handle here any business logic for ensuring you're application is healthy (DB connections, etc...)
    return "Healthy: OK"

