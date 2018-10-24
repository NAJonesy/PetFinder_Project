import logging
import logging.handlers
import logging.config
import sys
import os

class Logger:
    def __init__(self,logLevel = None):
        logging.addLevelName(5,"RESULT")
        current_directory = os.path.dirname(os.path.realpath(__file__))
        current_path = os.path.join(current_directory, 'logging.conf')
        logging.config.fileConfig(current_path,disable_existing_loggers = False)
        self.note = logging.getLogger(__name__)
        self.detail = logging.getLogger("detailLogger")


logger = Logger(logLevel=logging.DEBUG)