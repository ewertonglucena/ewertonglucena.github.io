const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const assert=require('assert/strict');
const {chromium}=require('C:/Users/ewert/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
  const url=pathToFileURL(path.resolve(__dirname,'../index.html')).href;
  const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
  try{
    const page=await browser.newPage({locale:'pt-BR',viewport:{width:1440,height:1050},reducedMotion:'reduce'});
    await page.clock.install({time:new Date('2026-10-08T12:00:00Z')});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto(url);
    assert.equal(await page.locator('html').getAttribute('data-mode'),'identity');
    assert.equal(await page.locator('.project-card h3').first().textContent(),'Ciclo de Vida de Usuários');
    assert.equal(await page.locator('[data-skill-group]:visible').getAttribute('data-skill-group'),'identity');
    assert.equal(await page.locator('.metric [data-metric="certifications"]').textContent(),'9');
    assert.equal(await page.locator('[data-metric="projects"]').textContent(),'2');
    assert.equal(await page.locator('.brand-text i').textContent(),'curriculum vitae');
    assert.equal(await page.locator('.brand-text i').evaluate(el=>getComputedStyle(el).fontStyle),'italic');
    const computed=await page.evaluate(()=>{
      const {unionMonths,monthIndex}=window.ResumeMetrics;
      const data=JSON.parse(document.getElementById('resume-data').textContent);
      return {
        overlap:unionMonths([{start:'2020-01',end:'2021-06'},{start:'2020-06',end:'2022-01'}],'2026-10'),
        gaps:unionMonths([{start:'2020-01',end:'2020-07'},{start:'2021-01',end:'2021-07'}],'2026-10'),
        ongoing:unionMonths([{start:'2026-03',end:null}],'2026-10'),
        nextMonth:unionMonths([{start:'2026-03',end:null}],'2026-11'),
        invalid:unionMonths([{start:'2025-13',end:null},{start:'2028-01',end:null},{start:'2020-05',end:'2020-02'}],'2026-10'),
        it:unionMonths(data.jobs,'2026-10'),cyber:unionMonths(data.jobs.filter(job=>job.cybersecurity),'2026-10'),identity:unionMonths(data.jobs.filter(job=>job.identity),'2026-10'),
        invalidMonth:monthIndex('2020-13')
      };
    });
    assert.deepEqual(computed,{overlap:24,gaps:12,ongoing:7,nextMonth:8,invalid:0,it:146,cyber:52,identity:7,invalidMonth:null});
    const facts=await page.locator('.job-header').allTextContents();
    await page.locator('[data-mode="cloud-data"]').focus();
    await page.keyboard.press('Enter');
    assert.equal(await page.locator('html').getAttribute('data-mode'),'cloud-data');
    assert.equal(await page.locator('.project-card h3').first().textContent(),'Data Security Maturity');
    assert.deepEqual(await page.locator('.job-header').allTextContents(),facts,'Mode must preserve chronological jobs and dates');
    assert.equal(new URL(page.url()).searchParams.get('mode'),'cloud-data');
    await page.reload();
    assert.equal(await page.locator('html').getAttribute('data-mode'),'cloud-data');
    await page.locator('[data-mode="identity"]').click();
    await page.locator('[data-skill="data"]').click();
    assert.equal(await page.locator('[data-skill-group]:visible').getAttribute('data-skill-group'),'data');
    await page.locator('#credential-category').selectOption('professional');
    assert.equal(await page.locator('.certificate:visible').count(),9);
    assert.equal(await page.locator('.credential-category:visible').count(),1);
    await page.locator('#credential-search').fill('Fortinet');
    assert.equal(await page.locator('.certificate:visible').count(),3);
    assert.equal(await page.locator('.certificate:visible .cert-note').count(),3);
    await page.locator('[data-lang="en-US"]').click();
    assert.equal(await page.locator('#credential-category').inputValue(),'professional');
    assert.equal(await page.locator('#credential-category option:checked').textContent(),'Professional certifications');
    assert.equal(await page.locator('.project-card h3').first().textContent(),'User Lifecycle');
    assert.equal(await page.locator('.certificate:visible').count(),3);
    assert.equal(await page.locator('[data-metric="it"]').textContent(),'12 years and 2 months');
    assert.equal(await page.locator('.cert-note').filter({hasText:'Expired'}).count(),3);
    assert.equal(await page.locator('[data-skill-group="identity"] .study-note').textContent(),'Studies; no production experience reportedOktaCyberArkSailPoint');
    assert.equal(await page.locator('meta[property="og:title"]').getAttribute('content'),await page.title());
    assert.equal(await page.locator('.certificate a[href^="https://learn.microsoft.com"]').count(),4);
    const data=JSON.parse(await page.locator('#resume-data').textContent());
    const original=fs.readFileSync(path.join(__dirname,'remote-index.html'),'utf8');
    data.jobs.forEach(job=>{assert(original.includes(job.title));assert(original.includes(job.dates));job.bullets.forEach(b=>assert(original.includes(b.replaceAll('&','&amp;'))||original.includes(b)));});
    data.certificates.forEach(cert=>assert(cert.category!=='professional'||!['Clavis Academy','IAM Tech Day','Okta','Skillsoft','Udemy'].includes(cert.provider)));
    assert(!await page.locator('body').innerText().then(text=>text.includes('[PREENCHER]')));
    await page.locator('#credential-search').fill('');
    await page.locator('#credential-category').selectOption('all');
    await page.locator('[data-lang="pt-BR"]').click();
    assert.equal(await page.locator('#credential-category option:checked').textContent(),'Todas as categorias');
    for(const id of ['projects','skills','credentials']){
      await page.locator('#'+id).scrollIntoViewIfNeeded();
      await page.locator('#'+id).screenshot({path:path.join(__dirname,`modern-${id}.png`)});
    }
    await page.setViewportSize({width:390,height:844});
    await page.evaluate(()=>scrollTo(0,0));
    await page.screenshot({path:path.join(__dirname,'modern-mobile.png'),fullPage:true});
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
    const staticPage=await browser.newPage({javaScriptEnabled:false});await staticPage.goto(url);
    assert.equal(await staticPage.locator('.skill-group:visible').count(),3);
    assert.equal(await staticPage.locator('.certificate:visible').count(),27);
    assert.equal(await staticPage.locator('.project-card:visible').count(),2);
    await staticPage.close();
    assert.deepEqual(errors,[]);
    const report={status:'passed',durationCases:computed,modeSwitch:'Keyboard, direct URL, stable facts',credentials:{entries:27,professional:9,expiredFortinet:3,officialProgramLinks:4},projects:2,locales:['pt-BR','en-US'],noJavaScript:'Complete career, skills, projects and credentials',consoleErrors:0};
    fs.writeFileSync(path.join(__dirname,'verification-modernization.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));
  }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exit(1);});
