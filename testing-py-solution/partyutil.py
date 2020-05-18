"""Utility functions for the party app."""


def is_mel(name, email):
    """Return True if name or email are related to Mel.

    It returns True if both name and email are Mel's; otherwise
    it returns False:

       >>> is_mel('Mel Melitpolski', 'mel@ubermelon.com')
       True
       >>> is_mel('Jane Doe', 'jane@email.com')
       False

    Also, it'll return True if either name OR email are Mel's:

       >>> is_mel('Mel', 'mel@ubermelon.com')
       True
       >>> is_mel('Mel Melitpolski', 'totallynotmel@mel.com')
       True
    """

    return name == 'Mel Melitpolski' or email == 'mel@ubermelon.com'


def most_and_least_common_type(treats):
    """Given list of treats, return most and least common treat types.

    Return most and least common treat types in tuple of format
    (most, least). For example:

       >>> treats = [{'type': 'cheese'}, {'type':'cheese'}, {'type': 'drink'}]
       >>> most_and_least_common_type(treats)
       ('cheese', 'drink')

    If there's a tie, the dessert that appears first in alphabetical
    order should win. For example:

       >>> treats = [
       ... {'type': 'drink'},
       ... {'type': 'drink'},
       ... {'type': 'pizza'},
       ... {'type': 'pizza'},
       ... {'type': 'fruit'}]
       >>> most_and_least_common_type(treats)
       ('drink', 'fruit')

    If treats is empty, return (None, None):

       >>> treats = []
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