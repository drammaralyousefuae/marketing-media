"""i18n hook: import this BEFORE a generator runs (python3 -c "import i18n; ..." / run_gen.py).
Env:
  I18N_MODE   identity | extract | ru | fa
  I18N_TR     path to translations json  {arabic_node_text: {ru:..., fa:...}}
  I18N_HANDLE footer handle (default @drammaralyousefuae)
  I18N_LOG    path of jsonl log
Only IG-size pages (height<=1400) are rendered; TikTok-size pages are skipped.
"""
import os, json, asyncio
from pathlib import Path
import playwright.async_api as pa

MODE = os.environ.get('I18N_MODE', 'identity')
HANDLE = os.environ.get('I18N_HANDLE', '@drammaralyousefuae')
LOG = os.environ.get('I18N_LOG', 'i18n_log.jsonl')
TRP = os.environ.get('I18N_TR', 'i18n_tr.json')
TR = json.load(open(TRP)) if (MODE in ('ru', 'fa') and os.path.exists(TRP)) else {}
B = Path(__file__).parent.resolve()
F = B / 'node_modules/@fontsource'

CY = f"""
@font-face{{font-family:'Cormorant';src:url('file://{F}/cormorant-garamond/files/cormorant-garamond-cyrillic-600-normal.woff2') format('woff2');font-weight:600;unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}}
@font-face{{font-family:'Cormorant';src:url('file://{F}/cormorant-garamond/files/cormorant-garamond-cyrillic-700-normal.woff2') format('woff2');font-weight:700;unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}}
@font-face{{font-family:'Cormorant';src:url('file://{F}/cormorant-garamond/files/cormorant-garamond-cyrillic-600-italic.woff2') format('woff2');font-weight:600;font-style:italic;unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}}
@font-face{{font-family:'Inter';src:url('file://{F}/inter/files/inter-cyrillic-400-normal.woff2') format('woff2');font-weight:400;unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}}
@font-face{{font-family:'Inter';src:url('file://{F}/inter/files/inter-cyrillic-500-normal.woff2') format('woff2');font-weight:500;unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}}
@font-face{{font-family:'Inter';src:url('file://{F}/inter/files/inter-cyrillic-600-normal.woff2') format('woff2');font-weight:600;unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}}
"""

STAGE1 = r"""
(cfg)=>{
 const AR=/[؀-ۿ]/;
 const body=document.body;
 const kids=[...body.children].filter(e=>!e.matches('.pat,style,script'));
 const R=e=>{const r=e.getBoundingClientRect();return [r.left,r.top,r.right,r.bottom]};
 const ov=(a,b)=>Math.min(a[2],b[2])-Math.max(a[0],b[0])>2 && Math.min(a[3],b[3])-Math.max(a[1],b[1])>2;
 const rects=kids.map(R); const base=[];
 for(let i=0;i<kids.length;i++)for(let j=i+1;j<kids.length;j++) if(ov(rects[i],rects[j])) base.push(i+','+j);
 window.__base=new Set(base); window.__kids=kids;
 const w=document.createTreeWalker(body,NodeFilter.SHOW_TEXT);
 const ar=[],en=[],nodes=[];
 while(w.nextNode()){const n=w.currentNode; const t=n.nodeValue.trim(); if(!t) continue;
   if(n.parentElement.closest('style,script')) continue;
   if(AR.test(t)){ar.push(t);nodes.push(n)} else en.push(t)}
 if(cfg.mode==='extract') return {ar,en};
 if(cfg.mode==='identity') return {ar:ar.length};
 const missing=[];
 for(const n of nodes){
   const key=n.nodeValue.trim(); const t=cfg.tr[key];
   if(!t||!t[cfg.mode]){missing.push(key);continue}
   n.nodeValue=n.nodeValue.replace(key,t[cfg.mode]);
   const el=n.parentElement; el.setAttribute('data-i18n','1');
   if(cfg.mode==='ru'){
     const st=el.getAttribute('style')||'';
     if(el.classList.contains('ar')){
       el.style.fontFamily='Cormorant'; el.style.direction='ltr'; el.style.fontWeight='700'; if(!el.style.width) el.style.fontSize=(parseFloat(getComputedStyle(el).fontSize)*1.12)+'px';
       if(!el.style.textAlign||el.style.textAlign==='right') el.style.textAlign='left';
     } else if(el.matches('.card .a')||/Cairo/.test(st)){
       el.style.fontFamily='Inter'; el.style.direction='ltr';
       if(!el.style.textAlign||el.style.textAlign==='right') el.style.textAlign='left';
     } else if(!AR.test(key.replace(/[؀-ۿ]/g,'')==='')){ }
   }
 }
 const hh=document.querySelector('.foot .h'); if(hh) hh.textContent=cfg.handle;
 return {missing};
}
"""

