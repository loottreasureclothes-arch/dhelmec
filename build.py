#!/usr/bin/env python3
"""Genera las 5 páginas de DHELMEC con cabecera y pie compartidos. Correr: python3 build.py"""
import os, glob
HERE = os.path.dirname(os.path.abspath(__file__))

PAGINAS = [("index.html","Inicio"),("servicios.html","Servicios"),("conocenos.html","Conócenos"),("nosotros.html","Nosotros"),("contacto.html","Contacto")]

def shell(archivo, titulo, desc, cuerpo):
    nav = "".join(f'<a href="{a}" class="{"act" if a==archivo else ""}">{t}</a>' for a,t in PAGINAS)
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<meta property="og:title" content="{titulo}"><meta property="og:description" content="{desc}"><meta property="og:image" content="img/dhelmec-8387.jpg">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a href="index.html" class="logo" aria-label="DHELMEC inicio"><img src="img/logo.png" alt="DHELMEC"></a>
    <nav class="nav">{nav}<a href="contacto.html" class="btn">Cotizar</a></nav>
    <button class="burger" aria-label="Menú"><i></i><i></i><i></i></button>
  </div>
</header>
<nav class="movil">{nav}<a href="contacto.html" class="btn">Cotizar proyecto</a><a class="btn wa solo-wa" href="#">WhatsApp</a></nav>
<main>
{cuerpo}
</main>
<footer>
  <div class="wrap">
    <div class="cols">
      <div><img src="img/logo.png" alt="DHELMEC"><p>Desarrollos Hidrocálidos Electromecánicos S.A. de C.V. Instalaciones electromecánicas, fabricación metálica, ductos, tuberías y maniobras para la industria. Aguascalientes, México.</p></div>
      <div><h4>Menú</h4><nav>{nav}</nav></div>
      <div><h4>Contacto</h4><p data-dir>Circe, Las Hadas, 20140 Aguascalientes, Ags.</p><p>Tel: <a class="pend" data-tel href="#">por confirmar</a></p><p>Correo: <a class="pend" data-email href="#">por confirmar</a></p></div>
    </div>
    <div class="abajo"><span>© 2026 DHELMEC · Desarrollos Hidrocálidos Electromecánicos S.A. de C.V.</span><a href="#top">Volver arriba ↑</a></div>
  </div>
