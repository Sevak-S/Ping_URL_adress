"""This pic of program is running url"""

import argparse
import subprocess
import re


def create_parser():
    """
    The function create parser for you can set your link as argument
    :return: string
    """
    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument(dest='url')
    return parser


def ping_ip(url_address):
    """
    :param url_address: set your link of website,
    you can set without http/https/www
    :return: status of your link address
    """
    if re.search(r"(http|https)\:\/\/", url_address):
        url_address = url_address.split("//")[1]

    reply = subprocess.run(
        f"ping {url_address}",
        check=True,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='CP866'
        # errors='ignore'
    )

    if reply.returncode == 0:
        print(reply.stdout)
    else:
        print(reply.stdout + reply.stderr)


if __name__ == "__main__":
    link = input()
    ping_ip(link)
