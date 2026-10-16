#!/usr/bin/env python3
"""Rebuild the standalone demo using only the Python standard library."""
from pathlib import Path
import html

root = Path(__file__).resolve().parent
shell = (root / 'source' / 'shell.html').read_text(encoding='utf-8')
frame = (root / 'source' / 'frame.html').read_text(encoding='utf-8')
placeholder = '__ATELIER_SRCDOC__'
if shell.count(placeholder) != 1:
    raise SystemExit('Expected exactly one frame placeholder in source/shell.html')
output = root / 'dist' / 'index.html'
output.parent.mkdir(exist_ok=True)
output.write_text(shell.replace(placeholder, html.escape(frame, quote=True)), encoding='utf-8')
print('Built dist/index.html')
