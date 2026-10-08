const path=require('path');
const {pathToFileURL}=require('url');
const assert=require('assert/strict');
const {chromium}=require('C:/Users/ewert/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
  const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
  try{
    const page=await browser.newPage({viewport:{width:700,height:572},locale:'en-US',reducedMotion:'reduce'});
    await page.goto(pathToFileURL(path.resolve(__dirname,'../CV - Ewerton Gomes de Lucena 2026 - PT-BR EN-US.html')).href);
    for(const locale of ['pt-BR','en-US']){
      await page.locator(`[data-lang="${locale}"]`).click();
      for(const width of [320,700,1440]){
        await page.setViewportSize({width,height:572});
        for(const open of [true,false]){
          await page.locator('.responsibilities').evaluateAll((elements,open)=>elements.forEach(el=>el.open=open),open);
          const labels=await page.locator('.responsibilities summary [data-i18n]').evaluateAll(elements=>elements.map(el=>{const s=getComputedStyle(el),r=el.getBoundingClientRect();return {transform:s.transform,writingMode:s.writingMode,width:r.width,height:r.height};}));
          assert.equal(labels.length,7);
          labels.forEach(label=>{assert.equal(label.transform,'none');assert.equal(label.writingMode,'horizontal-tb');assert(label.width>label.height);});
        }
      }
    }
    await page.setViewportSize({width:700,height:572});
    const summary=page.locator('.job').nth(4).locator('summary');
    await summary.scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(__dirname,'preview-horizontal-responsibilities.png')});
    console.log(JSON.stringify({status:'passed',labels:7,languages:['pt-BR','en-US'],states:['expanded','collapsed'],widths:[320,700,1440]}));
  }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exit(1);});
