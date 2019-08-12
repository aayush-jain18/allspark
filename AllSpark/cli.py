import os
import sys
import logging

import click
from AllSpark.core.pd_compare import Compare
from AllSpark.constants import Constants


@click.command()
@click.option(
    '-l', '--left_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True))
@click.option(
    '-r', '--right_file',
    type=click.Path(exists=True, file_okay=True, dir_okay=True, readable=True))
@click.option('-k', '--key', multiple=True)
@click.option('-o', '--output', type=click.Path())
@click.option('--ltype',
              type=click.Choice(['csv', 'tsv', 'excel', 'json', 'html']))
@click.option('--rtype',
              type=click.Choice(['csv', 'tsv', 'excel', 'json', 'html ']))
@click.option('-a', '--atol', type=(float, int))
@click.option('-r', '--rtol', type=(float, int))
@click.option('--progress-bar/--no-progress-bar',
              default=None, help="Flag for turning on the progress bar.")
def main():
    Compare()
    pass


if __name__ == '__main__':
    logging.basicConfig(format=Constants.LOG_FORMAT,
                        level=logging.INFO)
    main()