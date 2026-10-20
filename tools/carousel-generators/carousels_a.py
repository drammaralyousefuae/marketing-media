# Each carousel: date, slug, tag, hero, title_en, title_ar, slides[5]=(title_en,title_ar,body_en,body_ar), cta=(en,ar), tt (tiktok title), tags
C=[]
def add(**k): C.append(k)

add(n=2,date="2026-10-20",slug="first-consultation",tag="FIRST VISIT",hero="5",
 title_en="Before your first consultation: what to bring",title_ar="قبل أول استشارة: شو بتجيب معك",
 slides=[
 ("Your previous X-rays and scans","الأشعة والسكانرات السابقة","Bring any X-ray, CBCT or MRI you already have, as digital files or on a disc. It can save you a repeat scan.","جيب أي أشعة أو سكانر أو رنين عندك، ملفات رقمية أو على قرص. ممكن يوفّر عليك إعادة التصوير."),
 ("Recent labs and doctors' reports","التحاليل الأخيرة وتقارير الأطباء","Blood tests from the last year and any reports from other doctors who have seen you.","تحاليل الدم من آخر سنة وأي تقارير من أطباء تانيين شافوك."),
 ("Medications and allergies","قائمة الأدوية والحساسية","Every medicine and supplement you take, with doses if you know them, and any allergy.","كل دوا ومكمّل بتاخده مع الجرعات إذا بتعرفها، وأي حساسية."),
 ("A sleep study, if you have one","تحليل النوم إن عملته","If you feel tired or sleep badly, bring any sleep test you did, even a home test.","إذا بتحس بتعب أو نومك سيئ، جيب أي تحليل نوم عملته حتى لو بالبيت."),
 ("Your questions and goals","أسئلتك وأهدافك","Write down what bothers you and what you hope to change, before the visit.","اكتب شو بيزعجك وشو بدك يتغيّر، قبل الزيارة."),
 ],
 cta=("Send your photos and files to Ezza before the appointment.","ابعت صورك وملفاتك لعزة قبل الموعد."),
 tt="5 things to bring to your first consultation",
 tags="#FirstConsultation #PatientTips #OralSurgery #DrAmmarAlYousef #DubaiDentist #Sharjah #UAE #استشارة #جراحة_الفم_والوجه_والفكين #دبي #الشارقة")

add(n=3,date="2026-10-21",slug="child-mouth-breathing-short",tag="CHILDREN",hero="?",
 title_en="Why does your child sleep with an open mouth?",title_ar="ليش طفلك نايم وتمه مفتوح؟",
 slides=[
 ("Broken sleep, snoring, night sweats","نوم متقطع وشخير وتعرّق بالليل","A child who breathes through the mouth often sleeps restlessly, snores and sweats at night.","الطفل اللي بيتنفس من تمه كتير ما بينام منيح، وبيشخر وبيتعرّق بالليل."),
 ("Tired and distracted at school","تعب وقلة تركيز بالمدرسة","Poor sleep is linked with daytime tiredness and trouble concentrating.","النوم السيئ مرتبط بتعب بالنهار وصعوبة بالتركيز."),
 ("Dry mouth, bad breath, cavities","جفاف وروائح وتسوس","Breathing through the mouth dries it out, which can mean bad breath and more cavities.","التنفس من الفم بيجفف التم، وهاد ممكن يعني رائحة فم وتسوس أكتر."),
 ("Repeated tonsil and nose infections","التهابات متكررة باللوزات والأنف","Blocked noses and enlarged tonsils often go together with mouth breathing.","الأنف المسدود واللوزات المتضخمة بيجوا غالباً مع التنفس من الفم."),
 ("Mood and behaviour","عصبية وفرط حركة","Irritability and restlessness are linked with poor sleep. Linked does not mean proven cause.","العصبية وفرط الحركة مرتبطة بقلة النوم. مرتبط ما بيعني سبب مؤكد."),
 ],
 cta=("Have your child checked. Early assessment is simple.","افحص طفلك. التقييم المبكر بسيط."),
 tt="Why does your child sleep with an open mouth?",
 tags="#ChildHealth #MouthBreathing #KidsSleep #Parenting #DrAmmarAlYousef #Dubai #UAE #صحة_الأطفال #التنفس_الفموي #نوم_الأطفال #دبي")

