import pyperclip
import os
import sys
import importlib
import pkgutil
import pathlib

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def match_command_with_package(commandName, packageName):
    return commandName == packageName


def import_from_path(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def get_command(commandString):
    for (lama, name, lama2) in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__), "clipfuncs")]):

        if match_command_with_package(commandString, name):
            path = "{0}/clipfuncs/{1}.py".format(
                pathlib.Path(__file__).parent.absolute(), name)
            return import_from_path(path, name).get_clipboard_function(commandString)
            # imported_module = import_module(path)

    logging.warning("No package found. looked for package path: {0}, with command string".format(
        "{0}/clipfuncs/{1}.py".format(pathlib.Path(__file__).parent.absolute(), name), commandString))


if __name__ == "__main__":
    to_execute = sys.argv[1:]
    text = pyperclip.paste()
    # logging.debug('clipboard text: \n{0}'.format(text))
    for name in to_execute:
        text = get_command(name)(text)
        # text sanitization
        if text is None:
            logging.warning(
                "command {0} returned a None instead of string".format(name))
            sys.exit()

    # logging.debug('saving this text to the clipboard: \n{0}'.format(text))
    pyperclip.copy(text)
