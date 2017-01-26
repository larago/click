# encoding=utf8

import click

@click.command()
@click.option('--gender', type=click.Choice(['man', 'woman']))
def choose(gender):
    click.echo('gender: {}'.format(gender))

choose()