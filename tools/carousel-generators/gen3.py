import sys, asyncio
sys.path.insert(0,'.')
from pathlib import Path
from genlib import page, A, B
from playwright.async_api import async_playwright

CARS=[
dict(n=25,date="2026-11-16",slug="gaps-not-cosmetic",tag="TEETH GAPS",cover_img="d3_f.png",cover_pos="50% 55%",
 title_en="Gaps between your teeth are not always cosmetic",title_ar="فراغات الأسنان مو دايماً مشكلة تجميلية",
 note_en="Real case, shared with the patient's consent",note_ar="حالة حقيقية بموافقة المريضة",
 slides=[
 dict(t=("It looks like a smile problem","بتبان مشكلة تجميل"),img="gaps_front.png",pos="50% 50%",
  cap=("Gaps between the front teeth: most people think it is only about looks.","فراغات الأسنان الأمامية: كتير ناس بيحسبوها مسألة شكل بس.")),
 dict(t=("But a gap can be a signal","بس الفراغ ممكن يكون إشارة"),
  card=("Teeth drift apart when the bone, the tongue or the jaw is not supporting them well. The mouth may be showing you something bigger.","الأسنان بتتباعد لما العظم أو اللسان أو الفك ما عم يدعموها منيح. الفم ممكن عم يعرض عليك شي أكبر.")),
 dict(t=("Behind the teeth: the airway","ورا الأسنان: مجرى التنفس"),img="sag_wide.png",pos="50% 50%",
  cap=("On the CT scan, the airway looks narrow. Its value: 2.3 mm.","بالأشعة المقطعية بيظهر ضيق مجرى التنفس، وقيمته 2.3 ملم.")),
 dict(t=("What you may be feeling","شو ممكن تكون عم تحس"),
  card=("Tiredness, poor focus and attention, headaches, raised blood pressure. These are linked with disturbed sleep and breathing. Linked does not mean the cause in every case.","تعب، ضعف تركيز وانتباه، صداع، ارتفاع ضغط. هي أعراض مرتبطة باضطراب النوم والتنفس. مرتبط ما بيعني السبب بكل حالة.")),
 dict(t=("When to get checked","متى بتحتاج فحص"),
  card=("Gaps between your teeth and any of these symptoms? A full assessment of the jaw, tongue and airway can find the link.","فراغات بين أسنانك وأي من هالأعراض؟ التقييم الشامل للفك واللسان والمجرى بيلاقي الرابط.")),
 ],
 cta=("Gaps and symptoms? Contact us.","فراغات وأعراض؟ تواصل معنا."),
 cta_note=("A full assessment shows whether the gaps are only cosmetic.","التقييم الشامل بيبيّن إذا الفراغات تجميلية بس.")),
dict(n=26,date="2026-11-17",slug="recession-hidden-cause",tag="BONE & GUM RECESSION",cover_img="d3_r.png",cover_pos="50% 55%",
 title_en="Bone and gum recession: bacteria, or something bigger?",title_ar="انحسار العظم واللثة: جراثيم ولا سبب أكبر؟",
 note_en="Real case, shared with the patient's consent",note_ar="حالة حقيقية بموافقة المريضة",
 slides=[
 dict(t=("Bacteria are part of the story","الجراثيم جزء من القصة"),
  card=("Plaque and gum disease cause recession in many people. But when it is severe and affects the front teeth, it is worth asking why.","الجراثيم والتهاب اللثة بيسببوا انحسار عند كتير ناس. بس لما يكون شديد وبالأسنان الأمامية، بيستاهل نسأل ليش.")),
 dict(t=("What a 3D CT scan shows","شو بتبيّن الأشعة المقطعية ثلاثية الأبعاد"),img="rec_side.png",pos="50% 50%",
  cap=("Severe bone and gum recession: the tooth roots are exposed. Real case.","انحسار شديد بالعظم واللثة، وجذور الأسنان مكشوفة. حالة حقيقية.")),
 dict(t=("Is treating the gums enough?","يكفي نعالج اللثة؟"),
  card=("Cleaning and gum treatment are needed. But if the underlying cause is not found, the recession can return.","التنظيف وعلاج اللثة ضروريين. بس إذا ما لقينا السبب الأساسي، الانحسار ممكن يرجع.")),
 dict(t=("Tongue, jaw and airway","اللسان والفك والمجرى"),img="sag_wide.png",pos="50% 50%",
  cap=("On the CT scan, the airway narrows to 2.3 mm: it may be part of the picture.","بالأشعة المقطعية المجرى بيضيق لـ 2.3 ملم: ممكن يكون جزء من الصورة.")),
 dict(t=("Questions to ask your doctor","أسئلة اسألها لطبيبك"),
  card=("Why here? Why so severe? Have my jaw, tongue and airway been assessed, or only my gums?","ليش بهالمكان؟ ليش شديد؟ هل تقيّم فكي ولساني ومجرى تنفسي، ولا لثتي بس؟")),
 ],
 cta=("Recession on your front teeth?","انحسار بأسنانك الأمامية؟"),
 cta_note=("Find the cause, not only the symptom.","ندوّر على السبب، مو على العرَض بس.")),
]