STAGE2 = r"""
()=>{
 const kids=window.__kids, base=window.__base;
 const R=e=>{const r=e.getBoundingClientRect();return [r.left,r.top,r.right,r.bottom]};
 const ov=(a,b)=>Math.min(a[2],b[2])-Math.max(a[0],b[0])>2 && Math.min(a[3],b[3])-Math.max(a[1],b[1])>2;
 const topOf=e=>{while(e.parentElement!==document.body)e=e.parentElement;return e};
 const tr=[...document.querySelectorAll('[data-i18n]')];
 const idx=e=>kids.indexOf(topOf(e));
 let scaled=0, it=0, bad;
 for(;it<20;it++){
   const rects=kids.map(R); bad=new Set();
   for(let i=0;i<kids.length;i++)for(let j=i+1;j<kids.length;j++){
     if(!ov(rects[i],rects[j])||base.has(i+','+j)) continue;
     for(const t of tr){const k=idx(t); if(k===i||k===j) bad.add(t)}
   }
   for(const t of tr){const r=rects[idx(t)]; if(r && (r[2]>1080-40)) bad.add(t)}
   if(!bad.size) break;
   for(const t of bad){const fs=parseFloat(getComputedStyle(t).fontSize); const orig=t.__fs||(t.__fs=fs);
     if(fs<=orig*0.62) continue; t.style.fontSize=(fs*0.95)+'px'; scaled++;}
 }
 return {scaled,iters:it,remaining:bad?bad.size:0};
}
"""

_orig_goto = pa.Page.goto
_orig_shot = pa.Page.screenshot


async def _goto(self, url, **kw):
    vp = self.viewport_size or {}
    self._skip = vp.get('height', 0) > 1400
    self._info = {}
    if self._skip:
        return None
    r = await _orig_goto(self, url, **kw)
    if MODE in ('ru', 'fa', 'extract', 'identity'):
        await self.add_style_tag(content=CY)
        res = await self.evaluate(STAGE1, dict(mode=MODE, tr=TR, handle=HANDLE))
        self._info = res or {}
        if MODE in ('ru', 'fa'):
            await self.evaluate("Promise.all([document.fonts.load('700 40px Cormorant','Привет'),document.fonts.load('400 30px Inter','Привет'),document.fonts.load('400 30px Cairo','سلام'),document.fonts.load('700 30px Amiri','سلام')]).then(()=>document.fonts.ready).then(()=>1)")
            fit = await self.evaluate(STAGE2)
            self._info.update(fit)
    return r


async def _shot(self, **kw):
    if getattr(self, '_skip', False):
        return b''
    path = kw.get('path')
    if MODE=='extract':
        with open(LOG,'a') as f: f.write(json.dumps(dict(path=str(path),**getattr(self,'_info',{})),ensure_ascii=False)+'\n')
        return b''
    rec = dict(path=str(path), mode=MODE, **getattr(self, '_info', {}))
    with open(LOG, 'a') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return await _orig_shot(self, **kw)

pa.Page.goto = _goto
pa.Page.screenshot = _shot
