#!/usr/bin/env python

import click


@click.command(help="Displays a greeting.")
@click.argument('names', nargs=-1)
@click.option('--greeting',
              '-g',
              default='Hello',
              help='The greeting to display',
              )
@click.option('--question',
              is_flag=True,
              default=False,
              help='Make the greeting a question'
              )
@click.option('--int-option', type=int)
@click.option('--float-option', type=float)
@click.option('--bool-option', type=bool)
@click.option('--choice-option', type=click.Choice({'A', 'B', 'C'}))
def cli(greeting,
        names,
        question,
        int_option,
        float_option,
        bool_option,
        choice_option,
        ):
    punc = '?' if question else '!'
    if choice_option is not None:
        print(f'choice: {choice_option}')
    if int_option is not None:
        print(f'int: {int_option}')
    if float_option is not None:
        print(f'float: {float_option}')
    if bool_option is not None:
        print(f'bool: {bool_option}')
    for name in names:
        print(f"{greeting}, {name}{punc}")


if __name__ == "__main__":
    cli()
