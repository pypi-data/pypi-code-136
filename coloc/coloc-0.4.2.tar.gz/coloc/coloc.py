#!/usr/bin/env python3
#===============================================================================
# coloc.py
#===============================================================================

# Imports ======================================================================

import math
import pandas as pd
import sumstats




# Functions ====================================================================

def coloc(
    trait1_lnbfs,
    trait2_lnbfs,
    prior1: float = 1e-4,
    prior2: float = 1e-4,
    prior12: float = 1e-5
):
    """Perform a Bayesian colocalization test (with two traits)

    Parameters
    ----------
    trait1_lnbfs
        sequence of log Bayes factors for the first trait
    trait2_lnbfs
        sequence of log Bayes factors for the second trait
    prior1
        first prior parameter for the colocalization model [1e-4]
    prior2
        second prior parameter for the colocalization model [1e-4]
    prior12=1e-5
        third prior parameter for the colocalization model [1e-5]
    
    Returns
    -------
    generator
        posterior probabilities for the five colocalization hypotheses
    """

    log_numerators = (
        0,
        math.log(prior1) + sumstats.log_sum(trait1_lnbfs),
        math.log(prior2) + sumstats.log_sum(trait2_lnbfs),
        math.log(prior1) + math.log(prior2) + sumstats.log_sum(
            trait1_lnbf + trait2_lnbf
            for i, trait1_lnbf in enumerate(trait1_lnbfs)
            for j, trait2_lnbf in enumerate(trait2_lnbfs)
            if i != j
        ),
        math.log(prior12) + sumstats.log_sum(
            trait1_lnbf + trait2_lnbf
            for trait1_lnbf, trait2_lnbf in zip(trait1_lnbfs, trait2_lnbfs)
        )
    )
    yield from  (
        math.exp(log_numerator - sumstats.log_sum(log_numerators))
        for log_numerator in log_numerators
    )


def log_diff(x, y):
    if x + y == 0:
        return 0
    if x == y:
        return 0
    m = max(x, y)
    if x > y:
        return m + math.log(math.exp(x - m) - math.exp(y - m))
    if y > x:
        return m + math.log(math.exp(y - m) - math.exp(x - m))


def moloc(
    trait1_lnbfs,
    trait2_lnbfs,
    trait3_lnbfs,
    priors=(1e-4, 1e-6, 1e-7)
):
    """Perform a Bayesian colocalization test (with three traits)

    Parameters
    ----------
    trait1_lnbfs
        sequence of log Bayes factors for the first trait
    trait2_lnbfs
        sequence of log Bayes factors for the second trait
    trait2_lnbfs
        sequence of log Bayes factors for the third trait
    priors
        sequence of three priors [(1e-4, 1e-6, 1e-7)]

    Returns
    -------
    generator
        posterior probabilities for the 15 colocalization hypotheses
    """

    lnbfs = {
        'a': trait1_lnbfs,
        'b': trait2_lnbfs,
        'c': trait3_lnbfs,
        'ab': tuple(
            lnbf1 + lnbf2 for lnbf1, lnbf2 in zip(trait1_lnbfs, trait2_lnbfs)
        ),
        'bc': tuple(
            lnbf2 + lnbf3 for lnbf2, lnbf3 in zip(trait2_lnbfs, trait3_lnbfs)
        ),
        'ac': tuple(
            lnbf1 + lnbf3 for lnbf1, lnbf3 in zip(trait1_lnbfs, trait3_lnbfs)
        ),
        'abc': tuple(
            lnbf1 + lnbf2 + lnbf3
            for lnbf1, lnbf2, lnbf3 in zip(
                trait1_lnbfs, trait2_lnbfs, trait3_lnbfs
            )
        )
    }
    print(lnbfs)
    configs = (
        "a", "b", "c", "ab", "bc", "ac", "a,b", "b,c", "a,c", "a,bc", "ab,c",
        "ac,b", "a,b,c", "abc"
    )
    config_ppas = pd.DataFrame(
        index=('z',) + configs,
        columns=('prior', 'sumbf', 'loglkl')
    )
    config_ppas.loc['z'] = [0.999, 0, 0]
    for config in configs:
        if ',' not in config:
            prior = priors[len(config) - 1]
            config_ppas.loc[config, 'prior'] = prior
            config_ppas.loc[config, 'sumbf'] = sumstats.log_sum(lnbfs[config])
    for config in configs:
        if ',' in config:
            left_trait_bfs = 0
            prior_num = 1
            composite_configs = config.split(',')
            for c in composite_configs:
                left_trait_bfs += config_ppas.loc[c, 'sumbf']
                prior_num *= config_ppas.loc[c, 'prior']
            coloc_config = ''.join(sorted(config.replace(',', '')))
            right_trait_bfs = config_ppas.loc[coloc_config, 'sumbf']
            config_bf = log_diff(left_trait_bfs, right_trait_bfs)
            config_ppas.loc[config, 'sumbf'] = config_bf
            config_ppas.loc[config, 'prior'] = prior_num
        config_ppas.loc[config, 'loglkl'] = (
            math.log(config_ppas.loc[config, 'prior'])
            + config_ppas.loc[config, 'sumbf']
        )
    log_denomenator = sumstats.log_sum(config_ppas.loc[:, 'loglkl'])
    yield from (
        math.exp(log_numerator - log_denomenator)
        for log_numerator in config_ppas.loc[:, 'loglkl']
    )


def ascii_bar(prob: float):
    """Draw an ascii bar to display a probability

    Parameters
    ----------
    prob
        the probability value to display
    
    Returns
    -------
    string
        the ascii bar
    """
    level = int(prob * 20)
    return '[{}{}]'.format('|' * int(level), ' ' * (20-level))


def print_coloc_result(
    title: str,
    pp0: float,
    pp1: float,
    pp2: float,
    pp3: float,
    pp4: float
):
    """Print an ascii representation of the colocalization test result

    Parameters
    ----------
    title
        a title for the ascii art
    pp0
        the posterior probability of H0: no association
    pp1
        the posterior probability of H1: association in trait 1 only
    pp2
        the posterior probability of H2: association in trait 2 only
    pp3
        the posterior probability of H3: independent associations
    pp4
        the posterior probability of H4: colocalized associations
    """
    
    print(
        '\n'.join(
            ('', title, '') + tuple(
                'PP{}: {} [ {} ]'.format(i, ascii_bar(pp), pp)
                for i, pp in enumerate((pp0, pp1, pp2, pp3, pp4))
            )
            + ('',)
        )
    )


def print_moloc_result(
    title: str,
    pp
):
    """Print an ascii representation of the colocalization test result

    Parameters
    ----------
    title
        a title for the ascii art
    pp
        iterable of posterior probabilities
    """
    
    print(
        '\n'.join(
            ('', title, '') + tuple(
                'PP{}: {} [ {} ]'.format(i, ascii_bar(ppi), ppi)
                for i, ppi in enumerate(pp)
            )
            + ('',)
        )
    )
    