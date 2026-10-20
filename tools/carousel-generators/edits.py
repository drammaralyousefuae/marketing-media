# Dr. Ammar's review edits (2026-10-15) + pose covers
POSE={2: 'P09', 3: 'P06', 4: 'P04', 5: 'P12', 6: 'P03', 7: 'P08', 8: 'P10', 9: 'P03', 10: 'P11', 11: 'P01', 12: 'P06', 13: 'X05', 14: 'P14', 15: 'P22', 16: 'P19', 17: 'P25', 18: 'P15', 19: 'P23', 20: 'P17', 21: 'P26', 22: 'P16', 23: 'P21', 24: 'P18'}
BADGE={6:'AHI 1.6',8:'0 min',9:'258/146',10:'2.3 mm',22:'85.5%'}
def apply(C):
    d={c['n']:c for c in C}
    for n,c in d.items():
        c['pose']=POSE[n]; c['badge']=BADGE.get(n)
    c=d[2]
    c['slides'][0]=("Your previous X-rays and digital readings","الأشعة والقراءات الرقمية السابقة","Bring any X-ray, CBCT, MRI or digital reading you already have, as files or on a disc. It can save you a repeat scan.","جيب أي أشعة أو CBCT أو رنين أو قراءة رقمية عندك، ملفات أو على قرص. ممكن يوفّر عليك إعادة التصوير.")
    c['slides'][3]=("Your medical history and past surgeries","تاريخك الطبي وعملياتك السابقة","Chronic conditions, any operations you had before, and how you responded to anesthesia, so we can plan safely.","الأمراض المزمنة وأي عمليات عملتها قبل، وكيف تحمّلت التخدير، لنخطط بأمان.")
    c=d[4]
    c['slides'][4]=("Why early assessment matters","ليش التدخل المبكر مهم","A growing child responds best to early guidance. Waiting leaves fewer options, and it can affect the child's health and healthy growth.","الطفل وهو عم يكبر بيستجيب أحسن للتوجيه المبكر. الانتظار بيقلل الخيارات، وممكن يأثر على صحته ونموه السليم.")
    c=d[5]
    c['slides'][2]=("Is it only a look?","هل هو مجرد شكل؟","Dark circles and a long, narrow face are not only about appearance. They can point to disturbed growth and a problem in general health.","الهالات السودا والوجه الطويل الضيق مو شكل بس. ممكن يدلوا على اضطراب بالنمو وخلل بالصحة العامة.")
    c=d[6]
    c['title_en']="Slept 8 hours and still exhausted?"; c['title_ar']="نمت 8 ساعات ولسا تعبان؟"; c['tt']="Slept 8 hours and still exhausted?"
    c['slides'][2]=("The whole body on alert","الجسم كله بحالة إنذار","Your brain stays over-awake and signals every muscle in your body to protect you from interrupted breathing and oxygen drops.","دماغك مستيقظ بشكل مفرط وعم يرسل إشارات لكل عضلات جسمك ليحميك من انقطاع الأكسجين.")
    c['slides'][3]=("Why a normal result can mislead","ليش النتيجة الطبيعية ممكن تضلّل","Your body's defenses manage to prevent breathing pauses completely, but your over-alerted brain pays the price, with a heart beating abnormally fast and muscles tensing all night.","دفاعات جسمك بتنجح بمنع انقطاع النفس بشكل تام، بس دماغك المنبّه بشكل مفرط هو اللي بيدفع الضريبة، مع قلب بيدق بسرعة غير طبيعية وعضلات بتتشنج طول الليل.")
    c['slides'][4]=("The next step","الخطوة التالية","Take a serious step to stop your health from getting worse, and contact us to find the root cause of your problem.","خذ خطوة جدية لتمنع تدهور صحتك، وتواصل معنا لنحدد السبب الأساسي لمشكلتك.")
    c=d[10]
    c['slides'][0]=("Side view: 2.3 mm behind the tongue","منظر جانبي: 2.3 ملم ورا اللسان","In the side view, the airway behind the tongue measured only 2.3 mm.","بالمنظر الجانبي، مجرى التنفس ورا اللسان كان قياسه 2.3 ملم بس.")
    c['slides'][1]=("What 2.3 mm means","شو يعني 2.3 ملم","That is extremely narrow. Air has almost no room to pass.","هاد ضيق جداً. الهوا تقريباً ما عنده مساحة يمر.")
    c['tt']="The 3D scan that showed the airway was only 2.3 mm"
    c['imgs']={1:('airway23.png','50% 66%')}
    d[11]['imgs']={2:('turbinate.png','50% 50%')}
    c=d[13]
    c['slides'][2]=("Grinding: a very heavy load","الصريف: حمل ثقيل جداً","In a PubMed study of sleep bruxism, events averaged about 22 kgf with individual peaks above 40 kgf, and some nights exceeded the person's own maximum daytime bite force (79 kgf on average). Source: J Oral Rehabil 2001, doi 10.1046/j.1365-2842.2001.00692.x","بدراسة على صريف النوم، متوسط الحدث حوالي 22 كغ قوة، وقمم فردية فوق 40 كغ، وبعض الليالي تجاوزت أقصى قوة إطباق للشخص نفسه بالنهار (متوسطها 79 كغ). المصدر: J Oral Rehabil 2001.")
    c['slides'][3]=("A chain from your jaw to your feet","سلسلة من فكك لأخمص قدميك","Some clinicians describe a connected chain of muscle, bone and body-function changes that links your jaw to the soles of your feet.","في أطباء بيوصفوا سلسلة مترابطة من الخلل بعضلات الجسم وعظامه ووظائفه بتوصل بين فكك وأسفل قدميك.")
    c['slides'][4]=("The jaw can shape your whole posture","الفك ممكن يشكّل وضعية جسمك كلها","The shape of your jaw can influence how you walk, the curve of your spine and the position of your shoulders, without you knowing. Many people spend years on physiotherapy, massage and exercises while the underlying cause stays untreated.","شكل فكك ممكن يأثر على مشيتك وعلى انحناء عمودك الفقري ووضعية أكتافك، وأنت ما بتدري. كتير ناس بيقضوا سنين بعلاج فيزيائي ومساج وتمارين، والسبب الأساسي لسا بدون علاج.")