add(n=4,date="2026-10-22",slug="child-mouth-breathing-long",tag="CHILDREN",hero="10y",
 title_en="Mouth breathing in a child: what happens years later?",title_ar="التنفس من الفم عند الطفل: شو بيصير بعد سنين؟",
 slides=[
 ("A low tongue and a narrow palate","لسان واطي وسقف حلق ضيق","When the tongue does not rest on the palate, the upper jaw may not widen as it should.","لما اللسان ما بيرتاح على سقف الحلق، الفك العلوي ممكن ما يتوسّع متل ما لازم."),
 ("A long face and a set-back lower jaw","وجه طويل وفك سفلي رجعي","Long-term mouth breathing is associated with a longer face and a lower jaw that sits back.","التنفس الفموي لسنين مرتبط بوجه أطول وفك سفلي راجع لورا."),
 ("Crowded teeth, longer orthodontics","ازدحام أسنان وتقويم أطول","A narrow jaw leaves less room, so teeth crowd and braces may take longer.","الفك الضيق بيترك مساحة أقل، فالأسنان بتتزاحم والتقويم ممكن ياخد وقت أطول."),
 ("A narrow airway that grows with them","مجرى ضيق بيكبر مع الطفل","A narrow airway in childhood can stay narrow in adulthood and affect sleep.","مجرى التنفس الضيق بالطفولة ممكن يضل ضيق بالكبر وبيأثر على النوم."),
 ("Why early assessment matters","ليش التدخل المبكر مهم","A growing child responds best to early guidance. Waiting makes the options fewer.","الطفل وهو عم يكبر بيستجيب أحسن للتوجيه المبكر. الانتظار بيقلل الخيارات."),
 ],
 cta=("Book an assessment for your child with Ezza.","احجز تقييم لطفلك مع عزة."),
 tt="Mouth breathing in children: the long-term effects",
 tags="#ChildHealth #MouthBreathing #Orthodontics #AirwayHealth #DrAmmarAlYousef #Dubai #UAE #صحة_الأطفال #التنفس_الفموي #تقويم #دبي")

add(n=5,date="2026-10-23",slug="child-mouth-breathing-signs",tag="CHECKLIST",hero="5",
 title_en="Is your child a mouth breather? A quick checklist",title_ar="طفلك بيتنفس من فمه؟ قائمة فحص سريعة",
 slides=[
 ("Mouth open at rest","التم مفتوح بالراحة","Watch your child while watching TV or sleeping. Is the mouth open most of the time?","راقب طفلك وهو بيتفرج تلفزيون أو نايم. التم مفتوح أغلب الوقت؟"),
 ("Snoring and morning tiredness","شخير وتعب صباحي","Loud snoring, restless sleep and a hard time waking up are worth noting.","الشخير العالي والنوم المضطرب وصعوبة الاستيقاظ لازم ننتبه إلها."),
 ("Dark circles and a long face","هالات سودا ووجه طويل","Dark circles under the eyes and a long, narrow face can go with mouth breathing.","هالات سودا تحت العيون ووجه طويل وضيق ممكن يترافقوا مع التنفس الفموي."),
 ("Spaced or crowded teeth","أسنان متباعدة أو متزاحمة","Teeth that are crowded or spaced out may point to how the jaw and tongue are working.","الأسنان المتزاحمة أو المتباعدة ممكن تدل على شغل الفك واللسان."),
 ("A blocked nose all the time","أنف مسدود دايماً","A nose that is always blocked pushes a child to breathe through the mouth.","الأنف المسدود دايماً بيخلي الطفل يتنفس من تمه."),
 ],
 cta=("Two or more signs? See your doctor for an assessment.","علامتين أو أكتر؟ راجع الطبيب للتقييم."),
 tt="Is your child a mouth breather? Quick checklist",
 tags="#ChildHealth #MouthBreathing #ParentingTips #Checklist #DrAmmarAlYousef #Dubai #UAE #صحة_الأطفال #التنفس_الفموي #دبي")

