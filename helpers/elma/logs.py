import logging
import os
import sys


class Log:
    formatter_template = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self, name, level=logging.DEBUG, path=None):
        self.path = path
        self.log = logging.getLogger(name)
        self.log.setLevel(level)
        self._configure_stdout()
        if path:
            self.path = os.path.join(os.getcwd(), '{}.log'.format(name))
            self._configure_file_handler()

    def __getattr__(self, attr):
        return getattr(self.log, attr)

    def _configure_stdout(self):
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_formatter = logging.Formatter(self.formatter_template)
        stdout_handler.setFormatter(stdout_formatter)
        self.addHandler(stdout_handler)

    def _configure_file_handler(self):
        file_handler = logging.FileHandler(self.path)
        file_formatter = logging.Formatter(self.formatter_template)
        file_handler.setFormatter(file_formatter)
        self.addHandler(file_handler)
