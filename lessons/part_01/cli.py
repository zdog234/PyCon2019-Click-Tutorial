#!/usr/bin/env python

import click


@click.command()
@click.argument('names', nargs=-1)
@click.option('--greeting', '-g', default='Hello')
@click.option('--question', is_flag=True, default=False)
def cli(greeting, names, question):
    punc = '?' if question else '!'
    for name in names:
        print(f"{greeting}, {name}{punc}")


if __name__ == "__main__":
    cli()
