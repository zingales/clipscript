import json

def get_clipboard_function(commandString):
    return json_pretty_print


def json_pretty_print(text):
    json_blob = json.loads(text)
    return json.dumps(json_blob, sort_keys=True, indent=4, separators=(',', ': '))
