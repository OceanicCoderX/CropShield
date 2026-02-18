// Simple client-side i18n loader
(function(){
    const getLang = () => localStorage.getItem('lang') || 'en';
    const setLang = (l) => { localStorage.setItem('lang', l); };

    async function fetchTranslations(lang){
        const prefixes = ['assets/lang/', './assets/lang/', '../assets/lang/', '../../assets/lang/'];
        for(const p of prefixes){
            try{
                const res = await fetch(p + lang + '.json');
                if(res && res.ok){
                    const translations = await res.json();
                    return translations;
                }
            }catch(e){
                // try next prefix
            }
        }
        return null;
    }

    async function loadTranslations(lang){
        try{
            const translations = await fetchTranslations(lang);
            if(!translations) return;
            // Replace element innerHTML/text for elements marked with data-i18n
            document.querySelectorAll('[data-i18n]').forEach(el=>{
                const key = el.getAttribute('data-i18n');
                if(!key) return;
                const val = translations[key];
                if(val === undefined) return;
                // if element has children and the translation contains HTML, set innerHTML; otherwise set textContent
                try{
                    if(/<[a-z][\s\S]*>/i.test(val)) el.innerHTML = val; else el.textContent = val;
                }catch(e){ el.textContent = val; }
            });

            // Translate placeholders
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el=>{
                const key = el.getAttribute('data-i18n-placeholder');
                if(!key) return;
                const val = translations[key];
                if(val !== undefined) el.setAttribute('placeholder', val);
            });

            // Translate value attributes (for inputs/buttons)
            document.querySelectorAll('[data-i18n-value]').forEach(el=>{
                const key = el.getAttribute('data-i18n-value');
                if(!key) return;
                const val = translations[key];
                if(val !== undefined) el.value = val;
            });

            // If translations contain a title key, update document title
            if(translations.title) document.title = translations.title;
        }catch(e){
            console.warn('i18n load failed', e);
        }
    }

    // expose a global setter so inline onclick handlers can call it
    window.setLanguage = function(lang){
        setLang(lang);
        loadTranslations(lang);
    };

    document.addEventListener('DOMContentLoaded', ()=>{
        const sel = document.getElementById('langSelect');
        const lang = getLang();
        if(sel){
            sel.value = lang;
            sel.addEventListener('change', (e)=>{
                const v = e.target.value;
                setLang(v);
                loadTranslations(v);
            });
        }
        loadTranslations(lang);
    });
})();
