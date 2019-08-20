# -*- coding: utf-8 -*-

"""Console script for fsdesign."""

import click

from fsdesign import fsdesign


@click.command()
@click.option('-t', '--template', help='Path to template text file for vignettes', type=click.Path(exists=True),
              prompt=True)
@click.option('-f', '--factors', help='Path to factors csv file', type=click.Path(exists=True), prompt=True)
@click.option('-s', '--size', help='Number of resulting vignettes', type=int, prompt=True)
@click.option('-o', '--output', help='Output file path', type=click.Path())
@click.option('-d', '--duplicates', help='Flag for duplicated vignettes', is_flag=True)
def main(template, factors, size, output, duplicates):
    """Console script for fsdesign."""

    factors = fsdesign.read_factors(factors)

    with open(template) as f:
        text_template = f.read()
    fsexperiment = fsdesign.FSDesign(text_template, factors, size=size, duplicates=duplicates)

    if output:
        fsexperiment.to_csv(output)
    else:
        for vignette in fsexperiment.generate_vignettes():
            print(vignette)
            print('\n\n')
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
