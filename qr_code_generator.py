#!/usr/bin/env python3

import qrcode
import argparse


def qr_generator(url):
    qr = qrcode.QRCode(version=1, box_size=7, border=7)
    qr.add_data(url)
    qr.make()
    qr.make_image(fill_color="black", back_color="white").save("qrcode.png")


def main():
    my_parser = argparse.ArgumentParser(
        prog="qr_code_generator",
        usage="%(prog)s [-u,--url] URL link",
        description="QR Code generator",
        epilog="Enjoy",
    )
    my_parser.add_argument(
        "-u", "--url", type=str, help="insert url link", required=True
    )
    args = my_parser.parse_args()
    qr_generator(args.url)


if __name__ == "__main__":
    main()