def slides(c,h):
    T=h>1400; top=270 if not T else 470
    S=[]
    ph=(470 if not T else 760)
    S.append(f"""<div style="position:absolute;left:72px;top:{top}px"><span class=tag>{c['tag']}</span></div>
<h1 style="position:absolute;left:72px;top:{top+90}px;width:470px;font-size:{68 if len(c['title_en'])<40 else 58}px">{c['title_en']}</h1>
<div class=div style="position:absolute;left:72px;top:{top+(600 if not T else 680)}px"><b></b></div>
<div class=ar style="position:absolute;left:72px;top:{top+(660 if not T else 740)}px;width:470px;font-size:42px;line-height:1.55;direction:rtl;text-align:left">{c['title_ar']}</div>
<div class=arch style="left:556px;top:{top-20}px;width:452px;height:{760 if not T else 980}px"><img class=f src="{A(c['cover_img'])}" style="object-position:{c['cover_pos']}"></div>
<div class=cap style="left:72px;top:{top+(790 if not T else 1010)}px;width:940px;font-style:italic;color:#7A6D76;font-size:22px">{c['note_en']} &nbsp;·&nbsp; {c['note_ar']}</div>
<div class=cap style="left:72px;top:{h-210}px;font-family:Cormorant;font-style:italic;font-size:32px">Swipe →</div>""")
    for i,s in enumerate(c['slides'],1):
        te,ta=s['t']; long=len(te)>=28
        y0=top+(380 if not T else 420)+(50 if long else 0)
        head=f"""<div class=num style="position:absolute;left:72px;top:{top-20}px">{i:02d}</div>
<h2 style="position:absolute;left:72px;top:{top+150}px;width:936px;font-size:{76 if not long else 62}px">{te}</h2>
<div class=ar style="position:absolute;left:72px;right:72px;top:{top+(250 if not long else 290)}px;font-size:{48 if not long else 42}px">{ta}</div>"""
        if 'chart' in s:
            rows=s['chart']; ce,ca=s['cap']; y1=top+(340 if not T else 440)
            bars=''.join(f'<div style="margin-bottom:26px"><div style="display:flex;justify-content:space-between;font-size:28px;font-weight:600;color:#3A0A2E"><span>{l}</span><span>{v}</span></div><div style="height:30px;background:#E9E1E6;border-radius:15px;margin-top:8px;position:relative"><div style="position:absolute;left:0;top:0;height:30px;width:{max(w,0.8)}%;background:{col};border-radius:15px"></div></div></div>' for l,v,w,col in rows)
            body=f'<div class=card style="position:absolute;left:72px;right:72px;top:{y1}px;padding:{44 if not T else 60}px 48px">{bars}</div><div class=cap style="left:72px;right:72px;top:{y1+(470 if not T else 560)}px;line-height:1.45;font-size:24px">{ce}<br><span style="font-family:Cairo;direction:rtl;display:block;text-align:right;margin-top:4px">{ca}</span></div>'
            S.append(head+body); continue
        if 'card' in s:
            e,a=s['card']
            body=f"""<div class=card style="position:absolute;left:72px;right:72px;top:{y0}px;padding:{46 if not T else 56}px 52px"><div class=e style="font-size:{40 if not T else 46}px">{e}</div><div class=a style="font-size:{33 if not T else 37}px;margin-top:26px">{a}</div></div>"""
        else:
            ce,ca=s['cap']
            fh=(530 if not T else 760)-(50 if long else 0); y0=top+(330 if not T else 420)+(50 if long else 0)
            if s.get('fit'): fh=(1075-y0) if not T else 585
            body=f"""<div class=fr style="left:72px;right:72px;top:{y0}px;height:{fh}px"><img class=f src="{A(s['img'])}" style="object-position:{s['pos']}"></div>
<div class=cap style="left:72px;right:72px;top:{y0+fh+20}px;line-height:1.45;font-size:25px">{ce}<br><span style="font-family:Cairo;direction:rtl;display:block;text-align:right;margin-top:4px">{ca}</span></div>"""
        S.append(head+body)
    cy=350 if not T else 640
    ce,ca=c['cta']; ne,na=c['cta_note']
    S.append(f"""<h1 style="position:absolute;left:72px;right:72px;top:{cy-120}px;text-align:center;font-size:70px">{ce}</h1>
<div class=ar style="position:absolute;left:72px;right:72px;top:{cy+40}px;text-align:center;font-size:46px">{ca}</div>
<div style="position:absolute;left:130px;right:130px;top:{cy+150}px;text-align:center;font-size:30px;line-height:1.5;color:#5A4E57">{ne}<br><span style="font-family:Cairo;direction:rtl;display:block;margin-top:10px">{na}</span></div>
<div class=div style="position:absolute;left:370px;top:{cy+370}px"><b></b></div>
<div style="position:absolute;left:190px;top:{cy+440}px"><div class=btn>Book with Ezza on WhatsApp</div>
<div class=ar style="text-align:center;font-size:30px;margin-top:22px;font-weight:700">احجز مع عزة عبر واتساب</div>
<div style="text-align:center;font-size:31px;color:#5A4E57;margin-top:46px">Or call us free <b style="color:#66004C;font-weight:600">800 016 0222</b></div>
<div style="text-align:center;font-size:31px;color:#5A4E57;margin-top:14px">drammar.ae</div></div>""")
    return S

async def main(root):
    root=Path(root)
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        for c in CARS:
            for tag,h in [('ig',1350),('tt',1920)]:
                d=root/f"{c['date']}-{c['slug']}"/'v1'/tag; d.mkdir(parents=True,exist_ok=True)
                for i,body in enumerate(slides(c,h),1):
                    f=B/f'tmp3_{tag}_{__import__('os').getpid()}.html'; f.write_text(page(h,body,i))
                    pg=await br.new_page(viewport={'width':1080,'height':h})
                    await pg.goto('file://'+str(f)); await pg.wait_for_timeout(300)
                    await pg.screenshot(path=str(d/f"{c['date']}-{c['slug']}_{tag}_{i}.jpg"),type='jpeg',quality=92)
                    await pg.close()
        await br.close()
if __name__=='__main__': asyncio.run(main(sys.argv[1]))
