const fs=require('fs');
const path=require('path');
const assert=require('assert/strict');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/ewert/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

(async()=>{
  const file=path.join(path.resolve(__dirname,'..'),'CV - Ewerton Gomes de Lucena 2026 - PT-BR EN-US.html');
  const url=pathToFileURL(file).href;
  const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
  const cases=[];
  try{
    for(const [browserLocale,expected] of [['pt-BR','pt-BR'],['pt-PT','pt-BR'],['en-US','en-US'],['en-GB','en-US'],['es-ES','en-US'],['de-DE','en-US']]){
      const context=await browser.newContext({locale:browserLocale});
      const page=await context.newPage();
      await page.goto(url);
      assert.equal(await page.locator('html').getAttribute('lang'),expected);
      assert.equal(await page.locator(`[data-lang="${expected}"]`).getAttribute('aria-pressed'),'true');
      assert.equal(await page.evaluate(()=>localStorage.getItem('ewerton-resume-language-override')),null,'Automatic detection must not create a manual override');
      assert.equal(await page.locator('a[href*="canva.com"]').count(),0);
      assert(!(await page.locator('footer').textContent()).includes('Canva'));
      cases.push({browserLocale,detected:expected});
      await context.close();
    }
    const preferences=await browser.newContext({locale:'fr-FR'});
    await preferences.addInitScript(()=>Object.defineProperty(navigator,'languages',{get:()=>['fr-FR','pt-PT','en-US']}));
    const preferencePage=await preferences.newPage();
    await preferencePage.goto(url);
    assert.equal(await preferencePage.locator('html').getAttribute('lang'),'pt-BR','Use the first supported language in the preference list');
    await preferences.close();

    const context=await browser.newContext({locale:'pt-BR',reducedMotion:'reduce'});
    const page=await context.newPage();
    const errors=[];
    page.on('pageerror',error=>errors.push(error.message));
    await page.goto(url+'?lang=en-US#credentials');
    assert.equal(await page.locator('html').getAttribute('lang'),'en-US','Explicit URL wins over browser detection');
    await page.locator('[data-lang="pt-BR"]').click();
    assert.equal(new URL(page.url()).searchParams.get('lang'),'pt-BR');
    assert.equal(new URL(page.url()).hash,'#credentials');
    await page.reload();
    assert.equal(await page.locator('html').getAttribute('lang'),'pt-BR','URL must not revert a manual selection');
    await page.locator('[data-lang="en-US"]').click();
    await page.goto(url);
    assert.equal(await page.locator('html').getAttribute('lang'),'en-US','Remember manual choice over browser setting');
    await page.evaluate(()=>{
      localStorage.removeItem('ewerton-resume-language-override');
      localStorage.setItem('ewerton-resume-language','en-US');
    });
    await page.reload();
    assert.equal(await page.locator('html').getAttribute('lang'),'pt-BR','Ignore the old automatic language cache');
    await page.goto(url+'?lang=unsupported');
    assert.equal(await page.locator('html').getAttribute('lang'),'pt-BR');
    await page.evaluate(()=>{
      Object.defineProperty(navigator,'languages',{configurable:true,get:()=>['en-US']});
      window.dispatchEvent(new Event('languagechange'));
    });
    assert.equal(await page.locator('html').getAttribute('lang'),'en-US');
    await page.locator('[data-lang="pt-BR"]').click();
    await page.evaluate(()=>window.dispatchEvent(new Event('languagechange')));
    assert.equal(await page.locator('html').getAttribute('lang'),'pt-BR','Language change must respect explicit choice');
    await page.setViewportSize({width:1440,height:1050});
    await page.evaluate(()=>window.scrollTo(0,0));
    await page.screenshot({path:path.join(__dirname,'preview-auto-language.png')});
    await page.locator('footer').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(__dirname,'preview-footer.png')});
    assert.deepEqual(errors,[]);
    await context.close();

    const unavailable=await browser.newContext({locale:'pt-PT'});
    await unavailable.addInitScript(()=>{
      Object.defineProperty(window,'localStorage',{get(){throw new Error('Storage unavailable');}});
    });
    const unavailablePage=await unavailable.newPage();
    await unavailablePage.goto(url);
    assert.equal(await unavailablePage.locator('html').getAttribute('lang'),'pt-BR');
    await unavailablePage.locator('[data-lang="en-US"]').click();
    assert.equal(await unavailablePage.locator('html').getAttribute('lang'),'en-US');
    await unavailable.close();

    const report={checks:'passed',cases,preferenceList:'First supported browser language',manualChoice:'Saved and respected',explicitLink:'Respected; updated by manual switch without losing anchor',legacyCache:'Ignored',blockedStorage:'Supported',browserLanguageChange:'Supported when no override',canvaLink:'Removed',consoleErrors:0};
    fs.writeFileSync(path.join(__dirname,'verification-language-detection.json'),JSON.stringify(report,null,2));
    console.log(JSON.stringify(report));
  }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exit(1);});
