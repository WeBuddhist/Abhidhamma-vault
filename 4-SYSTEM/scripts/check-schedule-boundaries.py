# -*- coding: utf-8 -*-
import re
L=open('1-SOURCES/Text/pi-2.md',encoding='utf-8').read().split('\n')
chap=None; span={}
for l in L:
    m=re.match(r'^###\s+(\S+)\s+\^2-(\d+)-0$', l)
    if m: chap=(int(m.group(2)),m.group(1)); span.setdefault(chap,[None,None])
    a=re.search(r'\^2-(\d+)$', l)
    if a and chap:
        n=int(a.group(1))
        if span[chap][0] is None: span[chap][0]=n
        span[chap][1]=n
present=sorted(int(x) for x in re.findall(r'\^2-(\d+)$', '\n'.join(L), re.M))
pset=set(present)

sched=[]
for l in open('3-TRANSFORMATIONS/Plans/Daily-Tipitaka/en/schedule.md',encoding='utf-8'):
    m=re.match(r'^\|\s*day-(\d+)\s*\|[^|]*\|\s*(\d+)\.\s*(\S+)\s*\|\s*(\d+)\s*(?:[–-]\s*(\d+))?\s*\|', l)
    if m:
        d=int(m.group(1))
        if 78<=d<=173:
            a=int(m.group(4)); b=int(m.group(5)) if m.group(5) else a
            sched.append((d,int(m.group(2)),m.group(3),a,b))
sched.sort()
print(f'{len(sched)} Book II day rows (single-verse rows now parsed), day-{sched[0][0]}..day-{sched[-1][0]}\n')

print('chapter-boundary check:')
bad=[]
for (num,name),(a,b) in sorted(span.items()):
    h=[d for d in sched if d[3]<=b<=d[4]]
    if not h: print(f'  ch.{num:2} {name:26} ends v{b:<5} -> NOT IN ANY DAY  <<<'); bad.append((num,name,b,None)); continue
    h=h[0]; ok=h[1]==num
    print(f'  ch.{num:2} {name:26} ends v{b:<5} -> day-{h[0]} ({h[3]}-{h[4]}) ch.{h[1]}  {"ok" if ok else "MISMATCH <<<"}')
    if not ok: bad.append((num,name,b,h))

print('\nstraddles:')
st=[d for d in sched if len({n for (n,_),(x,y) in span.items() if not (d[4]<x or d[3]>y)})>1]
print('  none' if not st else st)

print('\nscheduled verses that do not exist in pi-2.md:')
missing_sched=[]
for d in sched:
    for n in range(d[3],d[4]+1):
        if n not in pset: missing_sched.append((d[0],n))
print('  none' if not missing_sched else '  '+', '.join(f'day-{a}:^2-{b}' for a,b in missing_sched))

print('\nverses present in pi-2.md but in no scheduled day (Book II range):')
covered=set()
for d in sched: covered.update(range(d[3],d[4]+1))
lo=min(x for (_,_),(x,_) in [((k),v) for k,v in span.items()]) if span else 0
uncov=[n for n in present if n>=1 and n not in covered]
print('  none' if not uncov else '  '+', '.join(f'^2-{n}' for n in uncov))