add(n=6,date="2026-10-24",slug="slept-7-hours-still-tired",tag="SLEEP",hero="1.6",
 title_en="Slept 7 hours and still exhausted?",title_ar="نمت 7 ساعات وتعبان؟",
 slides=[
 ("The report said: no sleep apnea","التقرير قال: ما في انقطاع نفس","In a real case, the apnea index was 1.6. On paper that is normal.","بحالة حقيقية، مؤشر انقطاع النفس كان 1.6. عالورق هاد طبيعي."),
 ("But there was no deep sleep","بس ما في نوم عميق","64% of the night was spent in stage 1, the lightest sleep, with 0 minutes of deep sleep.","64% من الليل بالمرحلة الأولى، أخف نوم، و0 دقيقة نوم عميق."),
 ("The body on alarm, every night","الجسم بحالة إنذار كل ليلة","Sleep that never gets deep leaves the body without real rest.","النوم اللي ما بيوصل للعمق ما بيعطي الجسم راحة حقيقية."),
 ("Why a normal result can mislead","ليش النتيجة الطبيعية ممكن تضلّل","An apnea index counts pauses in breathing. It does not show how light the sleep was.","مؤشر الانقطاع بيعد توقفات النفس، وما بيبيّن قديش النوم كان خفيف."),
 ("The next step","الخطوة التالية","A full sleep study in a lab gives a more complete picture than a home test.","تحليل نوم كامل بالمختبر بيعطي صورة أشمل من تحليل البيت."),
 ],
 cta=("Tired despite sleeping? Talk to Ezza about an assessment.","تعبان رغم النوم؟ احكي مع عزة عن التقييم."),
 tt="Slept 7 hours and still exhausted?",
 tags="#SleepHealth #Fatigue #SleepStudy #AirwayHealth #DrAmmarAlYousef #Dubai #UAE #صحة_النوم #تعب #تحليل_النوم #دبي")

add(n=7,date="2026-10-26",slug="uars",tag="SLEEP",hero="10+",
 title_en="No sleep apnea, but your brain keeps waking up",title_ar="لا انقطاع نفس، بس دماغك بيصحى",
 slides=[
 ("What it is","شو هي","UARS: the airway is narrow but does not fully close, so the brain wakes up to keep breathing.","UARS: المجرى ضيق بس ما بيسكّر كامل، فالدماغ بيصحى ليضل يتنفس."),
 ("10 or more arousals an hour","10 صحوات أو أكتر بالساعة","In published criteria, 10 or more breathing-related arousals per hour point to UARS.","بالمعايير المنشورة، 10 صحوات أو أكتر بالساعة بسبب التنفس بتشير لـUARS."),
 ("Who it affects","مين بيصاب","It is often described in young, slim adults and in women, who rarely look like the typical apnea patient.","غالباً بيتوصف عند الشباب والنحاف والنساء، واللي ما بيشبهوا مريض الانقطاع التقليدي."),
 ("Symptoms","الأعراض","Tiredness, headaches and trouble sleeping are common.","تعب وصداع وصعوبة بالنوم أعراض شائعة."),
 ("Why it goes unnoticed for years","ليش بتضيع سنين دون جواب","A normal apnea index can hide it, so it needs a study that measures breathing effort.","مؤشر الانقطاع الطبيعي ممكن يخبّيها، فبتحتاج دراسة بتقيس مجهود التنفس."),
 ],
 cta=("Reference: Guilleminault; Stoohs 2007. A diagnosis needs a lab study.","المرجع: Guilleminault؛ Stoohs 2007. التشخيص بيحتاج دراسة بالمختبر."),
 tt="No sleep apnea, but your brain keeps waking up (UARS)",
 tags="#UARS #SleepHealth #UpperAirway #SleepStudy #DrAmmarAlYousef #Dubai #UAE #صحة_النوم #تحليل_النوم #دبي")

