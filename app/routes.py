#!/usr/bin/python
from flask import Flask, redirect, url_for, request, Blueprint
from . import app
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
import redis
import time
import json
from langchain.memory.chat_message_histories import RedisChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()
sock = Sock(app)
n_gpu_layer = 40
n_batch = 512
settings = {}

# Create a connection to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # Set a value
        ret = {"id":kwargs.get("tags")[0],"chatNum":kwargs.get("tags")[1], "token":token}
        r.append(kwargs.get("tags")[0], json.dumps(ret) )
        r.expire(kwargs.get("tags")[0],12000)
        
# Callbacks support token-wise streaming
callback_manager = CallbackManager([MyCustomHandler()])

llm = LlamaCpp(
    model_path=os.getenv("model"),
    temperature=0.25,
    max_tokens=2000,
    top_p=1,
    callbacks=[MyCustomHandler()],
    verbose=True,
    n_gpu_layers=n_gpu_layer,
    n_batch=n_batch,
    n_ctx=2048,
    f16_kv=True,
)

@app.route('/')
def encrypt():
    """Renders the home page."""
    return render_template(
        'index.html',
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
        resp = r.getdel(id)
        if resp is not None:
            sock.send(resp)

@app.route('/simple', methods=['POST'])
def simple():
    data = request.json
    dat = data
    msg = dat["txt"]
    id=dat["id"]
    chatNum = dat["chatNum"]
    llm(msg,tags=[id,chatNum])
    return ""
@app.route('/converstation', methods=['POST'])
def converstation():
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

