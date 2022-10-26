#!/usr/bin/env python3

# import qrcode
# import argparse
# from PIL import Image
from module.parser import parser


# def qr_generator(url):
#     logo = Image.open("strypes.png")

#     logo = logo.resize(
#         (80, int((float(logo.size[1]) * float(80 / float(logo.size[0]))))),
#         Image.LANCZOS,
#     )
#     # qr = qrcode.QRCode(version=1, box_size=10, border=10)
#     qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
#     qr.add_data(url)
#     qr.make()
#     qr_code = qr.make_image(fill_color="black", back_color="white").convert("RGB")
#     position = (
#         (qr_code.size[0] - logo.size[0]) // 2,
#         (qr_code.size[1] - logo.size[1]) // 2,
#     )
#     qr_code.paste(logo, position)
#     qr_code.save("qrcode.png")


# def parser():
#     my_parser = argparse.ArgumentParser(
#         prog="qr_code_generator",
#         usage="%(prog)s [-u,--url] URL link",
#         description="QR Code generator",
#         epilog="Enjoy",
#     )
#     my_parser.add_argument(
#         "-u", "--url", type=str, help="insert url link", required=True
#     )
#     args = my_parser.parse_args()
#     qr_generator(args.url)


if __name__ == "__main__":
    parser()