</footer>
<a class="flota solo-wa" href="#" aria-label="WhatsApp"></a>
<script src="config.js"></script>
<script src="app.js"></script>
</body>
</html>'''

SERVICIOS = [
 ("instalaciones","img/dhelmec-8382.jpg","Instalaciones electromecánicas","Eléctricas y mecánicas en planta","Ejecución y adecuación de instalaciones eléctricas y mecánicas para líneas, equipos y áreas de producción. Tableros, alimentaciones, canalizaciones y puesta en marcha."),
 ("ductos","img/dhelmec-8377.jpg","Ductos","Acero inoxidable, negro y galvanizado","Fabricación e instalación de ductería a la medida: extracción, ventilación, aire y procesos. Espiral, rectangular y piezas especiales según cada proyecto."),
 ("paileria","img/dhelmec-8356.jpg","Pailería y estructuras","Fabricación metálica ligera y media","Bases, soportes, plataformas, protecciones, racks y estructuras metálicas para dentro de planta. Diseñadas para cargar lo que tu proceso necesita."),
 ("soldadura","img/dhelmec-8389.jpg","Soldadura e inoxidable","Fabricación, unión y adecuaciones","Soldadura para mantenimiento, montaje y fabricación de componentes metálicos, incluyendo piezas en acero inoxidable para alimentos y procesos."),
 ("tuberias","img/dhelmec-8370.jpg","Tuberías de proceso","Fabricación, montaje y adecuación","Spools, tramos bridados y modificaciones de tubería para servicios industriales: agua, aire, vapor y procesos, adaptados a la operación del cliente."),
 ("maquinaria","img/dhelmec-8360.jpg","Movimiento de maquinaria","Descarga, maniobra y colocación","Bajamos, movemos y colocamos equipos y maquinaria con montacargas y maniobras controladas, hasta dejarlos en el punto exacto dentro de la planta."),
]

def tarjetas():
    out = []
    for i,(id_,img,t,sub,_) in enumerate(SERVICIOS,1):
        out.append(f'<a class="tarj" href="servicios.html#{id_}"><img src="{img}" alt="{t}" loading="lazy"><span class="num">0{i}</span><div class="pie"><b>{t}</b><span>{sub}</span></div></a>')
    return "".join(out)

GAL_HOME = ["8366","8372","8389","8369","8378","8386","8375","8359"]
def collage():
    out=[]
    for i,n in enumerate(GAL_HOME):
        out.append(f'<a href="img/g-{n}.jpg" data-lb class="{"g" if i==0 else ""}"><img src="img/g-{n}.jpg" alt="Trabajo DHELMEC" loading="lazy"></a>')
    return "".join(out)

CONTACTO_BLOQUE = '''
<section id="cotizar" class="band">
  <div class="wrap">
    <div class="contacto">
      <form class="form" data-rv>
        <h3>Cotiza tu proyecto</h3>
        <p>Dinos qué necesitas fabricar, instalar o mover. Te contestamos directo.</p>
        <div class="fila">
          <div><label for="nombre">Nombre *</label><input id="nombre" name="nombre" required placeholder="Tu nombre"></div>
          <div><label for="empresa">Empresa o planta</label><input id="empresa" name="empresa" placeholder="Nombre de la empresa"></div>
        </div>
        <label for="telefono">Teléfono o WhatsApp *</label><input id="telefono" name="telefono" type="tel" required placeholder="449 000 0000">
        <label for="mensaje">¿Qué necesitas? *</label><textarea id="mensaje" name="mensaje" required placeholder="Ej. 40 m de ducto galvanizado de 12 pulgadas con instalación"></textarea>
        <button class="btn lleno" type="submit">Enviar solicitud</button>
        <small>Sin compromiso. Un técnico de DHELMEC te responde para visitar o cotizar.</small>
      </form>
      <div data-rv>
        <p class="ojo">Contacto directo</p>
        <h2>Hablemos de <em>tu planta.</em></h2>
        <div class="lista-c" style="margin-top:26px">
          <div><b>Taller y oficina</b><span data-dir>Circe, Las Hadas, 20140 Aguascalientes, Ags.</span></div>
          <div><b>Teléfono</b><a class="pend" data-tel href="#">por confirmar</a></div>
          <div><b>Correo</b><a class="pend" data-email href="#">por confirmar</a></div>
          <div><b>Horario</b><span>Lunes a viernes · Atención en planta y en taller</span></div>
        </div>
        <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:26px"><a class="btn wa solo-wa" href="#">Escribir por WhatsApp</a><a class="btn amarillo" target="_blank" rel="noopener" href="https://maps.google.com/?q=Circe%2C+Las+Hadas%2C+20140+Aguascalientes%2C+Ags.">Ver en el mapa</a></div>
      </div>
    </div>
  </div>
</section>'''

# ---------- INICIO ----------
index = f'''
<section class="hero" id="top">
  <div class="fondo"><img src="img/dhelmec-8387.jpg" alt="Taller DHELMEC" fetchpriority="high"><video muted loop playsinline autoplay aria-hidden="true"></video></div>
  <img class="rayo" src="img/rayo.svg" alt="" aria-hidden="true">
  <div class="wrap">
    <p class="ojo enter">Aguascalientes · Industria</p>
    <h1 class="enter d1">Fabricamos e instalamos <em>lo que tu planta necesita.</em></h1>
    <p class="lead enter d2">Instalaciones electromecánicas, ductos, pailería, tuberías de proceso y movimiento de maquinaria. Un solo equipo de principio a fin.</p>
    <div class="acciones enter d3"><a class="btn lleno" href="#cotizar">Cotizar proyecto</a><a class="btn wa solo-wa" href="#">WhatsApp</a><a class="btn" href="servicios.html">Ver servicios</a></div>
    <div class="marcas enter d3"><span>Instalaciones</span><span>Fabricación</span><span>Montaje</span><span>Maniobras</span></div>
  </div>
