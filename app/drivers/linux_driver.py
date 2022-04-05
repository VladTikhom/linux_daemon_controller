import subprocess
from enum import Enum
from typing import List


class CommandOption(Enum):
    START = "start"
    STOP = "stop"
    RESTART = "restart"


class LinuxDriver:
    SERVICE_NAME = "bluetooth"

    @classmethod
    def _prepare_command(cls, command: CommandOption) -> List[str]:
        return ["sudo", "systemctl", command.value, cls.SERVICE_NAME]

    @classmethod
    def _execute_command(cls, command: CommandOption) -> int:
        return subprocess.run(cls._prepare_command(command)).returncode

    @classmethod
    def start(cls) -> int:
        return cls._execute_command(CommandOption.START)

    @classmethod
    def stop(cls) -> int:
        return cls._execute_command(CommandOption.STOP)

    @classmethod
    def restart(cls) -> int:
        return cls._execute_command(CommandOption.RESTART)
