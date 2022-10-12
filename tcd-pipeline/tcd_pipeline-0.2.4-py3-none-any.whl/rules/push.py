"""Evaluate push event with push rules

Examples
--------
    event : dict
        refType: branch
        refName: release/dev
        changes:
          - Dockerfilex
          - src/main/java/Main.java

    rules : list[dict]
        when:
          push:
            - type: branch # [branch, tag]
              matcher: exact # [ regex, glob, semver, exact] https://semver.org/#is-v123-a-semantic-version
              value: master  #
            - type: branch
              matcher: glob
              value: release/*
              changes: # When one of this file list changed.
                - "Dockerfile"
                - "src/main/java/**.java"
            - type: tag
              matcher: semver
            - type: tag
              matcher: regex
              value: release/.+
"""
import re
from fnmatch import fnmatch

import tcd_pipeline.rules.changes as changes_rules
from jsonpath_ng.ext import parse


def is_git_ref_match_glob(rules: list[dict], fact: dict) -> bool:
    """Evaluate fact matched with glob

    Parameters
    ----------
    rule : list[dict]
        List of rule.

        Example: list of rules
        [
          {
            'type': 'branch',
            'matcher': 'glob',
            'value': 'release/*',
            'changes': [
              'Dockerfile',
              'src/main/java/**.java'
            ]
          }
        ]
    fact : dict
        Git push event data

        Example:
        {
          'refType', 'branch',
          'refName', 'release/dev',
          'changes', [
            'Dockerfile',
            'src/main/java/Main.java'
          ]

        }
    """

    actual: str = fact.get("refName")
    fact_ref_type: str = fact.get("refType")
    jsonpath_expr = parse(f"$..push[?((@.type=='{fact_ref_type}')&(@.matcher=='glob'))]")
    for rule in jsonpath_expr.find(rules):
        if fnmatch(actual, rule.value.get("value")):
            return changes_rules.is_changes_match_glob(
              glob_patterns=rule.value.get("changes"),
              facts=fact.get("changes")
            )

    return False


def is_git_ref_match_regex(rules: list[dict], fact: dict) -> bool:
    """Evaluate fact matched with regex

    Parameters
    ----------
    rule : list[dict]
        List of rule.

        Example: list of rules
        [
          {
            'type': 'branch',
            'matcher': 'regex',
            'value': 'release/.+',
            'changes': [
              'Dockerfile',
              'src/main/java/**.java'
            ]
          }
        ]
    fact : dict
        Git push event data

        Example:
        {
          'refType', 'branch',
          'refName', 'release/dev',
          'changes', [
            'Dockerfile',
            'src/main/java/Main.java'
          ]
        }
    """

    actual: str = fact.get("refName")
    fact_ref_type: str = fact.get("refType")
    jsonpath_expr = parse(f"$..push[?((@.type=='{fact_ref_type}')&(@.matcher=='regex'))]")
    for rule in jsonpath_expr.find(rules):
        if bool(re.match(pattern=rule.value.get("value"), string=actual)):
            return changes_rules.is_changes_match_glob(
              glob_patterns=rule.value.get("changes"),
              facts=fact.get("changes")
            )

    return False


def is_git_ref_match_semver(rules: list[dict], fact: dict) -> bool:
    """Evaluate fact matched with semver

    Parameters
    ----------
    rule : list[dict]
        List of rule.

        Example: list of rules
        [
          {
            'type': 'branch',
            'matcher': 'semver'
            'value': '(?i)((v|version|release)[\.\-\/]?)?', # prefix
            'changes': [
              'Dockerfile',
              'src/main/java/**.java'
            ]
          }
        ]
    fact : dict
        Git push event data

        Example:
        {
          'refType', 'branch',
          'refName', 'release/dev',
          'changes', [
            'Dockerfile',
            'src/main/java/Main.java'
          ]

        }
    """

    actual: str = fact.get("refName")
    fact_ref_type: str = fact.get("refType")
    jsonpath_expr = parse(f"$..push[?((@.type=='{fact_ref_type}')&(@.matcher=='semver'))]")
    for rule in jsonpath_expr.find(rules):
        # default semver prefix
        prefix_regex_pattern = '(?i)((v|version|release)[\.\-\/]?)?'
        semver_regex_pattern = '\d+(\.\d+){0,2}(\-.+)?'

        # Replace default prefix from rule value
        if rule.value.get("value"):
            prefix_regex_pattern = rule.value.get("value")
        regex_pattern = f"{prefix_regex_pattern}{semver_regex_pattern}"

        if bool(re.match(pattern=regex_pattern, string=actual)):
            return changes_rules.is_changes_match_glob(
              glob_patterns=rule.value.get("changes"),
              facts=fact.get("changes")
            )

    return False


def is_git_ref_match_exact(rules: list[dict], fact: dict) -> bool:
    """Evaluate fact matched with semver

    Parameters
    ----------
    rule : list[dict]
        List of rule.

        Example: list of rules
        [
          {
            'type': 'branch',
            'matcher': 'exact',
            'value': 'develop',
            'changes': [
              'Dockerfile',
              'src/main/java/**.java'
            ]
          }
        ]
    fact : dict
        Git push event data

        Example:
        {
          'refType', 'branch',
          'refName', 'develop',
          'changes', [
            'Dockerfile',
            'src/main/java/Main.java'
          ]

        }
    """

    actual: str = fact.get("refName")
    fact_ref_type: str = fact.get("refType")
    jsonpath_expr = parse(f"$..push[?((@.type=='{fact_ref_type}')&(@.matcher=='exact'))]")
    for rule in jsonpath_expr.find(rules):
        if rule.value.get("value") == actual:
            return changes_rules.is_changes_match_glob(
              glob_patterns=rule.value.get("changes"),
              facts=fact.get("changes")
            )

    return False
