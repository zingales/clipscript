import re

def get_clipboard_function(commandString):
    return list_to_lines


def list_to_lines(text):
    searchObj = re.search( r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+', text, re.M|re.I)
    return searchObj.group(0)
