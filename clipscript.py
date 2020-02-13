import rumps
import funcmanager
import logging
import clipboardmanager

class ClipScriptApp(object):

    def __init__(self):
        self.app = rumps.App("ClipScript", "⛽️", quit_button=None)

        self.rebuild_menu(None)

    def rebuild_menu(self, sender):
        logging.debug("building menu")
        suffix = \
        [
            None,
            [
                rumps.MenuItem("Options"),
                [ \
                    rumps.MenuItem("Refresh Functions", callback=self.rebuild_menu), \
                    rumps.MenuItem("Quit", callback=rumps.quit_application)
                ], \
            ],

        ]


        menu_items = [self.menuify_func(name) for name in funcmanager.get_list_of_commands()]
        menu_items.extend(suffix)

        logging.debug("finished building menu")
        self.app.menu.clear()
        self.app.menu = menu_items


    def menuify_func(self, name):

        def clipboard_function(sender=None):

            logging.debug("function {0} was called".format(name))
            original_clipboard_text = clipboardmanager.get_latest()
            logging.debug("copied {0} from clipboard".format(original_clipboard_text))

            new_clipboard_text = funcmanager.get_command(name)(original_clipboard_text)
            logging.debug("new clipboard {0}".format(new_clipboard_text))

            # text sanitization
            if new_clipboard_text is None:
                logging.warning("command {0} returned a None instead of string, clipboard is unchanged".format(name))
                return


            clipboardmanager.put(new_clipboard_text)
            logging.debug("function {0} finished".format(name))


        return rumps.MenuItem(name.replace('_', ' '), callback=clipboard_function)

    def run(self):
        self.app.run()
