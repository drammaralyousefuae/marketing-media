import sys, json, re
sys.path.insert(0,'.')
import gen3
src=open('gen4.py').read().split("gen3.CARS=CARS")[0].replace("import gen3","")
ns={'gen3':gen3,'sys':sys}
src=src.replace("import sys, asyncio","import asyncio")
exec(src,ns)
CARS=ns['CARS']+gen3.CARS
RAW="https://raw.githubusercontent.com/drammaralyousefuae/marketing-media/main/posts"
T={8:("#SleepStudy #DeepSleep #Polysomnography #SleepHealth #DrAmmarAlYousef #Dubai #UAE #دراسة_النوم #النوم_العميق #دبي","Why 8 hours of sleep can still leave you tired"),
9:("#BloodPressure #SleepApnea #HeartHealth #SleepStudy #DrAmmarAlYousef #Dubai #UAE #ضغط_الدم #النوم #دبي","Blood pressure 258 during sleep?"),
10:("#CBCT #3DScan #Airway #SleepHealth #DrAmmarAlYousef #Dubai #UAE #الأشعة_المقطعية #مجرى_الهواء #دبي","The 3D CT scan that shows your airway"),
11:("#BlockedNose #MouthBreathing #Turbinates #Sinus #DrAmmarAlYousef #Dubai #UAE #انسداد_الأنف #التنفس_من_الفم #دبي","Why can't you breathe through your nose?"),
12:("#Tongue #SpacedTeeth #Airway #MouthBreathing #DrAmmarAlYousef #Dubai #UAE #اللسان #فراغات_الأسنان #دبي","A tongue with no room"),
25:("#TeethGaps #Airway #CBCT #SleepHealth #DrAmmarAlYousef #Dubai #UAE #فراغات_الأسنان #مجرى_الهواء #دبي","Gaps between teeth: not always cosmetic"),
26:("#GumRecession #BoneLoss #CBCT #Airway #DrAmmarAlYousef #Dubai #UAE #انحسار_اللثة #العظم #دبي","Bone and gum recession: bacteria or more?"),
27:("#BloodPressure #SleepApnea #HeartHealth #Airway #DrAmmarAlYousef #Dubai #UAE #ضغط_الدم #انقطاع_النفس #دبي","Why pressure surges when breathing struggles"),
28:("#HeartRate #SleepApnea #HeartHealth #SleepStudy #DrAmmarAlYousef #Dubai #UAE #نبض_القلب #النوم #دبي","A heart at 140 beats while you sleep"),
29:("#NightBloodPressure #SleepHealth #HeartHealth #DrAmmarAlYousef #Dubai #UAE #ضغط_الليل #النوم #دبي","Normal at the clinic, abnormal at night"),
30:("#RootCause #Airway #Jaw #SleepHealth #DrAmmarAlYousef #Dubai #UAE #السبب_الجذري #الفك #دبي","Finding the cause behind the numbers")}
def line(s):
    te,ta=s['t']
    if 'card' in s: e,a=s['card']
    elif 'cap' in s: e,a=s['cap']
    elif 'chart' in s: e,a=s['cap']
    else: e=a=''
    return f"{te}: {e}",f"{ta}: {a}"
new=[]
for c in CARS:
    n=c['n']; tags,tt=T[n]
    L=[line(s) for s in c['slides']]
    cap=(f"{c['title_en']}\n\n"+"\n".join("• "+x[0] for x in L)+f"\n\n{c['cta'][0]} {c['cta_note'][0]}\n\n{c['note_en']}.\n\nSwipe through, and save this post for later.\n\nBook your assessment with Ezza on WhatsApp: wa.me/971585555958\n\nFree call: 800 016 0222 | drammar.ae\n\n"
     f"{c['title_ar']}\n\n"+"\n".join("• "+x[1] for x in L)+f"\n\n{c['cta'][1]} {c['cta_note'][1]}\n\n{c['note_ar']}.\n\nتصفّح الشرائح، واحفظ المنشور لترجع له.\n\nاحجز فحصك مع عزة على واتساب: wa.me/971585555958\n\nمكالمة مجانية: 8000160222 | drammar.ae\n\nفريق د. عمار | Dr. Ammar Team\n\n{tags}")
    tx=f"{c['title_en']} {c['cta'][0]} Book with Ezza on WhatsApp. {c['title_ar']} {tags}"
    base=f"{RAW}/{c['date']}-{c['slug']}/v1"
    new.append(dict(n=n,date=c['date'],slug=c['slug'],ig_caption=cap,tt_text=tx[:900],tt_title=tt[:90],
      ig_media=[f"{base}/ig/{c['date']}-{c['slug']}_ig_{i}.jpg" for i in range(1,8)],
      tt_media=[f"{base}/tt/{c['date']}-{c['slug']}_tt_{i}.jpg" for i in range(1,8)]))
old=json.load(open('captions.json'))
keep=[o for o in old if o['n'] not in {x['n'] for x in new}]
# reels
def reel(n,date,slug,en,ar,tags,tt):
    cap=f"{en}\n\nComment WHATSAPP and we send you the link to book with Ezza.\nFree call: 800 016 0222 | drammar.ae\n\n{ar}\n\nعلّق «واتساب» وبنبعتلك رابط الحجز مع عزة.\nمكالمة مجانية: 8000160222 | drammar.ae\n\nفريق د. عمار | Dr. Ammar Team\n\n{tags}"
    return dict(n=n,date=date,slug=slug,type='reel',ig_caption=cap,tt_text=(en+" "+tags)[:900],tt_title=tt,
      video=f"{RAW}/{date}-{slug}/v1/{date}-{slug}.mp4")
reels=[reel(31,"2026-11-18","gaps-not-cosmetic-reel","Gaps between your teeth plus tiredness or poor focus? The cause may be deeper than looks.","فراغات بين أسنانك مع تعب أو ضعف تركيز؟ السبب ممكن يكون أعمق من الشكل.","#TeethGaps #Airway #SleepHealth #DrAmmarAlYousef #Dubai #UAE #فراغات_الأسنان #دبي","Teeth gaps and tiredness: is there a link?"),
reel(32,"2026-11-19","recession-hidden-cause-reel","Bone and gum recession: find the cause, not only the symptom.","انحسار العظم واللثة: ندوّر على السبب مو العرَض بس.","#GumRecession #BoneLoss #Airway #DrAmmarAlYousef #Dubai #UAE #انحسار_اللثة #دبي","Gum recession: the hidden cause")]
allc=sorted(keep+new+reels,key=lambda o:(o['date'],o['n']))
json.dump(allc,open('captions.json','w'),ensure_ascii=False,indent=1)
print(len(allc),max(len(o['ig_caption']) for o in allc),max(len(o['tt_text']) for o in allc))
for o in allc:
    if len(o['ig_caption'])>2200: print('LONG',o['n'],len(o['ig_caption']))
