import sys, re
from pathlib import Path

def analyze_chapter(ch):
    f = list(Path('chapters').glob(f'第{ch:03d}章*.md'))[0]
    txt = f.read_text(encoding='utf-8-sig')
    lines = [l.strip() for l in txt.splitlines() if l.strip() and not l.startswith('#')]
    dialogues = [l for l in lines if any(q in l for q in '“”')]
 print(f'=== CH {ch} ({f.name}) ===')
 print('Lines:', len(lines))
 print('Head 1:', lines[0])
 print('Head 2:', lines[1])
 print('Tail 2:', lines[-2])
 print('Tail 1:', lines[-1])
 print('Dialogues count:', len(dialogues))

for c in range(2, 11):
 analyze_chapter(c)