#encoding=utf8

import click

@click.command()
@click.option('--rate', type=float, help='rate')

def show(rate):
    click.echo('rate: {}'.format(rate))

if __name__ == '__main__':
    show()