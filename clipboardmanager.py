import pyperclip


def get_latest():
    return pyperclip.paste()

def put(text):
    pyperclip.copy(text)
