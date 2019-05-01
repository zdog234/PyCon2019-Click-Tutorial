#!/usr/bin/env python

import click
import sys
import os


@click.command()
@click.option('--red', is_flag=True, default=False)
# @click.argument('input-file', type=os.PathLike)
# @click.argument('output-file', type=os.PathLike)
@click.argument('input-file', type=click.File('r'), default='-')
@click.argument('output-file', type=click.File('w'), default='-')
def cli(red,
        input_file,
        output_file,
        ):

    
    color = 'red' if red else 'green'
    def cecho(content, **kwargs):
        click.secho(content, fg=color, **kwargs)

    # color = 'red' if red else (144, 132, 22)
    cecho("Hello!")
    cecho("Printing...", err=True)

    input_data = input_file.read()
    cecho(f'Input length: {len(input_data)}', err=True)
    if input_file:
        cecho(input_data,
              file=output_file, # will default to stdout
              nl=False, # Don't add newline to the end
              )



if __name__ == "__main__":
    cli()
