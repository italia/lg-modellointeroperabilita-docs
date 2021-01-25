import re, yaml

from pathlib import Path
from hashlib import sha256

import docutils.statemachine
import docutils.parsers.rst.tableparser


def parse_grid_table(text):
    # Clean up the input: get rid of empty lines and strip all leading and
    # trailing whitespace.
    lines = filter(bool, (line.strip() for line in text.splitlines()))
    parser = docutils.parsers.rst.tableparser.GridTableParser()
    return parser.parse(docutils.statemachine.StringList(list(lines)))


def process_line(line):
    line = line.strip()
    line = line.replace("**", "")
    return "   " + line


def unbox_as_list_table(txt):
    colspecs, header, body = parse_grid_table(txt)
    ret = ""
    for y in body:
        for i, x in enumerate(y):
            try:
                _, _, _, content = x
                ret += "   \n  " if bool(i) else "   \n* "
                ret += "- "
                ret += "\n".join(process_line(x) for x in content)
            except Exception as e:
                raise ValueError("Error parsing %r" % x)
    return ret


def test_unbox_as_list_table():

    txt = """
+-----------------------------------+-----------------------------------+
| **Sigla**                         | **URI**                           |
+-----------------------------------+-----------------------------------+
| Canonical XML 1.0                 | http://www.w3.org/TR/2001/REC-xml |
|                                   | -c14n-20010315                    |
+-----------------------------------+-----------------------------------+
| Canonical XML 1.1                 | http://www.w3.org/2006/12/xml-c14 |
|                                   | n11                               |
+-----------------------------------+-----------------------------------+
| Exclusive XML Canonicalization    | Exclusive XML Canonicalization    |
| 1.0                               | 1.0                               |
+-----------------------------------+-----------------------------------+
"""
    ret = unbox_as_list_table(txt)
    print(ret)
    raise NotImplementedError


def unbox(txt):
    ph_table = "\n\+-+\+\n"
    re_1 = f"({ph_table}.*?{ph_table})"

    def _save_external_file(txt, lang):
        dpath = Path(f"file-" + sha256(txt.encode()).hexdigest() + f".{lang}")
        dpath.write_text(txt)
        return f"\n.. literalinclude:: {dpath}" f"\n   :language: {lang}" "\n"

    def _ret(m):
        needle = m.group(1)
        colspecs, header, body = parse_grid_table(needle)
        if len(colspecs) > 1:
            return needle

        if header:
            return needle

        if not body:
            return needle

        matrix = body[0][0]
        _, _, _, content = matrix

        # Basic file processing
        ret = "\n".join(process_line(x) for x in content) + "\n"

        lang = "python"
        if "openapi: " in needle:
            lang = "yaml"
            return _save_external_file(ret, lang)

        if "<wsdl:definitions" in needle:
            lang = "xml"
            return _save_external_file(ret, lang)

        if "**HTTP**" in needle:
            lang = "http"
        elif needle.strip().endswith("}"):
            lang = "json"
        return f"\n.. code-block:: {lang}\n\n" + ret

    res = re.sub(re_1, _ret, txt, flags=re.DOTALL)
    return res


def test_box():
    expected, data = (
        """
.. code-block::
  http://<dominioOrganizzativo>/[rest|soap]/<DominioApplicativo>/v<majo 
  r>[.<minor>[.<patch>]]/<NomeAPI>
  
""",
        """
+-----------------------------------------------------------------------+
| http://<dominioOrganizzativo>/[rest|soap]/<DominioApplicativo>/v<majo |
| r>[.<minor>[.<patch>]]/<NomeAPI>                                      |
+-----------------------------------------------------------------------+
""",
    )

    assert unbox(data) == expected


def deleteme(txt):
    ph_table = "\n\+-+\+\n"
    re_1 = f"{ph_table}(.*?){ph_table}"

    def _ret(m):
        needle = m.group(1)
        return "\n.. code-block:: python\n\n" + "\n".join(
            [re.sub("^ +", "   ", x.strip().strip("|")) for x in needle.splitlines()]
        )

    res = re.sub(re_1, _ret, txt, flags=re.DOTALL)
    return res


def mmd(x):
    s = yaml.load(x.group(1))["source"]
    s = s.replace(r"\\n", "\n").replace("\\n", "")
    lines = s.splitlines()
    lines = ["   " + lines[0]] + [" " * 5 + l for l in lines[1:]]
    s = "\n".join(lines)
    return f".. mermaid::\n\n  {s}\n\n"


def test_mermaid():
    txt = fh.read_text()

    re_2 = r'\|(\{"theme.*\})\|'
    re_1 = r"\.\. \|(\{.*\})\|"
    out = re.sub(re_1 + "|" + re_2, mmd, txt, flags=re.DOTALL)


import os
import contextlib
from pathlib import Path


@contextlib.contextmanager
def working_directory(path):
    """Changes working directory and returns to previous on exit."""
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


if __name__ == "__main__":
    from sys import argv

    progname, fpath = argv[:2]
    fh = Path(fpath)
    txt = fh.read_text()
    oldpwd = fh.cwd()
    with working_directory(fh.parent) as newpwd:
        out = unbox(txt)
    fh.write_text(out)
