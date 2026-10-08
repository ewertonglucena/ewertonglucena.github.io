      const resumeData=JSON.parse(document.getElementById('resume-data').textContent);
      root.classList.add('enhanced');
      function monthIndex(value){
        if(typeof value!=='string'||!/^\d{4}-(0[1-9]|1[0-2])$/.test(value))return null;
        const [year,month]=value.split('-').map(Number);
        return year*12+month-1;
      }
      function currentMonth(){
        const parts=new Intl.DateTimeFormat('en-US',{timeZone:'America/Sao_Paulo',year:'numeric',month:'2-digit'}).formatToParts(new Date());
        return `${parts.find(part=>part.type==='year').value}-${parts.find(part=>part.type==='month').value}`;
      }
      function unionMonths(periods,asOf=currentMonth()){
        const now=monthIndex(asOf);
        if(now===null)return 0;
        const ranges=periods.map(period=>[monthIndex(period.start),period.end?monthIndex(period.end):now])
          .filter(([start,end])=>start!==null&&end!==null&&end>start&&start<now)
          .map(([start,end])=>[start,Math.min(end,now)]).sort((a,b)=>a[0]-b[0]);
        let total=0,lastStart=null,lastEnd=null;
        for(const [start,end] of ranges){
          if(lastStart===null){lastStart=start;lastEnd=end;}
          else if(start<=lastEnd)lastEnd=Math.max(lastEnd,end);
          else{total+=lastEnd-lastStart;lastStart=start;lastEnd=end;}
        }
        return total+(lastStart===null?0:lastEnd-lastStart);
      }
      function formatDuration(months){
        const years=Math.floor(months/12),rest=months%12;
        const result=[];
        if(years)result.push(locale==='pt-BR'?`${years} ${years===1?'ano':'anos'}`:`${years} ${years===1?'year':'years'}`);
        if(rest||!years)result.push(locale==='pt-BR'?`${rest} ${rest===1?'mês':'meses'}`:`${rest} ${rest===1?'month':'months'}`);
        return result.join(locale==='pt-BR'?' e ':' and ');
      }
      function refreshCareerMetrics(){
        const asOf=currentMonth();
        const values={it:unionMonths(resumeData.jobs,asOf),cybersecurity:unionMonths(resumeData.jobs.filter(job=>job.cybersecurity),asOf),identity:unionMonths(resumeData.jobs.filter(job=>job.identity),asOf)};
        document.querySelectorAll('[data-metric]').forEach(element=>{
          const key=element.dataset.metric;
          element.textContent=key==='certifications'?resumeData.certificates.filter(cert=>cert.category==='professional').length:key==='projects'?resumeData.projects.length:formatDuration(values[key]);
        });
        document.querySelectorAll('[data-duration]').forEach(element=>{
          element.textContent=formatDuration(unionMonths([resumeData.jobs[Number(element.dataset.duration)]],asOf));
        });
      }
      // Month-based boundary differences, merged to avoid counting overlaps twice.
      window.ResumeMetrics=Object.freeze({monthIndex,unionMonths,currentMonth});
      window.addEventListener('pageshow',refreshCareerMetrics);
      document.addEventListener('visibilitychange',()=>{if(!document.hidden)refreshCareerMetrics();});
      const skillButtons=[...document.querySelectorAll('[data-skill]')];
      function selectSkill(key){
        skillButtons.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.skill===key)));
        document.querySelectorAll('[data-skill-group]').forEach(group=>group.hidden=group.dataset.skillGroup!==key);
      }
      skillButtons.forEach(button=>button.addEventListener('click',()=>selectSkill(button.dataset.skill)));
      const projectCards=[...document.querySelectorAll('.project-card')];
      const modeButtons=[...document.querySelectorAll('[data-mode]')];
      const requestedMode=new URLSearchParams(location.search).get('mode');
      let activeMode=requestedMode==='cloud-data'?'cloud-data':'identity';
      function setMode(mode,announce=false){
        activeMode=mode==='cloud-data'?'cloud-data':'identity';
        root.dataset.mode=activeMode;
        modeButtons.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.mode===activeMode)));
        document.querySelectorAll('.job').forEach(job=>job.classList.toggle('mode-relevant',job.dataset.focus.split(' ').includes(activeMode)));
        const projectList=document.querySelector('.project-list');
        [...projectCards].sort((a,b)=>Number(b.dataset.focus===activeMode)-Number(a.dataset.focus===activeMode)).forEach(card=>projectList.append(card));
        document.querySelectorAll('.credential-category').forEach(group=>{
          const list=group.querySelector('ul');
          certificates.filter(cert=>cert.closest('.credential-category')===group)
            .sort((a,b)=>Number(b.dataset.focus===activeMode)-Number(a.dataset.focus===activeMode)).forEach(cert=>list.append(cert));
        });
        selectSkill(activeMode==='identity'?'identity':'cloud');
        document.querySelectorAll('.focus-tags li').forEach((tag,index)=>tag.classList.toggle('focus-active',index===(activeMode==='identity'?0:2)));
        if(announce)document.getElementById('mode-status').textContent=locale==='pt-BR'?`Foco selecionado: ${activeMode==='identity'?'Identity & Access Security':'Cloud & Data Security'}.`:`Selected focus: ${activeMode==='identity'?'Identity & Access Security':'Cloud & Data Security'}.`;
      }
      modeButtons.forEach(button=>button.addEventListener('click',()=>{
        setMode(button.dataset.mode,true);
        try{const url=new URL(location.href);url.searchParams.set('mode',activeMode);history.replaceState(null,'',url);}catch(_){}
      }));
      setMode(activeMode);
