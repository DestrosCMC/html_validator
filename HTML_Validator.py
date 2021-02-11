#!/bin/python3

import re
from collections import deque


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    if len(html) == 0:
        return True
    tags = _extract_tags(html)
    if not tags:
        return False
    print(tags)
    s = deque()
    balanced = True
    index = 0

    while index < len(tags) and balanced:
        tag = tags[index]
        if '/' not in tag:
            s.append(tag)
        else:
            if not s:
                balanced = False
            else:
                top = s.pop()
                if not match(top, tag):
                    balanced = False
        index += 1
    if balanced and not s:
        return True
    else:
        return False

    # HINT:
    # use the _extract_tags function below to
    # generate a list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the book
    # the main difference between your code and
    # the book's code will be that you will have to keep
    # track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def match(first, second):
    first_rep, second_rep = first.replace('<', ""), second.replace('<', "")
    first_rep, second_rep = first.replace('>', ""), second.replace('>', "")
    first_rep, second_rep = first.replace('/', ""), second.replace('/', "")
    return first_rep == second_rep


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the
    input string,stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = re.findall(r'<[^>]+>', html)
#    if (not tags) and ('<' in html):
#        raise ValueError('found < without matching >')

    return tags
