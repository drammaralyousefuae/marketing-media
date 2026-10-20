import sys, json
sys.path.insert(0,'.')
from carousels_b import C
from datetime import date, timedelta
RAW="https://raw.githubusercontent.com/drammaralyousefuae/marketing-media/main/posts"
out=[]
for c in C:
    en=[f"{s[0]}: {s[2]}" for s in c['slides']]
    ar=[f"{s[1]}: {s[3]}" for s in c['slides']]
    cap=(f"{c['title_en']}\n\n"+"\n".join("• "+x for x in en)+f"\n\n{c['cta'][0]}\n\nSwipe through, and save this post for later.\n\nBook your assessment with Ezza on WhatsApp: wa.me/971585555958\n\nFree call: 800 016 0222 | drammar.ae\n\n"
         f"{c['title_ar']}\n\n"+"\n".join("• "+x for x in ar)+f"\n\n{c['cta'][1]}\n\nتصفّح الشرائح، واحفظ المنشور لترجع له.\n\nاحجز فحصك مع عزة على واتساب: wa.me/971585555958\n\nمكالمة مجانية: 8000160222 | drammar.ae\n\nفريق د. عمار | Dr. Ammar Team\n\n{c['tags']}")
    tt=f"{c['title_en']} {c['cta'][0]} Book with Ezza on WhatsApp. {c['title_ar']} {c['tags']}"
    base=f"{RAW}/{c['date']}-{c['slug']}/v1"
    out.append(dict(n=c['n'],date=c['date'],slug=c['slug'],ig_caption=cap,tt_text=tt[:900],tt_title=c['tt'][:90],
        ig_media=[f"{base}/ig/{c['date']}-{c['slug']}_ig_{i}.jpg" for i in range(1,8)],
        tt_media=[f"{base}/tt/{c['date']}-{c['slug']}_tt_{i}.jpg" for i in range(1,8)]))
json.dump(out,open('captions.json','w'),ensure_ascii=False,indent=1)
print(len(out), max(len(o['ig_caption']) for o in out), max(len(o['tt_text']) for o in out))
