import sys, asyncio
sys.path.insert(0,'.')
from pathlib import Path
from genlib import page, A, B
from playwright.async_api import async_playwright
from carousels_b import C

def slides(c,h):
    T=h>1400; top=(270 if not T else 470)
    out=[]
    # cover
    bd=c.get('badge'); badge=(f'<div style="position:absolute;left:600px;top:{top+(640 if not T else 860)}px;background:#66004C;color:#FBFAFB;font-family:Cormorant;font-weight:700;font-size:54px;padding:10px 30px;border-radius:40px">{bd}</div>' if bd else '')
    out.append(f"""<div style="position:absolute;left:72px;top:{top}px"><span class=tag>{c['tag']}</span></div>
<h1 style="position:absolute;left:72px;top:{top+90}px;width:470px;font-size:{76 if len(c['title_en'])<42 else 64}px">{c['title_en']}</h1>
<div class=div style="position:absolute;left:72px;top:{top+(560 if not T else 640)}px"><b></b></div>
<div class=ar style="position:absolute;left:72px;top:{top+(630 if not T else 710)}px;width:470px;font-size:44px;line-height:1.55;direction:rtl;text-align:left">{c['title_ar']}</div>
<div class=arch style="left:566px;top:{top-20}px;width:442px;height:{760 if not T else 980}px;background:#F4F1F3"><img class=f src="{A('pose_'+c['pose']+'.jpg')}" style="object-position:50% 12%"></div>
{badge}<div class=cap style="left:72px;top:{h-210}px;font-family:Cormorant;font-style:italic;font-size:32px">Swipe →</div>""")
    for i,(te,ta,be,ba) in enumerate(c['slides'],1):
        if i in c.get('imgs',{}):
            im,pos=c['imgs'][i]; long=len(te)>=28
            fh=(440 if not T else 700)-(50 if long else 0); yy=top+(330 if not T else 420)+(50 if long else 0)
            out.append(f"""<div class=num style="position:absolute;left:72px;top:{top-20}px">{i:02d}</div>
<h2 style="position:absolute;left:72px;top:{top+150}px;width:936px;font-size:{76 if not long else 62}px">{te}</h2>
<div class=ar style="position:absolute;left:72px;right:72px;top:{top+(250 if not long else 290)}px;font-size:{48 if not long else 42}px">{ta}</div>
<div class=fr style="left:72px;right:72px;top:{yy}px;height:{fh}px"><img class=f src="{A(im)}" style="object-position:{pos}"></div>
<div class=cap style="left:72px;right:72px;top:{yy+fh+18}px;line-height:1.4;font-size:25px">{be}<br><span style="font-family:Cairo;direction:rtl;display:block;text-align:right;margin-top:4px">{ba}</span></div>""")
            continue
        y0=top+(380 if not T else 420)
        out.append(f"""<div class=num style="position:absolute;left:72px;top:{top-20}px">{i:02d}</div>
<h2 style="position:absolute;left:72px;top:{top+150}px;width:936px;font-size:{76 if len(te)<28 else 62}px">{te}</h2>
<div class=ar style="position:absolute;left:72px;right:72px;top:{top+(250 if len(te)<28 else 290)}px;font-size:{48 if len(ta)<28 else 42}px">{ta}</div>
<div class=card style="position:absolute;left:72px;right:72px;top:{y0+(20 if len(te)<28 else 50)}px;padding:{46 if not T else 56}px 52px"><div class=e style="font-size:{(42 if not T else 48) if len(be)<150 else (34 if not T else 40)}px">{be}</div><div class=a style="font-size:{(34 if not T else 38) if len(be)<150 else (28 if not T else 33)}px;margin-top:22px">{ba}</div></div>""")
    cy=350 if not T else 640
    ce,ca=c['cta']
    out.append(f"""<h1 style="position:absolute;left:72px;right:72px;top:{cy-120}px;text-align:center;font-size:70px">{ 'Questions about your case?' }</h1>
<div class=ar style="position:absolute;left:72px;right:72px;top:{cy+40}px;text-align:center;font-size:46px">عندك سؤال عن حالتك؟</div>
<div style="position:absolute;left:130px;right:130px;top:{cy+150}px;text-align:center;font-size:30px;line-height:1.5;color:#5A4E57">{ce}<br><span style="font-family:Cairo;direction:rtl;display:block;margin-top:10px">{ca}</span></div>
<div class=div style="position:absolute;left:370px;top:{cy+370}px"><b></b></div>
<div style="position:absolute;left:190px;top:{cy+440}px"><div class=btn>Book with Ezza on WhatsApp</div>
<div class=ar style="text-align:center;font-size:30px;margin-top:22px;font-weight:700">احجز مع عزة عبر واتساب</div>
<div style="text-align:center;font-size:31px;color:#5A4E57;margin-top:46px">Or call us free <b style="color:#66004C;font-weight:600">800 016 0222</b></div>
<div style="text-align:center;font-size:31px;color:#5A4E57;margin-top:14px">drammar.ae</div></div>""")
    return out

async def main(root, only=None):
    root=Path(root)
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        for c in C:
            if only and c['n'] not in only: continue
            for tag,h in [('ig',1350),('tt',1920)]:
                d=root/f"{c['date']}-{c['slug']}"/'v1'/tag; d.mkdir(parents=True,exist_ok=True)
                for i,body in enumerate(slides(c,h),1):
                    f=B/f'tmp2_{tag}_{__import__('os').getpid()}.html'; f.write_text(page(h,body,i))
                    pg=await br.new_page(viewport={'width':1080,'height':h})
                    await pg.goto('file://'+str(f)); await pg.wait_for_timeout(250)
                    await pg.screenshot(path=str(d/f"{c['date']}-{c['slug']}_{tag}_{i}.jpg"),type='jpeg',quality=92)
                    await pg.close()
        await br.close()
only=[int(x) for x in sys.argv[2:]] or None
asyncio.run(main(sys.argv[1],only))
