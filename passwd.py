#encoding=utf8

import click

@click.command()
@click.option('--password', prompt=True, hide_input=True,
    confirmation_prompt=True)
def input_password(password):
    click.echo('password: %s' % password)

input_password()