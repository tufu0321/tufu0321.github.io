#!/usr/bin/env python3
"""Run from repository root after copying the provided update files."""
from pathlib import Path
import re
p=Path('_config.yml')
if not p.exists(): raise SystemExit('Run this from the GitHub repository root (_config.yml not found).')
s=p.read_text(encoding='utf-8')
def top(key,value):
 global s
 pat=rf'(?m)^({re.escape(key)}\s*:\s*).*?$'
 s,n=re.subn(pat,lambda m:m.group(1)+value,s,count=1)
 if not n: raise ValueError('Missing config key '+key)
top('site_theme','"air"')
top('title','"Tufan Ghosh"')
top('description','"Research in porous media, multiscale modelling and phase-field methods"')
top('url','"https://tufu0321.github.io"')
top('baseurl','""')
top('repository','"tufu0321/tufu0321.github.io"')
# Anchor to author section; only replace field values there.
start=s.index('author:'); end=s.index('# Publication Category',start)
a=s[start:end]
for key,val in {'avatar':'"profile.png"','name':'"Tufan Ghosh"','bio':'"Porous media · Multiscale modelling · Phase-field methods"','location':'"Stuttgart, Germany"','employer':'"University of Stuttgart"','email':'"tufan.ghosh@iws.uni-stuttgart.de"','github':'"tufu0321"','googlescholar':'"https://scholar.google.com/citations?user=PS_CX0AAAAAJ"','orcid':'','pubmed':'','bluesky':''}.items():
 a=re.sub(rf'(?m)^(\s+{re.escape(key)}\s*:\s*).*?$',lambda m:m.group(1)+val,a,count=1)
s=s[:start]+a+s[end:]
# Load supplementary stylesheet through head include; no theme core files replaced.
p.write_text(s,encoding='utf-8')
print('Updated _config.yml. Verify the resulting profile details before publishing.')
