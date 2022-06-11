from src.interface.ui import banner
from src.pinkerton.main import check_host

from argparse import ArgumentParser

if __name__ == "__main__":

    banner()

    parser = ArgumentParser()
    parser.add_argument("-u", help="Specify the target URL", required=True)
    args = parser.parse_args()

    check_host(args)