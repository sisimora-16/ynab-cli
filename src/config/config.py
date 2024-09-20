import os
import json

def save_token(token):

    token_data = {
        "token" : token
    }

    home_directory = os.path.expanduser("~")

    file_path = os.path.join(home_directory, ".ynab-cli-config.json")

    with open(file_path, "w") as file:
        json.dump(token_data, file)

    print(f"Token saved to {file_path}")

def delete_token():

    home_directory = os.path.expanduser("~")

    file_path = os.path.join(home_directory, ".ynab-cli-config.json")

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Token deleted from {file_path}")
    else:
        print("No token found to delete")   