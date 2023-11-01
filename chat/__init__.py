
import json
from flask import Flask

app = Flask(__name__)


import chat.routes
import chat.language.wiki
import chat.vision.image
import chat.language.simple
import chat.domain.catalog
