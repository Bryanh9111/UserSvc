# Databricks notebook source
from flask import jsonify, request
from app import app
from app.auth import msal_app 
import requests

@app.route('/user-info', methods=['GET'])
def get_user_info():
    # Mock user data for testing
    mock_user_data = {
        "displayName": "John Doe",
        "mail": "john.doe@example.com",
        "jobTitle": "Admin",
        "department": "Finance"
    }

    # Return the mock data instead of making an actual request to Azure AD
    return jsonify(mock_user_data)

    # Uncomment below to use real Azure AD logic when ready
    # token = request.headers.get('Authorization').split(' ')[1]
    # user_info = msal_app.acquire_token_on_behalf_of(token, app.config["SCOPES"])
    
    # if 'access_token' in user_info:
    #     graph_response = requests.get(
    #         'https://graph.microsoft.com/v1.0/me',
    #         headers={'Authorization': 'Bearer ' + user_info['access_token']}
    #     )
    #     return jsonify(graph_response.json())
    # return jsonify({'error': 'Unable to fetch user info'}), 400
