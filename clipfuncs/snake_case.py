#!/usr/bin/python

import re

# not using string.uppercase to be python2/python3 compatible
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'


def get_clipboard_function(commandString):
    return to_snake_case


def to_snake_case(text):
    is_kebab_case = '-' in text
    is_camel_case = (
        any(x in text for x in uppercase) and
        any(x in text for x in lowercase)
    )
    if is_kebab_case:
        return re.sub('-', r'_', text)
    elif is_camel_case:
        # https://www.geeksforgeeks.org/python-program-to-convert-camel-case-string-to-snake-case/
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    else:
        return text
