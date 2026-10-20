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

