from ynab.config import settings

YNAB_TOKEN = settings.load_token()
YNAB_BUDGET_ID = settings.load_budget_id()

YNAB_HEADERS = {
    "Authorization": "BEARER " + YNAB_TOKEN}

YNAB_API_URL = "https://api.ynab.com/v1/budgets"
YNAB_TRANSACTIONS_URL = f"{YNAB_API_URL}/{YNAB_BUDGET_ID}/transactions"
YNAB_CATEGORIES_URL = f"{YNAB_API_URL}/{YNAB_BUDGET_ID}/categories"