"""Main module."""
import collections
import csv
import itertools
import random

from jinja2 import Template


def read_factors(factors_csv):
    """Reads factors from csv file"""

    with open(factors_csv, encoding='utf8') as f:
        reader = csv.DictReader(f)
        factors = collections.defaultdict(list)

        for row in reader:
            for key, value in row.items():
                if value != '':
                    factors[key].append(value)

        return factors


class FSDesign:

    def __init__(self, text_template, factors, size, duplicates=False):
        self.text_template = Template(text_template)
        self.factors = factors
        self.size = size
        self.duplicates = duplicates

    def sample(self, size):
        """chooses size random combinations of factors."""

        all_combinations = self.get_all_combinations()

        return random.sample(all_combinations, size)

    def choices(self, size):
        """Chooses size combinations of factors. It may contain repetitions"""

        all_combinations = self.get_all_combinations()

        return random.choices(all_combinations, k=size)

    def get_all_combinations(self):
        """Get all possible combinations of Factors in a list of namedtuple's"""
        Combination = collections.namedtuple('Combination', self.factors.keys())

        return list(itertools.starmap(Combination, itertools.product(*self.factors.values())))

    def generate_vignettes(self):
        """
        Generate texts using different combinations of factors
        """

        if self.duplicates is False:
            vignette_params = self.sample(self.size)
        else:
            vignette_params = self.choices(self.size)

        for params in vignette_params:
            params_dict = params._asdict()
            yield self.text_template.render(params_dict), params_dict

    def to_csv(self, path):
        """Write vignettes to a csv file"""

        if self.duplicates is False:
            vignette_params = self.sample(self.size)
        else:
            vignette_params = self.choices(self.size)

        with open(path, 'w', encoding='utf8') as f:
            writer = csv.DictWriter(f, ['ID', 'Text'] + list(self.factors.keys()))
            writer.writeheader()
            for index, params in enumerate(vignette_params):
                params_dict = params._asdict()
                text = self.text_template.render(**params._asdict())

                id = index + 1
                row = {'ID': id, 'Text': text}
                row.update(params_dict)
                writer.writerow(row)