add(n=8,date="2026-10-27",slug="reading-sleep-study",tag="SLEEP STUDY",hero="0 min",
 title_en="Reading a sleep study: 7 hours, 0 minutes of deep sleep",title_ar="قراءة تحليل النوم: 7 ساعات وصفر نوم عميق",
 slides=[
 ("Apnea index 1.6","مؤشر الانقطاع 1.6","In this case the apnea index was 1.6, which counts as normal.","بهالحالة مؤشر الانقطاع كان 1.6، وهاد طبيعي."),
 ("64% of the night in stage 1","64% من الليل بالمرحلة الأولى","Stage 1 is the lightest sleep. The recording moved between stages 1 and 2 all night.","المرحلة الأولى أخف نوم. التسجيل بيبيّن تنقل بين المرحلة 1 و2 طول الليل."),
 ("0 minutes of deep sleep, 0 of REM","صفر دقيقة نوم عميق وصفر REM","Neither deep sleep (stage 3) nor REM sleep was recorded.","ما انسجّل لا نوم عميق (المرحلة 3) ولا نوم الأحلام REM."),
 ("What deep sleep does","شو بيعمل النوم العميق","Deep sleep is when the body repairs itself and the brain clears waste.","النوم العميق هو وقت ترميم الجسم وتنظيف الدماغ."),
 ("A screening, not a final word","فرز مو حكم نهائي","A home study screens. The pattern calls for a full study in a lab.","تحليل البيت فرز. النمط بيستدعي دراسة كاملة بالمختبر."),
 ],
 cta=("Have a sleep report you do not understand? Send it to Ezza.","عندك تقرير نوم مو فاهمه؟ ابعته لعزة."),
 tt="Reading a sleep study: 0 minutes of deep sleep",
 tags="#SleepStudy #Polysomnography #DeepSleep #SleepHealth #DrAmmarAlYousef #Dubai #UAE #تحليل_النوم #النوم_العميق #دبي")

add(n=9,date="2026-10-28",slug="bp-hr-during-sleep",tag="SLEEP STUDY",hero="258/146",
 title_en="Blood pressure and heart rate during sleep",title_ar="ضغط الدم والنبض أثناء النوم",
 slides=[
 ("Highest night reading: 258/146","أعلى قراءة بالليل: 258/146","During the recorded night, blood pressure peaked at 258/146 mmHg.","خلال الليلة المسجّلة، وصل الضغط أعلى شي 258/146."),
 ("Average: 190/111","المعدل: 190/111","The average over the night was 190/111, higher than a sleeping body should show.","المعدل طول الليل كان 190/111، أعلى من المتوقع لجسم نايم."),
 ("Heart rate: up to 140, average 103","النبض: لحد 140 والمعدل 103","The heart rate reached 140 beats per minute, with an average of 103.","وصل النبض 140 بالدقيقة، والمعدل 103."),
 ("Linked to broken sleep","مرتبط بنوم متقطع","Broken sleep is linked with higher blood pressure. This is a link, not a proven single cause.","النوم المتقطع مرتبط بضغط أعلى. هاد ارتباط، مو سبب وحيد مؤكد."),
 ("Confirm with a 24-hour monitor","نتأكد بجهاز ضغط 24 ساعة","One home night is a clue. A 24-hour blood pressure monitor confirms.","ليلة وحدة بالبيت مؤشر. جهاز ضغط لمدة 24 ساعة بيأكد."),
 ],
 cta=("High blood pressure and poor sleep? Ask for an assessment.","ضغط عالي ونوم سيئ؟ اطلب تقييم."),
 tt="Blood pressure during sleep: 258/146",
 tags="#BloodPressure #SleepHealth #HeartRate #SleepStudy #DrAmmarAlYousef #Dubai #UAE #ضغط_الدم #النوم #دبي")

add(n=10,date="2026-10-29",slug="3d-scan-airway",tag="3D SCAN",hero="3.1 mm",
 title_en="The 3D scan that showed why",title_ar="السكانر الثلاثي الأبعاد اللي بيّن السبب",
 slides=[
 ("Side view: 3.1 mm behind the tongue","منظر جانبي: 3.1 ملم ورا اللسان","In the side view, the airway behind the tongue measured only 3.1 mm.","بالمنظر الجانبي، مجرى التنفس ورا اللسان كان قياسه 3.1 ملم بس."),
 ("What 3.1 mm means","شو يعني 3.1 ملم","That is very narrow. Air has little room to pass.","هاد ضيق كتير. الهوا ما عنده مساحة يمر."),
 ("And this is the best case","وهاي أحسن حالة","The scan is taken awake and upright. Asleep, the muscles relax and the airway is usually narrower.","السكانر بيتاخد وأنت صاحي وواقف. وأنت نايم العضلات بترتخي والمجرى عادة بيضيق أكتر."),
 ("0.3 mm slices, identity removed","شرائح 0.3 ملم والهوية مزالة","The scan is read in 0.3 mm slices, and all identifying details are removed.","السكانر بينقرأ بشرائح 0.3 ملم، وكل معلومة بتدل على المريض بتنشال."),
 ("Not an ordinary X-ray","مو أشعة عادية","A CBCT shows the jaws, joints, nose and airway in 3D, in one scan.","الـCBCT بيبيّن الفكين والمفاصل والأنف والمجرى بثلاثة أبعاد بمسح واحد."),
 ],
 cta=("Want to see your own airway? Ask Ezza about a 3D scan.","بدك تشوف مجراك؟ اسأل عزة عن السكانر الثلاثي."),
 tt="The 3D scan that showed the airway was only 3.1 mm",
 tags="#CBCT #3DScan #Airway #SleepHealth #DrAmmarAlYousef #Dubai #UAE #سكانر #مجرى_الهواء #CBCT #دبي")

