import sys, asyncio
sys.path.insert(0,'.')
import gen3
CN="Real case, identity removed"; CA="حالة حقيقية، الهوية محذوفة"
def car(n,date,slug,tag,pose,title,tar,slides,cta,ctan):
    return dict(n=n,date=date,slug=slug,tag=tag,cover_img=f"pose_{pose}.jpg",cover_pos="50% 18%",
      title_en=title,title_ar=tar,note_en=CN,note_ar=CA,slides=slides,cta=cta,cta_note=ctan)
S=lambda t,e,a,**k:dict(t=t,card=(e,a),**k)
CARS=[
car(8,"2026-10-27","reading-sleep-study","SLEEP STUDY","P10","Reading an 8-hour sleep study","قراءة تحليل النوم 8 ساعات",[
 S(("Breathing index: 1.6","مؤشر التنفس: 1.6"),"An AHI of 1.6 is normal. On breathing pauses alone, this night looks fine.","مؤشر 1.6 طبيعي. من ناحية انقطاع النفس لوحده، الليلة بتبان تمام."),
 S(("But the sleep itself is not normal","بس النوم نفسه مو طبيعي"),"Only light sleep stages. No real deep sleep at all. The body was in bed for 8 hours, but it is as if it never slept.","مراحل نوم خفيف بس. ولا نوم عميق. الجسم كان بالتخت 8 ساعات، بس كأنه ما نام."),
 dict(t=("Zero minutes of deep sleep","صفر دقيقة نوم عميق"),chart=[("Stage 1 (lightest sleep)","64%",64,"#B98FA8"),("Deep sleep","0 min",0,"#66004C"),("REM sleep","0 min",0,"#66004C")],
  cap=("From this study. Typical adults spend only a small share of the night in stage 1 and a much larger share in deep sleep.","من هالدراسة. البالغ عادةً بيقضي جزء صغير بالمرحلة الأولى وجزء أكبر بكتير بالنوم العميق.")),
 S(("What deep sleep does","شو بيعمل النوم العميق"),"Deep sleep helps the brain store memories and clear waste, and helps the body repair itself and regulate hormones and blood sugar.","النوم العميق بيساعد الدماغ يخزّن الذاكرة وينظّف نفسه، وبيساعد الجسم يصلّح حاله وينظّم الهرمونات والسكر."),
 S(("When deep sleep stays missing","لما النوم العميق يضل ناقص"),"Studies link long-term loss of deep sleep with memory problems, higher blood pressure, blood sugar changes and a higher dementia risk. The longer it lasts, the more it matters.","دراسات بتربط فقدان النوم العميق لفترة طويلة بمشاكل ذاكرة، وضغط أعلى، وتغيّر بالسكر، وخطر أعلى للخرف. وكل ما طالت المدة كل ما زادت الأهمية."),
 ],("Sleeping 8 hours but waking tired?","بتنام 8 ساعات وبتصحى تعبان؟"),("The cause may be in your jaw and airway.","السبب ممكن يكون بفكك ومجرى تنفسك.")),
car(9,"2026-10-28","bp-hr-peaks-1","SLEEP STUDY · 1/5","P03","Blood pressure peaks during sleep","ذروة ضغط الدم أثناء النوم",[
 S(("Peak: 258/146 mmHg","الذروة: 258/146"),"258 is the highest systolic pressure recorded during the night: the pressure when the heart pushes blood out.","258 هو أعلى ضغط انقباضي سُجّل بالليل: الضغط لما القلب بيدفع الدم."),
 S(("What sleep should look like","كيف المفروض يكون النوم"),"Asleep, blood pressure usually falls and stays below about 120/80, and the heart rate often settles around 50 to 60 beats per minute.","وأنت نايم الضغط عادةً بينزل ويضل تحت حوالي 120/80، والنبض غالباً بيهدا حوالي 50 لـ 60 بالدقيقة."),
 S(("Heart rate: up to 140","النبض: لحد 140"),"While asleep, the pulse reached 140 beats per minute. That is the rate of someone exercising, not resting.","وهو نايم، النبض وصل 140 بالدقيقة. هاد معدل شخص عم يتمرن، مو نايم."),
 S(("Values like these are dangerous","هيك قيم خطيرة"),"Readings in this range can threaten life and raise the risk of a sudden cardiac or brain event. They are not numbers to wait on.","قراءات بهالمستوى ممكن تهدد الحياة وبترفع خطر حدث مفاجئ بالقلب أو الدماغ. مو أرقام ننتظرها."),
 S(("The cause in this case: the jaw","السبب بهالحالة: الفك"),"In this case, the assessment points to the jaw and airway structure as what disturbs breathing, and so the pressure and pulse, all night.","بهالحالة، التقييم بيشير لشكل الفك والمجرى كسبب باضطراب التنفس، وبالتالي الضغط والنبض، طول الليل."),
 ],("High blood pressure and poor sleep?","ضغط عالي ونوم سيئ؟"),("Ask for an assessment of your jaw and airway.","اطلب تقييم لفكك ومجرى تنفسك.")),
car(10,"2026-10-29","ct-scan-airway","CT SCAN","P11","The 3D CT scan that shows the cause","الأشعة المقطعية ثلاثية الأبعاد اللي بتبيّن السبب",[
 dict(t=("Side view: 2.3 mm","منظر جانبي: 2.3 ملم"),fit=True,img="airway_ann.png",pos="50% 50%",cap=("The narrowest point of the airway, behind the tongue.","أضيق نقطة بمجرى التنفس، ورا اللسان.")),
 S(("This is a standing person","هاد شخص واقف"),"The scan was taken upright. Lying down, the airway gets worse and can lose around half of this space.","الأشعة اتاخدت والشخص واقف. بالاستلقاء المجرى بيسوء وممكن يخسر حوالي نص هالمساحة."),
 S(("About 1 mm while lying down","حوالي 1 ملم بالاستلقاء"),"So during sleep the body may be breathing through a passage of less than 1 mm.","يعني وقت النوم الجسم ممكن عم يتنفس من ممر أقل من 1 ملم."),
 S(("Imaging taken while awake","تصوير بيتاخد وأنت صاحي"),"The CT scan is taken while you are awake. Asleep, the muscles relax and the airway is usually narrower still.","الأشعة المقطعية بتتاخد وأنت صاحي. وأنت نايم العضلات بترتخي والمجرى عادةً بيضيق أكتر."),
 dict(t=("Not an ordinary X-ray","مو أشعة عادية"),img="d3_f.png",pos="50% 55%",cap=("A CT scan shows the jaw joint and the airway in 3D.","الأشعة المقطعية بتبيّن مفصل الفك والمجرى بثلاثة أبعاد.")),
 ],("Want to see your own airway?","بدك تشوف مجراك؟"),("Ask Ezza about a CT scan assessment.","اسأل عزة عن تقييم بالأشعة المقطعية.")),
car(11,"2026-10-30","blocked-nose","NOSE","P01","Why can't you breathe through your nose?","ليش ما بتتنفس من أنفك؟",[
 S(("Enlarged turbinates","قرينات متضخمة"),"The turbinates are small structures inside the nose. When they swell, the passage narrows.","القرينات تراكيب صغيرة جوا الأنف. لما بتتضخم الممر بيضيق."),
 dict(t=("Nose, sinus and mouth","الأنف والجيب والتم"),fit=True,img="coronal_nose.png",pos="50% 50%",cap=("Enlarged turbinates, inflamed sinus full of fluid: mouth breathing.","القرينات متضخمة والجيب الفكي ملتهب وممتلئ بسوائل التهابية، فالنتيجة تنفس بالفم.")),
 S(("The result: mouth breathing","النتيجة: تنفس بالفم"),"When the nose is blocked, the mouth takes over, and the tongue drops away from the palate.","لما الأنف بيسد، التم بيتولى التنفس، واللسان بينزل عن سقف الحلق."),
 S(("The link to sleep","علاقته بالنوم"),"Mouth breathing and a low tongue can make the airway narrower during sleep.","التنفس من الفم واللسان الواطي ممكن يضيّقوا المجرى بالنوم."),
 S(("A complete assessment","تقييم شامل"),"We examine the nose, airway, sinuses, jaws, tongue position, teeth and neck vertebrae together, to find what is really behind it.","منفحص الأنف والمجرى والجيوب والفكين وموضع اللسان والأسنان وفقرات الرقبة مع بعض، لنلاقي السبب الحقيقي."),
 ],("Blocked nose for months?","أنفك مسدود من شهور؟"),("Book a full assessment.","احجز تقييم شامل.")),
car(12,"2026-10-31","low-tongue-spaced-teeth","TONGUE","P06","A tongue with no room","لسان ما إله مكان",[
 S(("Where the tongue should rest","مكانه الصحيح"),"At rest, the tongue should sit against the roof of the mouth, behind the front teeth.","بالراحة، اللسان لازم يكون ملاصق لسقف الحلق، ورا الأسنان الأمامية."),
 dict(t=("Tongue away from the palate","اللسان مبتعد عن سقف الحلق"),fit=True,img="coronal_gap.png",pos="50% 50%",cap=("The dark space is air between tongue and palate: often mouth breathing.","الفراغ الغامق هو هوا بين اللسان وسقف الحلق، وغالباً معناه تنفس من الفم.")),
 dict(t=("Spaced teeth, little room","فراغات الأسنان: مساحة قليلة"),img="d3_l.png",pos="50% 62%",cap=("Gaps between teeth can mean the tongue has too little room.","الفراغات بين الأسنان ممكن تدل إنو اللسان ما عنده مساحة كافية.")),
 dict(t=("The tongue falls back","اللسان بيرجع لورا"),fit=True,img="sag_wide.png",pos="50% 50%",cap=("No room: the tongue moves back and narrows the airway.","ما في مساحة: اللسان بيرجع لورا وبيضيّق المجرى.")),
 S(("One pattern, many signs","نمط واحد وعلامات كتير"),"Gaps between teeth and a narrow space at the back of the mouth can be linked to tongue size and airway. A full assessment confirms it.","فراغات بين الأسنان وضيق خلفي ممكن يرتبطوا بحجم اللسان والمجرى. التقييم الكامل بيأكد."),
 ],("Ask Ezza about a tongue and airway assessment.","اسأل عزة عن تقييم اللسان والمجرى."),("Find the cause, not only the symptom.","ندوّر على السبب، مو على العرَض بس.")),
]
# BP/HR series parts 2-5 (provisional dates)
CARS+=[
car(27,"2026-11-20","bp-hr-peaks-2","SLEEP STUDY · 2/5","P24","Why pressure surges when breathing struggles","ليش الضغط بيرتفع لما التنفس يتعثر",[
 S(("A closing airway","مجرى بيضيق"),"When the airway narrows during sleep, the body struggles to get air in.","لما المجرى بيضيق بالنوم، الجسم بيكافح ليدخّل الهوا."),
 S(("The alarm response","استجابة الإنذار"),"The brain fires alarms and the body responds: the heart speeds up abnormally and the blood vessels constrict abnormally, to make up for the lack of oxygen across the whole body.","الدماغ بيطلق إنذارات والجسم بيستجيب: بيسرّع دقات القلب بشكل غير طبيعي وبتتقبض الأوعية الدموية بشكل غير طبيعي، حتى تعوّض نقص الأكسجين بكامل الجسم."),
 S(("Pressure jumps","الضغط بيقفز"),"Blood pressure reaches abnormal levels. Time after time, a chronic condition can develop: arterial hypertension, heart failure, or other vascular and blood diseases.","الضغط بيوصل لمستويات غير طبيعية. مرة بعد مرة ممكن تتكوّن حالة مزمنة: ارتفاع توتر شرياني، أو قصور قلب، أو أمراض وعائية ودموية تانية."),
 S(("A link, not a guarantee","ارتباط مو ضمان"),"Not everyone with a narrow airway reaches extreme values. Each case needs its own measurements.","مو كل واحد مجراه ضيق بيوصل لقيم متطرفة. كل حالة بدها قياساتها."),
 S(("Why we measure","ليش منقيس"),"A sleep study shows what actually happens at night, not only what we expect.","دراسة النوم بتبيّن شو بيصير فعلاً بالليل، مو بس شو منتوقع."),
 ],("Worried about your nights?","قلقان من لياليك؟"),("Ask about a sleep and airway assessment.","اسأل عن تقييم النوم والمجرى.")),
car(28,"2026-11-21","bp-hr-peaks-3","SLEEP STUDY · 3/5","P13","A heart at 140 beats while you sleep","قلب بـ 140 نبضة وأنت نايم",[
 S(("Resting versus working","راحة مقابل جهد"),"A sleeping heart usually slows down. At 140 beats per minute, you are lying down but doing hard exercise.","القلب النايم عادةً بيبطّئ. على 140 نبضة بالدقيقة معناه إنك راقد وعم تعمل تمارين شاقة."),
 S(("Every night, all night","كل ليلة وطول الليل"),"A heart that never gets its rest has less time to recover.","قلب ما بياخد راحته عنده وقت أقل ليتعافى."),
 S(("A load on the heart","حمل على القلب"),"A peak pressure of 258 means a heavy load on the heart in a single night. Now imagine it repeating every single day.","ضغط أعظمي 258 يعني حمل ثقيل على القلب بليلة وحدة. فكّر لو المشكلة عم تتكرر كل يوم، كل يوم."),
 S(("Do not ignore it","لا تتجاهله"),"Unexplained fast pulse or high pressure at night deserves a proper evaluation.","نبض سريع أو ضغط عالي بالليل بلا تفسير بيستاهل تقييم صحيح."),
 S(("Look for the cause","دوّر على السبب"),"Look for the cause instead of taking medication for life. If the cause is structural, there may be a chance to treat the chronic condition at its root, and for good.","دوّر على السبب ولا تستمر بالأدوية طول حياتك. إذا السبب بنيوي، ممكن تكون في فرصة تعالج المرض المزمن من جذره وبشكل دائم."),
 ],("Waking with a racing heart?","بتصحى والقلب عم يدق بسرعة؟"),("Get your breathing and jaw assessed.","قيّم تنفسك وفكك.")),
car(29,"2026-11-23","bp-hr-peaks-4","SLEEP STUDY · 4/5","P20","Normal at the clinic, abnormal at night","طبيعي بالعيادة، غير طبيعي بالليل",[
 S(("A daytime reading can mislead","قراءة النهار ممكن تضلّل"),"Blood pressure measured while awake can look acceptable even when nights are not.","ضغط مقاس وأنت صاحي ممكن يبان مقبول حتى لو لياليك مو هيك."),
 S(("Sleep should lower pressure","النوم المفروض يخفّض الضغط"),"In healthy sleep, pressure usually dips below the daytime level.","بالنوم الصحي الضغط عادةً بينزل تحت مستوى النهار."),
 S(("When it does not dip","لما ما ينزل"),"If the pressure stays high or surges at night, the heart and vessels get no break.","إذا الضغط ضل عالي أو قفز بالليل، القلب والأوعية ما بياخدوا راحة."),
 S(("Why it matters","ليش مهم"),"Night-time pressure is linked with cardiovascular risk, sometimes more than daytime readings.","ضغط الليل مرتبط بخطر القلب والأوعية، أحياناً أكتر من قراءات النهار."),
 S(("What to do","شو بتعمل"),"If you have poor sleep and high pressure, ask for a night-time assessment.","إذا نومك سيئ وضغطك عالي، اطلب تقييم ليلي."),
 ],("Good days, bad nights?","نهارك تمام ولياليك لأ؟"),("Ask Ezza about an assessment.","اسأل عزة عن تقييم.")),
car(30,"2026-11-24","bp-hr-peaks-5","SLEEP STUDY · 5/5","P14","Finding the cause behind the numbers","نلاقي السبب ورا الأرقام",[
 S(("Numbers are signals","الأرقام إشارات"),"High pressure and fast pulse at night are signals. The question is what is behind them.","ضغط عالي ونبض سريع بالليل إشارات. السؤال شو وراها."),
 S(("Jaw, tongue and airway","الفك واللسان والمجرى"),"A recessed jaw or a tongue with no room can narrow the airway behind it.","فك رجوعي أو لسان ما إله مكان ممكن يضيّق المجرى اللي وراه."),
 dict(t=("The CT scan shows it","الأشعة المقطعية بتبيّنه"),fit=True,img="sag_wide.png",pos="50% 50%",cap=("A side cut through the head: jaws, tongue, airway and spine.","مقطع جانبي بالرأس: الفكين واللسان والمجرى والعمود الفقري.")),
 S(("Treat the cause","نعالج السبب"),"When the structure is the cause, the plan targets the structure.","لما الشكل هو السبب، الخطة بتستهدف الشكل."),
 S(("Your next step","خطوتك التالية"),"If you have symptoms or abnormal readings, a full assessment is the place to start.","إذا عندك أعراض أو قراءات غير طبيعية، التقييم الكامل هو البداية."),
 ],("Numbers that worry you?","أرقام قلقتك؟"),("Book a full assessment with Ezza.","احجز تقييم شامل مع عزة.")),
]
gen3.CARS=CARS
asyncio.run(gen3.main(sys.argv[1]))
