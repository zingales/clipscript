import sys
import funcmanager
from clipscript import ClipScriptApp

import logging
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)

if __name__ == "__main__":
    logging.info("Starting App")
    ClipScriptApp().run()
