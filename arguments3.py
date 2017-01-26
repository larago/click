#encoding=utf8

import click

@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def move(src, dst):
    click.echo('move %s to %s' % (src, dst))

move()
