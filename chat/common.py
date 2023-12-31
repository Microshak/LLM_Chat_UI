import redis
from langchain.callbacks.manager import CallbackManager
from langchain.llms import LlamaCpp
from langchain.callbacks.streaming_aiter import AsyncIteratorCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.base import BaseCallbackHandler
import os
import json
from dotenv import load_dotenv
load_dotenv()



class MyCustomHandler(BaseCallbackHandler):
    # Create a connection to Redis
    def __init__(self):
        redisURL = os.getenv("redisURL")
        self.r = redis.Redis(host=redisURL, port=6379, decode_responses=True)

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # Set a value
        if(len(kwargs.get("tags")) == 0):
            return
        ret = {"id":kwargs.get("tags")[0],"chatNum":kwargs.get("tags")[1], "token":token}
        self.r.append(kwargs.get("tags")[0], json.dumps(ret) )
        self.r.expire(kwargs.get("tags")[0],12000)
        
# Callbacks support token-wise streaming



class common(object):
    callback_manager = CallbackManager([MyCustomHandler()])

    def __init__(self):
        redisURL = os.getenv("redisURL")
        self.chatredis = redis.Redis(host=redisURL, db=0, port=6379, decode_responses=True)
        self.imageredis = redis.Redis(host=redisURL, db=2, port=6379, decode_responses=True)
        path = os.getenv("model")
        print(path)
        #n_gpu_layer = 1

#        n_batch = 128
        #print(os.getenv("model"))
        self.llm =  LlamaCpp(
        model_path=path,
        temperature=0.75,
        #max_tokens=2000,
        #top_p=1,
        callbacks=[MyCustomHandler()],
        #verbose=True,
 #       n_gpu_layers=n_gpu_layer,
 #       n_batch=n_batch,
        #n_ctx=2048,
        #f16_kv=True,
        )
