#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""

import requests

if __name__ == "__main__":
    # Send a GET request to the URL
    response = requests.get("https://intranet.hbtn.io/status")
    
    # Print the response body
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

