from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from datetime import datetime
import requests, json

app = Flask(__name__)
bootstrap = Bootstrap5(app)