#!/usr/bin/env python

import click


@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.secho('Hello!')


if __name__ == "__main__":
    cli()
