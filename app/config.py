# Databricks notebook source
import os

class Config:
    CLIENT_ID = os.getenv("CLIENT_ID", "real-client-id")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET", "real-client-secret")
    TENANT_ID = os.getenv("TENANT_ID", "real-tenant-id")
    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
    REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:4200")
    SCOPES = ["User.Read"]
