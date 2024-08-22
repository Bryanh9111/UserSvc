# Databricks notebook source
# Mock MSAL app, no actual MSAL initialization needed when bypassing Azure AD
msal_app = None

# import msal
# from app import app

# def create_msal_app():
#     return msal.ConfidentialClientApplication(
#         app.config["CLIENT_ID"],
#         authority=app.config["AUTHORITY"],
#         client_credential=app.config["CLIENT_SECRET"],
#     )

# msal_app = create_msal_app()