import click

@click.command()
@click.option('--center', nargs=2, type=float,
    help='center of the circle')
@click.option('--radius', type=float,
    help='radius of the circle')
def circle(center, radius):
    click.echo('center: %s, radius: %s' % (center, radius))

circle()