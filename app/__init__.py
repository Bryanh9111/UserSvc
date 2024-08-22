# Databricks notebook source
from flask import Flask
from flask_cors import CORS
import msal

app = Flask(__name__)
CORS(app)

from app.routes import *

def create_msal_app():
    return msal.ConfidentialClientApplication(
        app.config["CLIENT_ID"],
        authority=app.config["AUTHORITY"],
        client_credential=app.config["CLIENT_SECRET"],
    )

msal_app = create_msal_app()
