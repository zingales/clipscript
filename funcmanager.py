import os
import sys
import importlib
import pkgutil
import pathlib

import logging


class ModuleFailedToImport(Exception):
    pass

class ModuleMissingClipboardFunction(Exception):
    pass

class FailureInGettingClipboardFunction(Exception):
    pass

def match_command_with_package(commandName, packageName):
    return commandName == packageName


def import_from_path(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def find_command(commandString):
    for (_, name, _) in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__),"clipfuncs")]):

        if match_command_with_package(commandString, name):
            path = "{0}/clipfuncs/{1}.py".format(pathlib.Path(__file__).parent.absolute(), name)
            return import_from_path(path, name).get_clipboard_function(commandString)
            # imported_module = import_module(path)


    logging.warning("no package matched {0}".format(commandString))


def get_module(name):
    try:
        logging.debug("trying to get command {0}".format(name))
        path = "{0}/clipfuncs/{1}.py".format(pathlib.Path(__file__).parent.absolute(), name)
        logging.debug("looking for command in {0}".format(path))
        module = import_from_path(path, name)
        logging.debug("module loaded {0}".format(type(module)))
        logging.debug("module fields:\n{0}".format(dir(module)))
        return module
    except Exception:
        logging.exception("Failure in loading module {0}".format(name))
        raise ModuleFailedToImport("Failure in loading module {0}".format(name))


def get_command(name):
    module = get_module(name)
    if hasattr(module, 'func_description'):
        logging.debug('func description:"{0}"'.format(module.func_description))

    if not hasattr(module, 'get_clipboard_function'):
        logging.warn("module {0} does not have get_clipboard_function and thus cannot be run")
        raise ModuleMissingClipboardFunction("module {0} does not have get_clipboard_function and thus cannot be run".format(name))

    try:
        logging.debug("got clipboard function {0}".format(module.get_clipboard_function))
        func = module.get_clipboard_function(name)
        logging.debug("func loaded {0}".format(func))
        return func
    except Exception as e:
        logging.exception("Failure in getting func {0}".format(name))
        raise FailureInGettingClipboardFunction(e)


def get_list_of_commands():
    return [name for (_, name, _) in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__),"clipfuncs")]) if not name.startswith('_')]
