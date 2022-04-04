from enum import Enum
import subprocess


class CommandOption(Enum):
    START = "start"
    STOP = "stop"
    RESTART = "restart"


class LinuxDriver:
    SERVICE_NAME = "bluetooth"

    @classmethod
    def _prepare_command(cls, command: CommandOption):
        return ["sudo", "systemctl", command.value, cls.SERVICE_NAME]

    @classmethod
    def start(cls):
        subprocess.run(cls._prepare_command(CommandOption.START))

    @classmethod
    def stop(cls):
        subprocess.run(cls._prepare_command(CommandOption.STOP))

    @classmethod
    def restart(cls):
        subprocess.run(cls._prepare_command(CommandOption.RESTART))