</section>

<section id="servicios">
  <div class="wrap">
    <div class="cab" data-rv><div><p class="ojo">Servicios</p><h2>Seis áreas, <em>un solo proveedor.</em></h2></div><p>Del tablero eléctrico a la estructura y la maniobra final. Todo sale de nuestro taller en Aguascalientes.</p></div>
    <div class="serv" data-rv-g>{tarjetas()}</div>
  </div>
</section>

<section class="band" id="trabajos">
  <div class="wrap">
    <div class="cab" data-rv><div><p class="ojo">Lo que hemos fabricado</p><h2>Hecho en <em>nuestro taller.</em></h2></div><p>Fotos reales del taller y de las piezas: estructuras, bridas, ductos, inoxidable y equipo propio.</p></div>
    <div class="col" data-rv-g>{collage()}</div>
    <div class="todas"><a class="btn" href="conocenos.html">Ver todas las fotos</a></div>
  </div>
</section>

<section id="nosotros">
  <div class="wrap">
    <div class="dos">
      <div class="foto-marco" data-rv><img src="img/dhelmec-8366.jpg" alt="Taladro radial en el taller de DHELMEC" loading="lazy"><span>Taller DHELMEC · Las Hadas, Ags.</span></div>
      <div data-rv>
        <p class="ojo">Quién es DHELMEC</p>
        <h2>Soluciones que <em>funcionan en planta.</em></h2>
        <p class="lead" style="margin-top:16px">Desarrollos Hidrocálidos Electromecánicos S.A. de C.V. atiende proyectos de instalación, fabricación metálica y maniobras industriales desde Aguascalientes. Taller propio con cizallas, dobladoras, taladro radial y equipo de soldadura.</p>
        <div class="datos"><div><b>Ags.</b><small>Taller propio en Las Hadas</small></div><div><b>6</b><small>áreas de servicio</small></div><div><b>1</b><small>equipo de principio a fin</small></div></div>
        <div style="margin-top:28px"><a class="btn" href="nosotros.html">Conoce más</a></div>
      </div>
    </div>
  </div>
</section>

<section class="band-rojo" id="proceso">
  <div class="wrap">
    <div class="cab" data-rv><div><p class="ojo">De principio a fin</p><h2>Así trabajamos <em>tu proyecto.</em></h2></div></div>
    <div class="pasos" data-rv-g>
      <div><b>Analizamos</b><p>Visitamos la planta, medimos y entendemos el proceso y la necesidad real.</p></div>
      <div><b>Fabricamos</b><p>Ductos, estructuras, tubería y adecuaciones se hacen en nuestro taller.</p></div>
      <div><b>Instalamos</b><p>Montaje, maniobra y colocación final en el punto exacto, sin detener tu operación.</p></div>
    </div>
  </div>
