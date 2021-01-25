#!/usr/bin/env python
from argparse import ArgumentParser
from pathlib import Path
from base64 import urlsafe_b64encode, b64encode
import json
from requests import get
from tempfile import NamedTemporaryFile
from subprocess import check_output


def jpg_to_pdf(jpg_data, dpath):
    with NamedTemporaryFile() as fh:
        fh.write(jpg_data)
        check_output(["./magick", "convert", fh.name, dpath])


def get_mermaid_jpg(mermaid_txt):
    mmd_o = json.dumps({"code": mermaid_txt})
    mmd_b64 = b64encode(mmd_o.encode())
    mermaid_url = "https://mermaid.ink/img/%s" % mmd_b64.decode()
    res = get(mermaid_url.strip())
    if res.status_code > 299:
        raise SystemError("Malformed mermaid_txt: %s" % mermaid_url)
    return res.content


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", dest="spath", help="input file")
    parser.add_argument("-o", dest="dpath", help="destination file")
    args = parser.parse_args()

    mermaid_txt = Path(args.spath).read_text()
    # Rely on mermaid website for renderings.
    mermaid_jpg = get_mermaid_jpg(mermaid_txt)

    # Latex expects a pdf image.
    jpg_to_pdf(mermaid_jpg, args.dpath)
    exit(0)
