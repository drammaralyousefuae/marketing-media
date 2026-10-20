import sys, asyncio
from pathlib import Path
from playwright.async_api import async_playwright
B=Path(__file__).parent.resolve()
F=B/'node_modules/@fontsource'
def ff(fam,file,wt,style='normal'):
    return f"@font-face{{font-family:'{fam}';src:url('file://{F}/{file}') format('woff2');font-weight:{wt};font-style:{style}}}"
FONTS="".join([
 ff('Cormorant','cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2',600),
 ff('Cormorant','cormorant-garamond/files/cormorant-garamond-latin-700-normal.woff2',700),
 ff('Cormorant','cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2',600,'italic'),
 ff('Amiri','amiri/files/amiri-arabic-700-normal.woff2',700),
 ff('Amiri','amiri/files/amiri-latin-700-normal.woff2',700),
 ff('Cairo','cairo/files/cairo-arabic-400-normal.woff2',400),
 ff('Cairo','cairo/files/cairo-arabic-600-normal.woff2',600),
 ff('Inter','inter/files/inter-latin-400-normal.woff2',400),
 ff('Inter','inter/files/inter-latin-500-normal.woff2',500),
 ff('Inter','inter/files/inter-latin-600-normal.woff2',600)])
A=lambda n:f"file://{B}/assets/{n}"
CSS=FONTS+f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;background:#FBFAFB;position:relative;overflow:hidden;font-family:Inter,Cairo,sans-serif;color:#2B2229}}
.pat{{position:absolute;inset:0;background:url('{A('pattern_plum.png')}');background-size:360px 640px;opacity:.06}}
.logo{{position:absolute;left:72px;top:56px;width:64px}}
.sig{{position:absolute;right:72px;top:68px;text-align:right}}
.sig .ar{{font-family:Amiri;font-weight:700;font-size:26px;color:#66004C;line-height:1.1}}
.sig .en{{font-family:Cormorant;font-weight:600;font-size:23px;color:#3A0A2E;margin-top:4px}}
.sig i{{font-style:italic}}
.foot{{position:absolute;left:72px;right:72px;display:flex;justify-content:space-between;font-size:23px}}
.foot .h{{color:#66004C;font-weight:600}} .foot .n{{color:#7A6D76}}
.tag{{display:inline-block;border:1.5px solid #D9B8CC;border-radius:40px;padding:11px 28px;font-weight:600;letter-spacing:.14em;font-size:21px;color:#66004C;background:#F4F1F3}}
h1,h2{{font-family:Cormorant;font-weight:700;color:#3A0A2E;line-height:1.05}}
.ar{{font-family:Amiri;font-weight:700;color:#66004C;direction:rtl}}
.num{{font-family:Cormorant;font-weight:700;color:#D9B8CC;font-size:150px;line-height:.9}}
.div{{display:flex;align-items:center;gap:16px;width:340px;margin:30px 0}}
.div:before,.div:after{{content:'';flex:1;height:1.5px;background:#D9B8CC}}
.div b{{width:14px;height:14px;background:#B98FA8;transform:rotate(45deg)}}
.card{{border:1.5px solid #D9B8CC;border-radius:20px;background:#F4F1F3;padding:34px 42px}}
.card .e{{font-size:35px;line-height:1.45;color:#2B2229}}
.card .a{{font-family:Cairo;font-size:29px;line-height:1.7;color:#5A4E57;direction:rtl;margin-top:16px;font-weight:400}}
.arch{{position:absolute;border:2px solid #D9B8CC;border-radius:999px 999px 0 0;overflow:hidden;background:#F4F1F3}}
.fr{{position:absolute;border:2px solid #D9B8CC;border-radius:20px;overflow:hidden;background:#F4F1F3}}
img.f{{width:100%;height:100%;object-fit:cover;display:block}}
.cap{{position:absolute;font-size:23px;color:#5A4E57}}
.btn{{display:flex;align-items:center;justify-content:center;gap:18px;background:#66004C;color:#fff;border-radius:40px;font-weight:600;font-size:39px;padding:30px 0;width:700px}}
"""
def page(h,body,n,total=7):
    foot_y=h-110
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{CSS}body{{height:{h}px}}.foot{{top:{foot_y}px}}</style></head><body>
<div class=pat></div><img class=logo src="{A('logo_plum.png')}">
<div class=sig><div class=ar>فريق د. عمار</div><div class=en>Dr. Ammar <i>Team</i></div></div>
{body}
<div class=foot><span class=h>@drammaralyousefuae</span><span class=n>{n:02d} / {total:02d}</span></div></body></html>"""

def slides(h):
    T=h>1400   # tiktok tall
    top=270 if not T else 360
    S=[]
    # 1 cover
    S.append(f"""<div style="position:absolute;left:72px;top:{top}px"><span class=tag>ONE-DAY IMPLANT</span></div>
<h1 style="position:absolute;left:72px;top:{top+90}px;width:470px;font-size:96px">The one-day implant journey</h1>
<div class=div style="position:absolute;left:72px;top:{top+520}px"><b></b></div>
<div class=ar style="position:absolute;left:72px;top:{top+600}px;width:470px;font-size:50px;line-height:1.5;text-align:left;direction:rtl">رحلة زراعة اليوم الواحد</div>
<div class=arch style="left:590px;top:{top-20}px;width:418px;height:{(760 if not T else 980)}px"><img class=f src="{A('face_wide.jpg')}" style="object-position:50% 30%"></div>
<div class=cap style="left:72px;top:{top+(780 if not T else 1000)}px;width:900px;font-style:italic;color:#7A6D76;font-size:22px">Real case, shared with the patient's consent &nbsp;·&nbsp; حالة حقيقية بموافقة المريضة</div>
<div class=cap style="left:72px;top:{h-210}px;font-family:Cormorant;font-style:italic;font-size:32px">Swipe →</div>""")
    def text(num,title,ar,en,arb):
        return f"""<div class=num style="position:absolute;left:72px;top:{top-20}px">{num}</div>
<h2 style="position:absolute;left:72px;top:{top+150}px;width:936px;font-size:76px">{title}</h2>
<div class=ar style="position:absolute;left:72px;right:72px;top:{top+250}px;font-size:48px">{ar}</div>"""
    def card(y,en,arb):
        return f"""<div class=card style="position:absolute;left:72px;right:72px;top:{y}px"><div class=e>{en}</div><div class=a>{arb}</div></div>"""
    # 2 what
    S.append(text('01','What does “one day” mean?','شو يعني «يوم واحد»؟','','')+card(top+(380 if not T else 420),
      "The tooth is replaced with an implant and, when bone and gum allow it, a temporary tooth is fitted in the same visit.",
      "بنستبدل السن بغرسة، وإذا العظم واللثة بيسمحوا بنركّب سن مؤقت بنفس الزيارة."))
    # 3 planning (3D illustration based on the real X-ray)
    pl=(530 if not T else 780)
    S.append(text('02','Before the day: the plan','قبل اليوم: الخطة','','')+f"""<div class=fr style="left:{72 if T else 190}px;right:{72 if T else 190}px;top:{top+(330 if not T else 420)}px;height:{pl}px"><img class=f src="{A('implant3d.jpg')}" style="object-position:50% {70 if not T else 62}%"></div>
<div class=cap style="left:72px;top:{top+(330 if not T else 420)+pl+22}px;right:72px;line-height:1.5">A digital plan sets the implant position. Illustration based on a real X-ray.<br><span style="font-family:Cairo;direction:rtl;display:block;text-align:right">خطة رقمية بتحدد مكان الغرسة. رسم توضيحي مبني على أشعة حقيقية.</span></div>""")
    # 4 implant photo
    ph=(430 if not T else 700)
    S.append(text('03','The day: the implant is placed','يوم الزراعة: وضع الغرسة','','')+f"""<div class=fr style="left:72px;right:72px;top:{top+(380 if not T else 420)}px;height:{ph}px"><img class=f src="{A('implant.jpg')}"></div>
<div class=cap style="left:72px;top:{top+(380 if not T else 420)+ph+22}px;right:72px;line-height:1.5">Implant in place in the front area, with its abutment.<br><span style="font-family:Cairo;direction:rtl;display:block;text-align:right">الغرسة بمكانها بالمنطقة الأمامية مع الدعامة.</span></div>""")
    # 5 xray
    xh=(520 if not T else 760)
    S.append(text('04','Confirmed on X-ray','التأكد بالأشعة','','')+f"""<div class=fr style="left:72px;top:{top+(380 if not T else 420)}px;width:{int(xh*795/1100)}px;height:{xh}px"><img class=f src="{A('xray.jpg')}"></div>
<div style="position:absolute;left:{72+int(xh*795/1100)+44}px;right:72px;top:{top+(430 if not T else 480)}px"><div class=card style="padding:30px 34px"><div class=e style="font-size:31px">The X-ray shows the implant seated in the bone.</div><div class=a style="font-size:27px">الأشعة بتبيّن الغرسة مثبّتة داخل العظم.</div></div></div>""")
    # 6 result
    rh=(260 if not T else 420)
    S.append(text('05','The result','النتيجة','','')+f"""<div class=fr style="left:72px;right:72px;top:{top+(380 if not T else 420)}px;height:{rh}px"><img class=f src="{A('teeth.jpg')}"></div>
<div class=fr style="left:72px;right:72px;top:{top+(380 if not T else 420)+rh+24}px;height:{rh}px"><img class=f src="{A('smile.jpg')}" style="object-position:50% 55%"></div>""")
    # 7 cta
    cy=(350 if not T else 520)
    S.append(f"""<h1 style="position:absolute;left:72px;right:72px;top:{cy-120}px;text-align:center;font-size:76px">Is one day right for you?</h1>
<div class=ar style="position:absolute;left:72px;right:72px;top:{cy+70}px;text-align:center;font-size:46px">هل «اليوم الواحد» مناسب إلك؟</div>
<div style="position:absolute;left:150px;right:150px;top:{cy+190}px;text-align:center;font-size:30px;line-height:1.5;color:#5A4E57">It depends on your bone, gums and any infection. Your scan decides.<br><span style="font-family:Cairo;direction:rtl;display:block;margin-top:10px">بيعتمد على العظم واللثة وأي التهاب، والمسح هو اللي بقرر.</span></div>
<div class=div style="position:absolute;left:370px;top:{cy+400}px"><b></b></div>
<div style="position:absolute;left:190px;top:{cy+470}px"><div class=btn>Book with Ezza on WhatsApp</div>
<div class=ar style="text-align:center;font-size:30px;margin-top:22px;font-weight:700">احجز مع عزة عبر واتساب</div>
<div style="text-align:center;font-size:31px;color:#5A4E57;margin-top:46px">Or call us free <b style="color:#66004C;font-weight:600">800 016 0222</b></div>
<div style="text-align:center;font-size:31px;color:#5A4E57;margin-top:14px">drammar.ae</div></div>""")
    return S

async def main():
    out=Path(sys.argv[1]); 
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        for tag,h in [('ig',1350),('tt',1920)]:
            d=out/tag; d.mkdir(parents=True,exist_ok=True)
            for i,body in enumerate(slides(h),1):
                f=B/f'tmp_{tag}_{i}_{__import__('os').getpid()}.html'; f.write_text(page(h,body,i))
                pg=await br.new_page(viewport={'width':1080,'height':h})
                await pg.goto('file://'+str(f)); await pg.wait_for_timeout(400)
                await pg.screenshot(path=str(d/f'oneday_{tag}_{i}.jpg'),type='jpeg',quality=93)
                await pg.close()
        await br.close()
asyncio.run(main())