</section>
{CONTACTO_BLOQUE}
'''

# ---------- SERVICIOS ----------
filas=[]
for i,(id_,img,t,sub,txt) in enumerate(SERVICIOS):
    filas.append(f'''<div class="fila-s {"inv" if i%2 else ""}" id="{id_}" data-rv><img src="{img}" alt="{t}" loading="lazy"><div class="texto"><h4>Servicio 0{i+1}</h4><h3>{t}</h3><h4>{sub}</h4><p>{txt}</p><a class="btn" href="contacto.html">Solicitar cotización</a></div></div>''')
servicios = f'''
<section class="sub" id="top"><img class="fondo" src="img/dhelmec-8372.jpg" alt=""><div class="wrap"><p class="ojo enter">Servicios</p><h1 class="enter d1">Lo que hacemos, <em>área por área.</em></h1><p class="lead enter d2">Fabricación, instalación y maniobra para las necesidades reales de cada proyecto industrial.</p></div></section>
<section><div class="wrap">{"".join(filas)}</div></section>
{CONTACTO_BLOQUE}
'''

# ---------- NOSOTROS ----------
nosotros = f'''
<section class="sub" id="top"><img class="fondo" src="img/dhelmec-8360.jpg" alt=""><div class="wrap"><p class="ojo enter">Nosotros</p><h1 class="enter d1">Soluciones industriales <em>hechas a la medida.</em></h1><p class="lead enter d2">Desarrollos Hidrocálidos Electromecánicos S.A. de C.V. es una empresa de Aguascalientes dedicada a instalaciones electromecánicas, fabricación metálica y servicios para la industria.</p></div></section>
<section><div class="wrap"><div class="dos">
  <div data-rv><p class="ojo">Quiénes somos</p><h2>Trabajo técnico. <em>Soluciones reales.</em></h2><p class="lead" style="margin-top:16px">Atendemos proyectos eléctricos, mecánicos, hidráulicos y metalmecánicos de acuerdo con las condiciones y necesidades operativas de cada cliente. Contamos con taller propio equipado con cizalla hidráulica, dobladoras, taladro radial, roladora y equipo de soldadura.</p>
  <div class="datos"><div><b>Taller</b><small>propio en Las Hadas</small></div><div><b>Campo</b><small>instalación en planta</small></div><div><b>Ags.</b><small>y región</small></div></div></div>
  <div class="foto-marco" data-rv><img src="img/dhelmec-8378.jpg" alt="Dobladora en el taller de DHELMEC" loading="lazy"><span>Dobladora · taller DHELMEC</span></div>
</div></div></section>
<section class="band"><div class="wrap"><div class="mv" data-rv-g>
  <article><span>01</span><h3>Misión</h3><p>Brindar soluciones electromecánicas y de fabricación metálica que respondan de manera funcional a las necesidades de cada proyecto industrial.</p></article>
  <article><span>02</span><h3>Visión</h3><p>Consolidarnos como una empresa confiable en soluciones industriales, reconocida por la calidad del trabajo y la atención directa a cada proyecto.</p></article>
</div></div></section>
<section><div class="wrap"><div class="cab" data-rv><div><p class="ojo">Lo que nos guía</p><h2>Nuestros <em>valores.</em></h2></div></div>
<div class="val" data-rv-g>
  <div><b>Responsabilidad</b><p>Compromiso con cada trabajo y con las necesidades del cliente.</p></div>
  <div><b>Calidad</b><p>Cuidado en la fabricación, instalación y terminación de cada proyecto.</p></div>
  <div><b>Seguridad</b><p>Atención a las condiciones de trabajo y al manejo correcto de equipos.</p></div>
  <div><b>Trabajo en equipo</b><p>Coordinación entre personal técnico, ingenieros y cliente.</p></div>
