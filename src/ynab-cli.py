import click

from ynab.commands import token, budget_id

@click.group()
@click.version_option()
def config():
    pass

@config.group()
def set_config():
    pass

set_config.add_command(token.set_token)
set_config.add_command(budget_id.set_budget_id)

cli = click.CommandCollection(sources=[config])

if __name__ == "__main__":
    cli()