import sys, asyncio, os
sys.path.insert(0,'.')
import gen2
from genlib import A
import json;TWM=json.loads(os.environ.get('TWM','{}'));FM=json.loads(os.environ.get('FM','{"6":86}'));ARF=int(os.environ.get('ARF','44'));TF=int(os.environ.get('TF','74')); TW=int(os.environ.get('TW','520'))
orig=gen2.slides
def slides(c,h):
    out=orig(c,h)
    if c['n'] in (2,3,4,5,6,7):
        T=h>1400; top=270 if not T else 470
        out[0]=f"""<div style="position:absolute;left:72px;top:{top}px"><span class=tag>{c['tag']}</span></div>
<h1 style="position:absolute;left:72px;top:{top+90}px;width:{TWM.get(str(c['n']),TW)}px;font-size:{FM.get(str(c['n']),TF)}px">{c['title_en']}</h1>
<div class=div style="position:absolute;left:72px;top:{top+(600 if not T else 680)}px"><b></b></div>
<div class=ar style="position:absolute;left:72px;top:{top+(660 if not T else 740)}px;width:470px;font-size:{ARF}px;line-height:1.55;direction:rtl;text-align:left">{c['title_ar']}</div>
<div class=arch style="left:630px;top:{top-20}px;width:378px;height:{760 if not T else 980}px"><img class=f src="{A('pose_PUB%d.jpg'%c['n'])}" style="object-position:50% 50%"></div>
<div class=cap style="left:72px;top:{h-210}px;font-family:Cormorant;font-style:italic;font-size:32px">Swipe →</div>"""
    return out
gen2.slides=slides
asyncio.run(gen2.main(sys.argv[1],[2,3,4,5,6,7]))
