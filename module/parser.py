import argparse
from module.generator import qr_generator


def parser():
    my_parser = argparse.ArgumentParser(
        prog="qr_code_generator",
        usage="%(prog)s [-u,--url] URL link",
        usage="%(prog)s [-o, --output] output file",
        description="QR Code generator",
        epilog="Enjoy",
    )
    my_parser.add_argument(
        "-u", "--url", type=str, help="insert url link", required=True
    )
    my_parser.add_argument(
        "-o", "--output", type=str, help="write output", required=True
    )
    args = my_parser.parse_args()
    qr_generator(args.url, args.output)
