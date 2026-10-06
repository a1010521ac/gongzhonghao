import sys, re
from pathlib import Path

for ch in range(2, 11):
    f = list(Path('chapters').glob(f'第{ch:03d}章*.md'))[0]
    txt = f.read_text(encoding='utf-8-sig')
    lines = [l.strip() for l in txt.splitlines() if l.strip() and not l.startswith('#')]
    print(f'CH {ch}: lines={len(lines)} chars={len(txt)}')
