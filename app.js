(function(){
  "use strict";
  var C = window.DHELMEC || {};
  var WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>';

  function waUrl(msg){ return "https://wa.me/" + C.whatsapp + (msg ? "?text=" + encodeURIComponent(msg) : ""); }

  // Contacto: si no hay WhatsApp, se esconden sus botones (nunca se inventa un número)
  function initContacto(){
    var tieneWA = !!(C.whatsapp && C.whatsapp.replace(/\D/g,"").length >= 10);
    document.querySelectorAll(".solo-wa").forEach(function(el){
      if(!tieneWA){ el.hidden = true; return; }
      if(el.tagName === "A"){ el.href = waUrl("Hola DHELMEC, quiero cotizar un proyecto."); el.target = "_blank"; el.rel = "noopener"; }
      if(!el.querySelector("svg")) el.insertAdjacentHTML("afterbegin", WA);
    });
    document.querySelectorAll("[data-tel]").forEach(function(el){
      if(C.tel){ el.textContent = C.tel; if(el.tagName==="A") el.href = "tel:" + C.tel.replace(/\s/g,""); el.classList.remove("pend"); }
    });
    document.querySelectorAll("[data-email]").forEach(function(el){
      if(C.email){ el.textContent = C.email; if(el.tagName==="A") el.href = "mailto:" + C.email; el.classList.remove("pend"); }
    });
    document.querySelectorAll("[data-dir]").forEach(function(el){ if(C.direccion) el.textContent = C.direccion; });
  }

  // Video del dron: si no existe el archivo, se queda la foto (poster)
  function initVideo(){
    var v = document.querySelector(".hero video");
    if(!v || !C.video) return;
    var s = document.createElement("source"); s.src = C.video; s.type = "video/mp4";
    v.addEventListener("error", function(){ v.remove(); }, true);
    v.addEventListener("canplay", function(){ v.classList.add("listo"); });
    v.appendChild(s); v.load();
    var p = v.play(); if(p && p.catch) p.catch(function(){});
  }

  function initHeader(){
    var h = document.querySelector(".top"); if(!h) return;
    var t = false;
    function up(){ t = false; h.classList.toggle("solida", (window.scrollY||0) > 30); }
    window.addEventListener("scroll", function(){ if(!t){ t = true; requestAnimationFrame(up); } }, {passive:true});
    up();
    var b = document.querySelector(".burger");
    if(b) b.addEventListener("click", function(){ document.body.classList.toggle("menu-abierto"); });
    document.querySelectorAll(".movil a").forEach(function(a){ a.addEventListener("click", function(){ document.body.classList.remove("menu-abierto"); }); });
  }

  function initReveal(){
    var els = document.querySelectorAll("[data-rv],[data-rv-g]");
    document.querySelectorAll("[data-rv-g]").forEach(function(g){ Array.prototype.forEach.call(g.children, function(k,i){ k.style.setProperty("--i", i); }); });
    if(!("IntersectionObserver" in window)){ els.forEach(function(e){ e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function(en){ en.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } }); }, {rootMargin:"0px 0px -6% 0px", threshold:0});
    els.forEach(function(e){ io.observe(e); });
    // Respaldo: si un salto de scroll se brinca un elemento, igual se muestra
    var tk = false;
    function barrido(){ tk = false; var h = window.innerHeight; els.forEach(function(e){ if(e.classList.contains("in")) return; var r = e.getBoundingClientRect(); if(r.top < h * .94 || r.bottom < 0){ e.classList.add("in"); io.unobserve(e); } }); }
    window.addEventListener("scroll", function(){ if(!tk){ tk = true; requestAnimationFrame(barrido); } }, {passive:true});
    barrido();
  }

  function initLightbox(){
    var links = Array.prototype.slice.call(document.querySelectorAll("[data-lb]"));
    if(!links.length) return;
    var lb = document.createElement("div"); lb.className = "lb";
    lb.innerHTML = '<img alt=""><button class="ant" aria-label="Anterior">‹</button><button class="sig" aria-label="Siguiente">›</button><button class="x" aria-label="Cerrar">×</button>';
    document.body.appendChild(lb);
    var img = lb.querySelector("img"), i = 0;
    function show(n){ i = (n + links.length) % links.length; img.src = links[i].getAttribute("href"); lb.classList.add("on"); }
    links.forEach(function(a,n){ a.addEventListener("click", function(e){ e.preventDefault(); show(n); }); });
    lb.querySelector(".x").addEventListener("click", function(){ lb.classList.remove("on"); });
    lb.querySelector(".ant").addEventListener("click", function(){ show(i-1); });
    lb.querySelector(".sig").addEventListener("click", function(){ show(i+1); });
    lb.addEventListener("click", function(e){ if(e.target === lb) lb.classList.remove("on"); });
    document.addEventListener("keydown", function(e){ if(!lb.classList.contains("on")) return; if(e.key==="Escape") lb.classList.remove("on"); if(e.key==="ArrowRight") show(i+1); if(e.key==="ArrowLeft") show(i-1); });
  }

  // Formulario: arma el mensaje y lo manda por WhatsApp (o por correo si no hay WhatsApp)
  function initForm(){
    var f = document.querySelector("form.form"); if(!f) return;
    f.addEventListener("submit", function(e){
      e.preventDefault();
      var d = new FormData(f);
      var msg = "Hola DHELMEC, quiero cotizar.\n" +
        "Nombre: " + (d.get("nombre")||"") + "\n" +
        "Empresa: " + (d.get("empresa")||"") + "\n" +
        "Teléfono: " + (d.get("telefono")||"") + "\n" +
        "Proyecto: " + (d.get("mensaje")||"");
      if(C.whatsapp){ window.open(waUrl(msg), "_blank"); }
      else if(C.email){ location.href = "mailto:" + C.email + "?subject=" + encodeURIComponent("Cotización DHELMEC") + "&body=" + encodeURIComponent(msg); }
      else { alert("Falta configurar el WhatsApp o correo de DHELMEC en config.js"); }
    });
  }

  initContacto(); initVideo(); initHeader(); initReveal(); initLightbox(); initForm();
})();
