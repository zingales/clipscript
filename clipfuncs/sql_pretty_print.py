import sqlparse

def get_clipboard_function(commandString):
    return list_to_lines


def list_to_lines(text):
    return sqlparse.format(text, reindent=True, keyword_case='upper')
