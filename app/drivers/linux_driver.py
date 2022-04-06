import subprocess
from enum import Enum
from typing import List


class CommandOption(Enum):
    START = "start"
    STOP = "stop"
    RESTART = "restart"
    IS_ACTIVE = "is-active"

class LinuxDriver:
    SERVICE_NAME = "bluetooth"

    @classmethod
    def _prepare_command(cls, command: CommandOption) -> List[str]:
        return ["sudo", "systemctl", command.value, cls.SERVICE_NAME]

    @classmethod
    def _execute_command(cls, command: CommandOption):
        return subprocess.run(cls._prepare_command(command), stdout=subprocess.PIPE)

    @classmethod
    def start(cls) -> int:
        return cls._execute_command(CommandOption.START).returncode

    @classmethod
    def stop(cls) -> int:
        return cls._execute_command(CommandOption.STOP).returncode

    @classmethod
    def restart(cls) -> int:
        return cls._execute_command(CommandOption.RESTART).returncode

    @classmethod
    def state(cls) -> bool:
        return cls._execute_command(CommandOption.IS_ACTIVE).stdout.decode().strip() == "active"
