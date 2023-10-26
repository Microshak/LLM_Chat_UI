
import json
from flask import Flask

app = Flask(__name__)


import chat.routes
import chat.wiki


