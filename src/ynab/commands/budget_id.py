import click

from ynab.config.settings import save_budget_id, delete_budget_id

@click.command("budget-id")
@click.option("--clear", is_flag=True, help="Clear the token")
def set_budget_id(clear):
    if clear:
        delete_budget_id()
        return
    
    budget_id = click.prompt("Enter your YNAB budget id: ")
    save_budget_id(budget_id)


