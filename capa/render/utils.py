import termcolor


def bold(s):
    """draw attention to the given string"""
    return termcolor.colored(s, 'blue')


def capability_rules(doc):
    """enumerate the rules in (namespace, name) order that are 'capability' rules (not lib/subscope/disposition/etc)."""
    for rule in sorted(map(lambda rule: (rule['meta']['namespace'], rule['meta']['name'], rule), doc.values())):
        if rule['meta'].get('lib'):
            continue
        if rule['meta'].get('capa/subscope'):
            continue
        if rule['meta'].get('maec/analysis-conclusion'):
            continue
        if rule['meta'].get('maec/analysis-conclusion-ov'):
            continue
        if rule['meta'].get('maec/malware-category'):
           continue
        if rule['meta'].get('maec/malware-category-ov'):
            continue

        yield rule
