import argparse
import os
import subprocess
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class CommandResult:
    cmd: str
    output: str
    error: str
    exit_code: int


class Command:
    def __init__(self, cmd):
        self.command = cmd

    @staticmethod
    def get_result(cmd, captures=True, encodes="UTF-8", **kwargs):
        return subprocess.run(
            cmd, shell=True, capture_output=captures, encoding=encodes, **kwargs
        )

    @staticmethod
    def wrap_result(cmd_process):
        return CommandResult(
            cmd=cmd_process.args,
            output=cmd_process.stdout,
            error=cmd_process.stderr,
            exit_code=cmd_process.returncode,
        )

    def execute(self):
        return self.wrap_result(self.get_result(self.command))
