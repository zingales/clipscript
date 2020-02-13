
func_description = "Given a comma seperated list, it adds single quotes around each item in the list"

def get_clipboard_function(commandString):
    return quote_list


def quote_list(text):
    items_raw = text.split(",")
    items = [x.strip() for x in items_raw]
    return ", ".join(["'{0}'".format(x) for x in items])
