#!/usr/bin/python

def get_clipboard_function(commandString):
    return to_camel_case

def to_camel_case(text):
    is_kebab_case = '-' in text
    is_snake_case = '_' in text

    if is_kebab_case:
        words = text.split('-')
        return (
            words[0] + ''.join(w.title() for w in words[1:]) if words
            else ''
        )
    elif is_snake_case:
        words = text.split('_')
        return (
            words[0] + ''.join(w.title() for w in words[1:]) if words
            else ''
        )
    else:
        return text