</div></div></section>
{CONTACTO_BLOQUE}
'''

# ---------- CONÓCENOS (galería completa) ----------
ORDEN = "8387 8366 8370 8377 8389 8360 8382 8372 8356 8378 8369 8375 8386 8359 8362 8364 8368 8371 8373 8374 8376 8379 8380 8383 8384 8385 8388 8355 8357 8358 8361 8363 8365 8367 8381".split()
_todas = {os.path.basename(f) for f in glob.glob(os.path.join(HERE,"img","g-*.jpg"))}
fotos = [f"g-{n}.jpg" for n in ORDEN if f"g-{n}.jpg" in _todas] + sorted(f for f in _todas if f[2:6] not in ORDEN)
grid = "".join(f'<a href="img/{f}" data-lb><img src="img/{f}" alt="Taller DHELMEC" loading="lazy"></a>' for f in fotos)
conocenos = f'''
<section class="sub" id="top"><img class="fondo" src="img/dhelmec-8356.jpg" alt=""><div class="wrap"><p class="ojo enter">Conócenos</p><h1 class="enter d1">Nuestro taller, <em>pieza por pieza.</em></h1><p class="lead enter d2">{len(fotos)} fotos reales del taller de DHELMEC: equipo, estructuras, ductos, bridas e inoxidable.</p></div></section>
<section><div class="wrap"><div class="grid-g" data-rv-g>{grid}</div></div></section>
<section class="band"><div class="wrap">
  <div class="cab" data-rv><div><p class="ojo">Todo listo para completar</p><h2>Lo que falta <em>de DHELMEC.</em></h2></div><p>La página ya funciona. Estos datos se agregan en cuanto el taller los mande.</p></div>
  <div class="falta" data-rv-g>
    <div><i></i><div><b>WhatsApp y teléfono</b><span>Con el número, todos los botones verdes y el formulario mandan directo al taller.</span></div></div>
    <div><i></i><div><b>Correo oficial</b><span>Para el pie de página y el formulario.</span></div></div>
    <div><i></i><div><b>Video del dron</b><span>Va de fondo en la portada mostrando todas las instalaciones.</span></div></div>
    <div><i></i><div><b>Proyectos con nombre</b><span>Foto, cliente o planta y qué se hizo, para la sección de obras.</span></div></div>
    <div><i></i><div><b>Logos de clientes</b><span>Empresas e industrias con las que han trabajado.</span></div></div>
    <div><i></i><div><b>Equipo</b><span>Foto, nombre y puesto de los responsables.</span></div></div>
  </div>
</div></section>
{CONTACTO_BLOQUE}
'''

# ---------- CONTACTO ----------
contacto = f'''
<section class="sub" id="top"><img class="fondo" src="img/dhelmec-8382.jpg" alt=""><div class="wrap"><p class="ojo enter">Contacto</p><h1 class="enter d1">Hablemos de <em>tu proyecto.</em></h1><p class="lead enter d2">Cuéntanos qué necesitas fabricar, instalar, adecuar o mover. Estamos en Aguascalientes.</p></div></section>
{CONTACTO_BLOQUE.replace('<section id="cotizar" class="band">','<section id="cotizar">')}
<section class="band" style="padding-top:0"><div class="wrap" data-rv><iframe class="mapa" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa DHELMEC" src="https://maps.google.com/maps?q=Circe%2C+Las+Hadas%2C+20140+Aguascalientes%2C+Ags.&z=15&output=embed"></iframe></div></section>
'''

paginas = {
 "index.html": ("DHELMEC · Fabricación metálica e instalaciones electromecánicas en Aguascalientes","Instalaciones electromecánicas, ductos, pailería, tuberías de proceso y movimiento de maquinaria. Taller propio en Aguascalientes.", index),
 "servicios.html": ("Servicios | DHELMEC","Instalaciones electromecánicas, ductos, pailería, soldadura, tuberías de proceso y movimiento de maquinaria.", servicios),
 "nosotros.html": ("Nosotros | DHELMEC","Quiénes somos, misión, visión y valores de Desarrollos Hidrocálidos Electromecánicos.", nosotros),
 "conocenos.html": ("Conócenos | DHELMEC","Galería del taller de DHELMEC en Aguascalientes.", conocenos),
 "contacto.html": ("Contacto | DHELMEC","Cotiza tu proyecto industrial con DHELMEC en Aguascalientes.", contacto),
}
for archivo,(t,d,cuerpo) in paginas.items():
    with open(os.path.join(HERE,archivo),"w",encoding="utf-8") as fh: fh.write(shell(archivo,t,d,cuerpo))
    print("ok", archivo)
