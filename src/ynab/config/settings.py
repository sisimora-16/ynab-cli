from ynab.config.config_manager import save_config, load_config, delete_config

TOKEN_SETTINGS = "token.json"
BUDGET_SETTINGS = "budget_id.json"

def save_token(token):
    save_config({"token": token}, TOKEN_SETTINGS)

def save_budget_id(budget_id):
    save_config({"budget_id": budget_id}, BUDGET_SETTINGS)

def load_token():
    return load_config("token", TOKEN_SETTINGS) 

def load_budget_id():
    return load_config("budget_id", BUDGET_SETTINGS)

def delete_token():
    delete_config(TOKEN_SETTINGS)

def delete_budget_id():
    delete_config(BUDGET_SETTINGS)