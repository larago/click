# encoding=utf8

import click

@click.command()
@click.argument('coordinates')
def show(coordinates):
    click.echo('coordinates: %s' % coordinates)

show()