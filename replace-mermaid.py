import re
from pathlib import Path
import sys
import yaml

fh = Path(sys.argv[1])


def mmd(x):
    s = yaml.load(x.group(1))["source"]
    s = s.replace(r"\\n", "\n").replace("\\n", "")
    lines = s.splitlines()
    lines = ["   " + lines[0]] + [" " * 5 + l for l in lines[1:]]
    s = "\n".join(lines)
    return f".. mermaid::\n\n  {s}\n\n"


txt = fh.read_text()

re_2 = r'\|(\{"theme.*\})\|'
re_1 = r"\.\. \|(\{.*\})\|"
out = re.sub(re_1 + "|" + re_2, mmd, txt, flags=re.DOTALL)
print(out)
fh.write_text(out)
