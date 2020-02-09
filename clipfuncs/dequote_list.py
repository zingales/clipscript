

def get_clipboard_function(commandString):
    return dequote_list

def dequote_list(text):
    items_raw = text.split(",")
    items = [x.strip().replace("'", '').replace('"', '') for x in items_raw]
    return ", ".join(items)
