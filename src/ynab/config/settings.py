from ynab.config.config_manager import save_config, load_config, delete_config

TOKEN_FILE = "token.json"
BUDGET_ID_FILE = "budget_id.json"

def save_token(token):
    save_config({"token": token}, TOKEN_FILE)

def save_budget_id(budget_id):
    save_config({"budget_id": budget_id}, BUDGET_ID_FILE)

def load_token():
    return load_config("token", TOKEN_FILE) 

def load_budget_id():
    return load_config("budget_id", BUDGET_ID_FILE)

def delete_token():
    delete_config(TOKEN_FILE)

def delete_budget_id():
    delete_config(BUDGET_ID_FILE)