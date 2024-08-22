# Databricks notebook source
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# # Placeholder configuration for future use
# app.config["CLIENT_ID"] = "client-id"  # Replace with actual client ID when ready
# app.config["CLIENT_SECRET"] = "client-secret"  # Replace with actual client secret when ready
# app.config["AUTHORITY"] = "https://login.microsoftonline.com/tenant-id"  # Replace with actual tenant ID when ready

from app import routes
