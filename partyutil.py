"""Utility functions for the party app."""


def is_mel(name, email):
    """Return True if either name or email are related to Mel.

    >>> is_mel('hi', 'hi')
    False
    >>> is_mel('melton', 'mel@ubermelon.com')
    True
    >>> is_mel('MEL', 'MEL@UBERMELON.COM')
    True
    >>> is_mel('MeL', 'mel@gmail.com')
    True

    """
    full_Mel = 'Mel Melitpolski'
    mel_mail = 'mel@ubermelon.com'

    if name.lower() == full_Mel.lower():
        return True
    elif email.lower() == mel_mail.lower():
        return True
    elif name.lower() in full_Mel.lower():
        return True
    else:
        return False  



def most_and_least_common_type(treats):
    """Given list of treats, return most and least common treat types.

    Return most and least common treat types in tuple of format
    (most, least). If there's a tie, the dessert that appears
    first in alphabetical order should win.
    
    In cases of a tie, alphabetical order:

    >>> treats = [{'type': 'dessert'}, 
    ...         {'type': 'drink'}, 
    ...         {'type': 'appetizer'}, 
    ...         {'type': 'dessert'}, 
    ...         {'type': 'appetizer'}]
    ...
    >>> most_and_least_common_type(treats)
    ('appetizer', 'drink')
    
    Similarly, if there is one of everything, alphabet orders:

    >>> treats = [{'type': 'dessert'}, 
    ...           {'type': 'drink'}, 
    ...           {'type': 'appetizer'}]
    ...
    >>> most_and_least_common_type(treats)
    ('appetizer', 'appetizer')
    
    If treats is empty, return None, None: 
    
    >>> treats = []
    ...
    >>> most_and_least_common_type(treats)
    (None, None)
    """


    if not treats:
        return (None, None)

    types = {}

    # Count number of each type
    for treat in treats:
        types[treat['type']] = types.get(treat['type'], 0) + 1

    # Get tuples of (treat type, count) in alphabetical order
    types = sorted(types.items())

    # Find the min & max using the count of each tuple (which
    # is stored at index 1)
    most_type, _ = max(types, key=lambda treat_type: treat_type[1])
    least_type, _ = min(types, key=lambda treat_type: treat_type[1])

    return (most_type, least_type)
