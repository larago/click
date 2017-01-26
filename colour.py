#encoding=utf8

import click

@click.command()
@click.option('--name', help='The person to greet')
def hello(name):
    click.secho('Hello %s!' % name, fg='red', underline=True)
    click.secho('Hello %s!' % name, fg='yellow', bg='white')

hello()