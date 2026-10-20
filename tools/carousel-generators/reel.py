import sys, asyncio, subprocess, glob
sys.path.insert(0,'.')
from pathlib import Path
from genlib import page, A, B
from playwright.async_api import async_playwright
V=glob.glob('/root/.claude/uploads/b2e37f4f-88e4-5ce4-8092-8fa4da7ad0c1/*.mp4')[0]
R=[dict(slug="gaps-not-cosmetic",date="2026-11-18",ss=0,dur=10,tag="TEETH GAPS",
  te="Gaps between your teeth are not always cosmetic",ta="فراغات الأسنان مو دايماً مشكلة تجميلية",
  be="Gaps plus tiredness or poor focus? Comment WHATSAPP and we send you the link.",ba="فراغات مع تعب أو ضعف تركيز؟ علّق «واتساب» وبنبعتلك الرابط."),
 dict(slug="recession-hidden-cause",date="2026-11-19",ss=38.5,dur=14.5,tag="BONE & GUM RECESSION",
  te="Bone and gum recession: bacteria, or something bigger?",ta="انحسار العظم واللثة: جراثيم ولا سبب أكبر؟",
  be="Find the cause, not only the symptom. Comment WHATSAPP for the link.",ba="ندوّر على السبب مو العرَض. علّق «واتساب» وبنبعتلك الرابط.")]
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        for r in R:
            body=f"""<div style="position:absolute;left:72px;top:210px"><span class=tag>{r['tag']}</span></div>
<h2 style="position:absolute;left:72px;top:290px;width:936px;font-size:66px">{r['te']}</h2>
<div class=ar style="position:absolute;left:72px;right:72px;top:445px;font-size:44px">{r['ta']}</div>
<div class=fr style="left:70px;top:560px;width:940px;height:945px"></div>
<div style="position:absolute;left:72px;right:72px;top:1535px;text-align:center;font-size:32px;line-height:1.45;color:#2B2229">{r['be']}<br><span style="font-family:Cairo;direction:rtl;display:block;font-size:29px;color:#5A4E57;margin-top:6px">{r['ba']}</span></div>
<div style="position:absolute;left:190px;top:1688px"><div class=btn style="font-size:33px;padding:24px 0">Book with Ezza on WhatsApp</div></div>"""
            f=B/'tmp_reel.html'; f.write_text(page(1920,body,1,1).replace('01 / 01','')) 
            pg=await br.new_page(viewport={'width':1080,'height':1920}); await pg.goto('file://'+str(f)); await pg.wait_for_timeout(300)
            d=Path('/home/claude/marketing-media/posts')/f"{r['date']}-{r['slug']}-reel"/'v1'; d.mkdir(parents=True,exist_ok=True)
            bg=B/f"reelbg_{r['slug']}.png"; await pg.screenshot(path=str(bg)); await pg.close()
            out=d/f"{r['date']}-{r['slug']}-reel.mp4"
            subprocess.run(["ffmpeg","-y","-v","error","-loop","1","-framerate","30","-i",str(bg),"-ss",str(r['ss']),"-t",str(r["dur"]),"-i",V,"-filter_complex","[1:v]scale=936:941[v];[0:v][v]overlay=72:562:shortest=1","-an","-c:v","libx264","-crf","19","-pix_fmt","yuv420p","-r","30","-movflags","+faststart",str(out)],check=True)
            subprocess.run(["ffmpeg","-y","-v","error","-ss","6","-i",str(out),"-frames:v","1",str(B/f"reelchk_{r['slug']}.jpg")],check=True)
            print(out, out.stat().st_size)
        await br.close()
asyncio.run(main())
