import click

from ynab.config.settings import save_token, delete_token

@click.command("token")
@click.option("--clear", is_flag=True, help="Clear the token")
def set_token(clear):
    if clear:
        delete_token()
        return
    
    token = click.prompt("Enter your YNAB API token: ")
    save_token(token)
