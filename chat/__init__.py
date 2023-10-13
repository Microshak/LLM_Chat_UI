from flask import Flask
import json

app = Flask(__name__)
import chat.routes
import chat.wiki
