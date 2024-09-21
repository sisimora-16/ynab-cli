import os
import json

def _get_config_directory():
    home_directory = os.path.expanduser("~")
    config_directory = os.path.join(home_directory, ".ynab-cli")
    return config_directory

def save_config(data, filename):

    file_path = os.path.join(_get_config_directory(), filename)
    with open(file_path, "w") as file:
        json.dump(data, file)
    print(f"Data saved to {file_path}")

def load_config(config_name,filename):

    file_path = os.path.join(_get_config_directory(),filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data.get(config_name)
    else:
        print(f"No data found in {file_path}")
        return None


def delete_config(filename):

    file_path = os.path.join(_get_config_directory(),filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Config deleted from {file_path}")
    else:
        print("No token found to delete")   