add(n=11,date="2026-10-30",slug="blocked-nose",tag="NOSE",hero="2",
 title_en="Why can't you breathe through your nose?",title_ar="ليش ما بتتنفس من أنفك؟",
 slides=[
 ("Enlarged turbinates","قرينات متضخمة","The turbinates are small structures inside the nose. When they swell, the passage narrows.","القرينات تراكيب صغيرة جوا الأنف. لما بتتضخم الممر بيضيق."),
 ("Seen from the front and from above","بالصور الأمامية والأفقية","On the 3D scan, both nasal passages appeared narrowed by enlarged inferior turbinates.","بالسكانر الثلاثي، الممرين الأنفيين بانوا ضيقين بسبب تضخم القرينات السفلية."),
 ("The result: breathing through the mouth","النتيجة: تنفس بالفم","When the nose is blocked, the mouth takes over, and the tongue drops from the palate.","لما الأنف بيسد، التم بيتولى التنفس، واللسان بينزل عن سقف الحلق."),
 ("The link to sleep","علاقته بالنوم","Mouth breathing and a low tongue can make the airway narrower during sleep.","التنفس من الفم واللسان الواطي ممكن يضيّقوا المجرى بالنوم."),
 ("Conservative care first","علاج محافظ أول","We start by finding the cause: allergy, nasal care and an ENT opinion, before anything else.","منبلش بمعرفة السبب: حساسية وعناية بالأنف ورأي أنف وأذن، قبل أي شي تاني."),
 ],
 cta=("Blocked nose for months? Book an assessment.","أنفك مسدود من شهور؟ احجز تقييم."),
 tt="Why can't you breathe through your nose?",
 tags="#BlockedNose #Turbinates #NasalBreathing #SleepHealth #DrAmmarAlYousef #Dubai #UAE #انسداد_الأنف #القرينات #دبي")

add(n=12,date="2026-10-31",slug="low-tongue-spaced-teeth",tag="TONGUE",hero="1",
 title_en="A tongue with no room",title_ar="لسان ما إله مكان",
 slides=[
 ("Where the tongue should rest","مكانه الصحيح","At rest, the tongue should sit against the roof of the mouth, behind the front teeth.","بالراحة، اللسان لازم يكون ملاصق لسقف الحلق، ورا الأسنان الأمامية."),
 ("A gap that shows mouth breathing","مسافة بتبيّن تنفس بالفم","When there is a gap between tongue and palate, it often means the mouth is doing the breathing.","لما في مسافة بين اللسان وسقف الحلق، غالباً التم هو اللي عم يتنفس."),
 ("Spaced teeth, little room","فراغات الأسنان: مساحة قليلة","Spaces between teeth can show the tongue has too little room inside the mouth.","الفراغات بين الأسنان ممكن تدل إنو اللسان ما عنده مساحة كافية جوا التم."),
 ("The tongue falls back","اللسان بيرجع لورا","With no room, the tongue moves back and narrows the airway behind it.","بدون مساحة، اللسان بيرجع لورا وبيضيّق المجرى اللي وراه."),
 ("One pattern, many signs","نمط واحد وعلامات كتير","One pattern can be linked to a long face, poor sleep and tiredness. A full assessment confirms it.","نمط واحد ممكن يرتبط بوجه طويل ونوم سيئ وتعب. التقييم الكامل بيأكد."),
 ],
 cta=("Ask Ezza about a tongue and airway assessment.","اسأل عزة عن تقييم اللسان والمجرى."),
 tt="Low tongue and spaced teeth: a tongue with no room",
 tags="#TonguePosture #Airway #MouthBreathing #OralHealth #DrAmmarAlYousef #Dubai #UAE #وضعية_اللسان #مجرى_الهواء #دبي")
