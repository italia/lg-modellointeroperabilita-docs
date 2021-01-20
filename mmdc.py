#!/usr/bin/env python
from argparse import ArgumentParser
from sys import argv
from sys import stdin, stdout
from pathlib import Path
from random import randint
from base64 import urlsafe_b64encode
import json
from requests import get
from img2pdf import convert as jpg_to_pdf


def get_mermaid_jpg(mermaid_text):
    mmd_o = json.dumps({"code": mermaid_txt})
    mmd_b64 = urlsafe_b64encode(mmd_o.encode())
    mermaid_url = f"https://mermaid.ink/img/{mmd_b64.decode()}"
    res = get(mermaid_url)
    if res.status_code > 299:
        raise SystemError("Malformed mermaid_txt: %s" % mermaid_url)
    return res.content


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-i", dest="spath", help="input file")
    parser.add_argument("-o", dest="dpath", help="destination file")
    args = parser.parse_args()


    mermaid_txt = Path(args.spath).read_text()
    # Rely on mermaid website for renderings.
    jpg_mermaid_txt = get_mermaid_jpg(mermaid_txt)

    # Latex expects a pdf image.
    img_pdf = jpg_to_pdf(jpg_mermaid_txt)
    Path(args.dpath).write_bytes(img_pdf)
    exit(0)
