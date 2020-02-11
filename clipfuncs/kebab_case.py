#!/usr/bin/python

import re

# not using string.uppercase to be python2/python3 compatible
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'


def get_clipboard_function(commandString):
    return to_kebab_case


def to_kebab_case(text):
    is_snake_case = '_' in text
    is_camel_case = (
        any(x in text for x in uppercase) and
        any(x in text for x in lowercase)
    )

    if is_snake_case:
        return re.sub('_', r'-', text)
    elif is_camel_case:
        # modified from
        # https://www.geeksforgeeks.org/python-program-to-convert-camel-case-string-to-snake-case/
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()
    else:
        return text
