

def get_clipboard_function(commandString):
    return list_to_lines


def list_to_lines(text):
    lines = text.split('\n')
    format_text = lines[0].strip()
    lines = lines[1:]

    text = ''
    for line in lines:
        replacements = line.strip().split(',')
        text+= format_text.format(*replacements) + '\n'

    return text
