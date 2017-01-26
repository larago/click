# encoding=utf8

import click

@click.command()
@click.password_option()
def input_password(password):
    clock.echo('password: %s' % password)

input_password()