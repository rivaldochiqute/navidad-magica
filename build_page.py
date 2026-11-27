"""Genera index.html (página de ventas) a partir de head/tail existentes."""
CK = 'https://mentora.ao/produto/20c544c8-2d06-4535-a9c5-ae4f6f6d821f'
head = open('parts/head.html').read()
tail = open('parts/tail.html').read()

RED, DRED, GREEN, GOLD, CREAM, INK = '#A50E1E', '#6E0914', '#0B3B2A', '#D4A53A', '#FFF8EC', '#1A1A1A'
H2 = 'margin: 0; font-size: clamp(23px, 6.4vw, 30px); line-height: 1.12; text-wrap: balance; text-align: center'
PAD = 'padding: 36px clamp(14px, 4.6vw, 22px)'


def btn(label, href=CK):
    return (f'<a class="buy" href="{href}" style="background: #12A150; color: #FFFFFF; text-decoration: none; text-align: center; font-weight: 800; '
            f'font-size: clamp(17px, 4.9vw, 21px); line-height: 1.2; padding: 20px 16px; border-radius: 14px; box-shadow: 0 6px 0 #0A5C2C">{label}&nbsp;→</a>')


def check(t, color=GOLD, ink=RED, size='clamp(17px, 4.8vw, 20px)'):
    return (f'<li style="display: flex; gap: 10px; align-items: flex-start"><span aria-hidden="true" style="flex: 0 0 26px; height: 26px; border-radius: 50%; '
            f'background: {color}; color: {ink}; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 800; margin-top: 1px">✓</span><span>{t}</span></li>')


ADVENT = ('<div class="kimg" style="flex: 0 0 104px; height: 104px; background: #A50E1E; border-radius: 12px; display: flex; align-items: center; justify-content: center">'
          '<svg width="80" height="70" viewBox="0 0 80 70" aria-hidden="true"><path d="M4 34 L18 20 L32 34 Z" fill="#FFFFFF"></path><rect x="7" y="34" width="22" height="22" fill="#D4A53A"></rect>'
          '<path d="M26 30 L40 14 L54 30 Z" fill="#FFFFFF"></path><rect x="29" y="30" width="22" height="30" fill="#2E7D4F"></rect><path d="M48 34 L62 20 L76 34 Z" fill="#FFFFFF"></path>'
          '<rect x="51" y="34" width="22" height="22" fill="#D4A53A"></rect><text x="18" y="50" text-anchor="middle" font-family="Inter, sans-serif" font-weight="800" font-size="11" fill="#A50E1E">1</text>'
          '<text x="40" y="50" text-anchor="middle" font-family="Inter, sans-serif" font-weight="800" font-size="11" fill="#FFFFFF">12</text>'
          '<text x="62" y="50" text-anchor="middle" font-family="Inter, sans-serif" font-weight="800" font-size="11" fill="#A50E1E">24</text></svg></div>')


def img(src, alt):
    return f'<img src="{src}" alt="{alt}" class="kimg" style="flex: 0 0 104px; width: 104px; height: 104px; object-fit: cover; border-radius: 12px; display: block">'


KITS = [
    (img('kit2.webp', 'Carta de Papá Noel y certificado'), 'Carta personalizada de Papá Noel',
     'Escribe el nombre de tu hijo directo en el PDF y luego imprime. Prepárate para ver su cara cuando la abra.',
     '3 cartas · 2 certificados · sobre del Polo Norte · boletos mágicos'),
    (img('familia.webp', 'Personajes navideños con las caras de la familia'), 'Personajes con la cara de tu familia',
     'Papá, mamá, los niños y hasta los abuelos convertidos en Papá Noel, duendes y renos.',
     '10 personajes en 2 tamaños + versiones para colorear'),
    (ADVENT, 'Calendario de adviento',
     'Una sorpresa cada día para vivir juntos la cuenta regresiva hasta Nochebuena.',
     '24 casitas a color + 24 para colorear + 24 ideas en familia'),
    (img('deco.webp', 'Decoración navideña de papel'), 'Decoración navideña',
     'Banderines, adornos, copos y carteles para transformar tu casa en una tarde.',
     '+100 piezas · abecedario para escribir nombres'),
    (img('kit1.webp', 'Cajitas navideñas con dulces'), 'Detalles para regalar',
     'Cajitas, sobres, etiquetas y tarjetas para profes, abuelos y amigos.',
     '+250 detalles · 105 etiquetas · 48 toppers'),
    (img('actividades.webp', 'Actividades navideñas para niños'), 'Actividades para niños',
     'Para colorear, recortar y jugar lejos de las pantallas durante las vacaciones.',
     '+70 actividades · laberintos · sopas de letras · memorama'),
]


def kit_card(n, media, title, desc, chip):
    return (f'<div style="background: {CREAM}; border-radius: 16px; padding: 14px; display: flex; gap: 14px; align-items: center; border: 3px solid {GOLD}">{media}'
            f'<div style="display: flex; flex-direction: column; gap: 5px; min-width: 0">'
            f'<h3 style="margin: 0; font-size: clamp(19px, 5.4vw, 22px); line-height: 1.12; color: {RED}">{title}</h3>'
            f'<p style="margin: 0; font-size: 15px; line-height: 1.4; color: #3A2E2A">{desc}</p>'
            f'<span style="align-self: flex-start; background: {GREEN}; color: #FFE08A; font-size: 12.5px; font-weight: 800; padding: 4px 9px; border-radius: 999px; line-height: 1.3">{chip}</span>'
            f'</div></div>')


STACK = [('+250 detalles para regalar', 27), ('Carta y certificado de Papá Noel', 12), ('Personajes con la cara de tu familia', 15),
         ('Calendario de adviento de 24 días', 12), ('+100 piezas de decoración', 12), ('+70 actividades para niños', 9), ('BONO: guía para vender tus detalles', 10)]

FAQ = [
    ('¿Cómo recibo el material?', 'Al instante, en tu correo electrónico, apenas se confirme el pago. Son más de 500 imprimibles en PDF, organizados en 6 kits + un bono.'),
    ('¿Necesito una impresora especial?', 'No. Funciona con cualquier impresora de casa, o puedes imprimir en una papelería. Viene en tamaño Carta y A4.'),
    ('¿Cómo pongo el nombre de mi hijo y la cara de mi familia?', 'El nombre lo escribes directamente en el PDF de la carta y el certificado (en la computadora o el celular, con Adobe Acrobat Reader gratis) y luego imprimes. Para los personajes, imprimes una foto de cada uno, la recortas en círculo y la pegas en el espacio marcado.'),
    ('¿Puedo imprimir más de una vez?', 'Sí, todas las veces que quieras, para usar este año y los siguientes.'),
    ('¿Puedo vender lo que armo?', 'Sí. Puedes vender las piezas impresas y armadas, y el bono te enseña cómo. Lo que no se permite es revender o compartir los archivos.'),
    ('¿Es seguro comprar?', 'Sí. El pago se procesa por Mentora, 100% seguro, y tienes 7 días de garantía.'),
]


def faq_item(i, q, a):
    open_ = i == 0
    return (f'<div style="background: #FFFFFF; border-radius: 12px; overflow: hidden">'
            f'<button type="button" class="faq-q" aria-expanded="{"true" if open_ else "false"}" style="width: 100%; min-height: 54px; background: #FFFFFF; border: 0; padding: 15px 16px; text-align: left; font: 800 16px Inter, sans-serif; color: {INK}; cursor: pointer; display: flex; justify-content: space-between; gap: 12px; align-items: center">'
            f'<span>{q}</span><span aria-hidden="true" style="font-size: 22px; color: {RED}">{"−" if open_ else "+"}</span></button>'
            f'<p class="faq-a"{"" if open_ else " hidden"} style="margin: 0; padding: 0 16px 15px; font-size: 15px; line-height: 1.5; color: #4A4236">{a}</p></div>')


GARLAND = ('<svg viewBox="0 0 520 60" style="width: 100%; height: 56px" aria-hidden="true"><path d="M0 6 Q130 46 260 10 Q390 46 520 6" fill="none" stroke="#2E7D4F" stroke-width="5"></path>'
           '<g stroke="#D4A53A" stroke-width="2"><line x1="60" y1="20" x2="60" y2="30"></line><line x1="160" y1="30" x2="160" y2="40"></line><line x1="260" y1="10" x2="260" y2="20"></line>'
           '<line x1="360" y1="30" x2="360" y2="40"></line><line x1="460" y1="20" x2="460" y2="30"></line></g><circle cx="60" cy="40" r="11" fill="#D4A53A"></circle><circle cx="160" cy="50" r="9" fill="#FFFFFF"></circle>'
           '<circle cx="260" cy="31" r="12" fill="#2E7D4F"></circle><circle cx="360" cy="50" r="9" fill="#FFFFFF"></circle><circle cx="460" cy="40" r="11" fill="#D4A53A"></circle></svg>')

hero_list = ''.join(check(t) for t in ['Carta de Papá Noel <u>con el nombre de tu hijo</u>', 'Personajes <u>con la cara de tu familia</u>',
                                       'Calendario de adviento de 24 días', 'Decoración, cajitas y etiquetas', '+70 actividades para niños'])

body = f'''
<div class="snowg" style="font-family: Inter, system-ui, sans-serif; color: {INK}; width: 100%; padding-bottom: 40px">

<div class="topbar" id="pricebar" style="background: {GREEN}; color: #FFFFFF; padding: 9px 8px; display: flex; flex-wrap: wrap; gap: 5px; justify-content: center; align-items: center; font-weight: 800; font-size: clamp(11.5px, 3.3vw, 14px)">
<span style="white-space: nowrap">EL PRECIO SUBE A US$&nbsp;9,90 EN:</span>
<span style="background: {RED}; padding: 3px 6px; border-radius: 6px; white-space: nowrap"><span class="pc-d">0</span>d</span>
<span style="background: {RED}; padding: 3px 6px; border-radius: 6px; white-space: nowrap"><span class="pc-h">0</span>h</span>
<span style="background: {RED}; padding: 3px 6px; border-radius: 6px; white-space: nowrap"><span class="pc-m">0</span>m</span>
<span style="background: {RED}; padding: 3px 6px; border-radius: 6px; white-space: nowrap"><span class="pc-s">0</span>s</span>
</div>
<div class="cane"></div>

<div class="col" style="max-width: 560px; margin: 0 auto; background: {CREAM}; display: flex; flex-direction: column; box-shadow: 0 0 0 6px {GOLD}">

<!-- 1. TOPO -->
<section class="snow" style="color: #FFFFFF; padding: 0 clamp(14px, 4.6vw, 20px) 34px; display: flex; flex-direction: column; gap: 18px; text-align: center">
<span style="align-self: center; margin-top: 14px; background: #FFE08A; color: {INK}; font-weight: 800; font-size: clamp(12.5px, 3.6vw, 14px); padding: 7px 12px; border-radius: 999px">🎄 MAMÁ, ANTES DE GASTAR UNA FORTUNA EN REGALOS, MIRA ESTO 👇</span>
<h1 style="margin: 0; display: flex; flex-direction: column; gap: 4px; line-height: 1.04">
<span style="font-family: 'Lilita One', sans-serif; font-size: clamp(34px, 9.6vw, 54px); color: #FFE08A; text-wrap: balance; text-shadow: 0 4px 0 #6E0914">Convierte a tu familia en personajes navideños</span>
<span style="font-size: clamp(21px, 6vw, 30px); text-wrap: balance">+500 imprimibles para imprimir en casa por solo <span style="background: #12A150; padding: 0 8px; border-radius: 8px; white-space: nowrap">US$&nbsp;4,90</span></span>
</h1>
<div style="position: relative; background: {CREAM}; border: 6px solid {GOLD}; border-radius: 20px; padding: 6px; display: flex; flex-direction: column; gap: 8px; box-shadow: 0 10px 0 rgba(0,0,0,.18)">
<div style="position: relative">
<img src="familia.webp" alt="Personajes navideños de papel con las caras de papá, mamá, los niños y la abuela" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 14px; display: block">
<span style="position: absolute; top: -14px; left: -12px; width: clamp(84px, 24vw, 108px); height: clamp(84px, 24vw, 108px); border-radius: 50%; background: {GOLD}; color: {RED}; border: 4px solid #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; transform: rotate(-12deg); box-shadow: 0 6px 14px rgba(0,0,0,.3); line-height: 1"><span style="font-family: 'Lilita One', sans-serif; font-size: clamp(26px, 7.4vw, 34px)">6 KITS</span><span style="font-size: clamp(10px, 2.8vw, 12px); font-weight: 800">+ BONO</span></span>
<span style="position: absolute; left: 10px; right: 10px; bottom: 10px; background: rgba(110,9,20,.92); color: #FFFFFF; font-weight: 800; font-size: clamp(14px, 4.2vw, 17px); line-height: 1.25; padding: 8px 12px; border-radius: 10px; border: 2px solid #FFE08A">📸 Pon su carita en Papá Noel, el duende, el reno y más</span>
</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; padding: 0 2px 4px"><figure style="margin: 0; display: flex; flex-direction: column; gap: 4px"><img src="kit2.webp" alt="Carta de Papá Noel" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 9px; display: block; border: 2px solid #FFFFFF"><figcaption style="font-size: clamp(10.5px, 2.9vw, 13px); line-height: 1.15; font-weight: 800; color: {RED}">Carta de Papá Noel</figcaption></figure><figure style="margin: 0; display: flex; flex-direction: column; gap: 4px"><img src="deco.webp" alt="Decoración" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 9px; display: block; border: 2px solid #FFFFFF"><figcaption style="font-size: clamp(10.5px, 2.9vw, 13px); line-height: 1.15; font-weight: 800; color: {RED}">Decoración</figcaption></figure><figure style="margin: 0; display: flex; flex-direction: column; gap: 4px"><img src="kit3.webp" alt="Personajes" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 9px; display: block; border: 2px solid #FFFFFF"><figcaption style="font-size: clamp(10.5px, 2.9vw, 13px); line-height: 1.15; font-weight: 800; color: {RED}">Personajes</figcaption></figure><figure style="margin: 0; display: flex; flex-direction: column; gap: 4px"><img src="actividades.webp" alt="Actividades" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 9px; display: block; border: 2px solid #FFFFFF"><figcaption style="font-size: clamp(10.5px, 2.9vw, 13px); line-height: 1.15; font-weight: 800; color: {RED}">Actividades</figcaption></figure></div>
</div>
<div style="display: flex; flex-direction: column; gap: 8px">{btn('QUIERO MI KIT POR US$&nbsp;4,90')}
<p style="margin: 0; font-size: clamp(12px, 3.4vw, 14px); line-height: 1.45; color: #FFFFFF; font-weight: 600">✅ Garantía de 7 días · ⚡ Acceso inmediato por email · 📄 Producto digital (PDF)</p></div>
<p style="margin: 4px 0 0; font-size: clamp(17px, 4.6vw, 19px); font-weight: 800; color: #FFFFFF">Esto es lo que recibes hoy:</p>
<ul style="list-style: none; margin: 0; padding: 16px 14px; display: flex; flex-direction: column; gap: 11px; text-align: left; background: rgba(0,0,0,.18); border: 2px solid #E2B13C; border-radius: 16px; font-size: clamp(18px, 5vw, 21px); line-height: 1.3; font-weight: 800; color: #FFE08A">{hero_list}</ul>
<p style="margin: 0; font-size: clamp(18px, 5vw, 21px); font-weight: 800; color: #FFFFFF">Compras hoy, imprimes hoy, lo usas hoy.</p>
{btn('QUIERO MI KIT NAVIDEÑO POR US$&nbsp;4,90')}
<p style="margin: 0; font-size: 14px; color: #FFE9E9">Acceso inmediato por email · Pago único · Garantía de 7 días</p>
</section>
<div class="cane"></div>

<!-- 2. DOR -->
<section style="background: #1A1A1A; color: #FFFFFF; {PAD}; display: flex; flex-direction: column; gap: 14px">
<h2 style="{H2}">¿Te pasa esto cada diciembre?</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.6">Quieres que tus hijos vivan una Navidad especial… pero los regalos están cada vez más caros. Gastas mucho y, a los dos días, el juguete queda olvidado en un rincón.</p>
<p style="margin: 0; font-size: 19px; line-height: 1.45; font-weight: 800; color: #FFE08A">Lo que los niños recuerdan de verdad no es lo que costó más.</p>
<p style="margin: 0; font-size: 17px; line-height: 1.6">Es la magia: <strong>la carta que llegó con su nombre</strong>, <strong>la cuenta regresiva cada mañana</strong>, <strong>la casa decorada en familia</strong>.</p>
</section>

<!-- 3. SOLUCIÓN -->
<section style="{PAD}; display: flex; flex-direction: column; gap: 16px; text-align: center">
<p style="margin: 0; font-family: 'Mountains of Christmas', serif; font-size: 28px; color: {GOLD}">Por eso creamos el</p>
<h2 style="{H2}; color: {RED}">Mega Kit Navidad Mágica 2026</h2>
<p style="margin: 0; font-size: 17px; line-height: 1.6">Más de 500 imprimibles diseñados para que tú, con tu impresora de casa, crees momentos que tus hijos nunca van a olvidar. <strong>Sin gastar de más y sin saber nada de diseño.</strong></p>
<p style="margin: 6px 0 0; font-size: 18px; font-weight: 800; color: {GREEN}">Imagina su carita cuando…</p>
<div style="display: flex; flex-direction: column; gap: 10px; text-align: left">
<div style="background: #FFFFFF; border: 2px solid #E9D6AE; border-radius: 12px; padding: 14px 16px; font-size: 16px; line-height: 1.45"><span style="color: {GOLD}">★</span> Abren una <strong>carta de Papá Noel con su nombre</strong> y su certificado de niño bueno</div>
<div style="background: #FFFFFF; border: 2px solid #E9D6AE; border-radius: 12px; padding: 14px 16px; font-size: 16px; line-height: 1.45"><span style="color: {GOLD}">★</span> Se ven <strong>convertidos en duendes y renos con su propia cara</strong>, junto a papá, mamá y los abuelos</div>
<div style="background: #FFFFFF; border: 2px solid #E9D6AE; border-radius: 12px; padding: 14px 16px; font-size: 16px; line-height: 1.45"><span style="color: {GOLD}">★</span> Abren una casita del <strong>calendario de adviento</strong> cada mañana</div>
<div style="background: #FFFFFF; border: 2px solid #E9D6AE; border-radius: 12px; padding: 14px 16px; font-size: 16px; line-height: 1.45"><span style="color: {GOLD}">★</span> Reparten <strong>sus propios detalles</strong> a los amiguitos de la escuela</div>
</div>
</section>

<!-- PERSONAJES SPOTLIGHT -->
<section style="background: {RED}; color: #FFFFFF; {PAD}; display: flex; flex-direction: column; gap: 16px; text-align: center">
<span style="align-self: center; background: #FFE08A; color: {INK}; font-weight: 800; font-size: 13px; padding: 6px 12px; border-radius: 999px">LO QUE MÁS AMAN LOS NIÑOS</span>
<h2 style="{H2}">Papá, mamá, los niños y los abuelos… <span style="color: #FFE08A">convertidos en personajes navideños</span></h2>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
<img src="familia.webp" alt="Papá Noel, Mamá Noel, duende, reno y muñeco de nieve con las caras de la familia" style="grid-column: 1 / -1; width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 14px; border: 5px solid {GOLD}; display: block">
<img src="kit3.webp" alt="Niños como duende, reno y muñeco de nieve" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 12px; border: 4px solid #FFFFFF; display: block">
<div style="background: rgba(0,0,0,.2); border: 2px solid {GOLD}; border-radius: 12px; padding: 10px; display: flex; flex-direction: column; justify-content: center; gap: 6px; font-weight: 800; font-size: clamp(14px, 4vw, 16px); line-height: 1.3; text-align: left">
<span>✂️ 1. Imprime el personaje</span><span>📸 2. Recorta la foto de su cara</span><span>✨ 3. Pégala ¡y listo!</span></div>
</div>
<p style="margin: 0; font-size: 16px; line-height: 1.55; color: #FFE9E9">10 personajes: <strong style="color: #FFFFFF">Papá Noel, Mamá Noel, duende, reno, muñeco de nieve, ángel, pingüino, galleta de jengibre, rey mago y pastorcito</strong>. En 2 tamaños y con versiones para colorear.</p>
<p style="margin: 0; font-size: 18px; font-weight: 800; color: #FFE08A">Perfectos para el árbol, la puerta, la mesa de Nochebuena… ¡y para las fotos de la familia!</p>
{btn('QUIERO CONVERTIR A MI FAMILIA EN PERSONAJES')}
</section>
<div class="cane"></div>

<!-- 4. LO QUE RECIBES -->
<section class="snowg" style="padding: 36px clamp(14px, 4.6vw, 20px); display: flex; flex-direction: column; gap: 14px">
<p style="margin: 0; text-align: center; font-family: 'Mountains of Christmas', serif; font-size: 28px; color: #FFE08A">Más de 500 imprimibles</p>
<h2 style="{H2}; color: #FFFFFF; margin-bottom: 4px">Esto es todo lo que recibes</h2>
{''.join(kit_card(i, *k) for i, k in enumerate(KITS))}
</section>

<!-- 5. CÓMO FUNCIONA -->
<section style="{PAD}; display: flex; flex-direction: column; gap: 14px">
<h2 style="{H2}; color: {GREEN}">Así de fácil</h2>
{''.join(f'<div style="display: flex; gap: 14px; align-items: center; background: #FFFFFF; border-radius: 14px; padding: 14px 16px; border: 2px solid #E9D6AE"><span class="lil" style="flex: 0 0 44px; height: 44px; border-radius: 50%; background: {RED}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-family: \'Lilita One\', sans-serif; font-size: 24px">{n}</span><span style="font-size: 17px; line-height: 1.4; font-weight: 700">{t}</span></div>' for n, t in ((1, 'Haces tu compra en un minuto.'), (2, 'Recibes el acceso al instante en tu correo.'), (3, 'Descargas, imprimes y listo. ¡La magia empieza hoy mismo!')))}
<ul style="list-style: none; margin: 6px 0 0; padding: 0; display: flex; flex-direction: column; gap: 9px; font-size: 16px; font-weight: 700; color: {GREEN}">
{check('Funciona con cualquier impresora de casa', GREEN, '#FFFFFF')}{check('Puedes imprimir todas las veces que quieras', GREEN, '#FFFFFF')}{check('No necesitas programas ni saber diseño: es un PDF listo', GREEN, '#FFFFFF')}
</ul>
</section>

<!-- 6. LA CUENTA + OFERTA -->
<section id="oferta" style="background: #F6EAD2; padding: 36px clamp(14px, 4.6vw, 20px); display: flex; flex-direction: column; gap: 16px">
<h2 style="{H2}; color: {RED}">Haz la cuenta</h2>
<div style="background: #FFFFFF; border: 4px solid {RED}; border-radius: 18px; overflow: hidden">
<div class="cane"></div>
{''.join(f'<div class="row" style="display: flex; justify-content: space-between; gap: 10px; align-items: center; padding: 13px 16px; border-bottom: 1px solid #F0E2C6"><span style="font-size: 15px; line-height: 1.35; font-weight: 600"><span style="color: #12A150">✓</span> {n}</span><s style="font-size: 14px; color: #8A1A1A; white-space: nowrap">US$&nbsp;{v}</s></div>' for n, v in STACK)}
<div class="snow" style="color: #FFFFFF; padding: 22px 16px; display: flex; flex-direction: column; gap: 4px; text-align: center">
<span style="font-size: 16px">Valor de todo el kit: <s>US$&nbsp;97</s></span>
<span style="font-size: 16px; font-weight: 800; color: #FFE08A">HOY SOLO</span>
<span style="font-family: 'Lilita One', sans-serif; font-size: clamp(46px, 15vw, 66px); line-height: 1">US$&nbsp;4,90</span>
<span style="font-size: 15px; font-weight: 800">Menos que un café con pastel</span>
<span style="font-size: 14px; color: #FFE9E9">…y menos de 1 centavo por imprimible</span>
</div>
</div>
{btn('SÍ, QUIERO MI KIT AHORA')}
<div style="background: {GREEN}; color: #FFFFFF; border-radius: 12px; padding: 14px; text-align: center; font-size: 15px; line-height: 1.5"><strong style="color: #FFE08A">ATENCIÓN:</strong> este precio es solo hasta el <strong>1 de diciembre a las 23:59</strong>. Después sube a <strong>US$&nbsp;9,90</strong>.</div>
</section>

<!-- 7. BONO -->
<section style="background: #FFF1C9; padding: 32px clamp(14px, 4.6vw, 22px); display: flex; flex-direction: column; gap: 12px; text-align: center; border-top: 4px dashed {GOLD}; border-bottom: 4px dashed {GOLD}">
<span style="align-self: center; background: {RED}; color: #FFFFFF; font-weight: 800; font-size: 13px; padding: 6px 12px; border-radius: 999px">DE REGALO SI COMPRAS HOY</span>
<h2 style="{H2}; color: {GREEN}">Bono: Guía para vender tus detalles y ganar dinero extra</h2>
<p style="margin: 0; font-size: 16px; line-height: 1.55">Qué vender, cómo calcular tu precio, tabla para completar y mensajes listos para conseguir pedidos de mamás, maestras y empresas. <strong>Con tus primeras ventas, el kit ya se pagó solo.</strong></p>
</section>

<!-- OBJECIONES -->
<section style="{PAD}; display: flex; flex-direction: column; gap: 12px">
<h2 style="{H2}; color: {GREEN}; margin-bottom: 4px">“Sí, pero…”</h2>
{''.join(f'<div style="background: #FFFFFF; border: 2px solid #E9D6AE; border-radius: 12px; padding: 14px 16px; font-size: 16px; line-height: 1.45"><strong style="color: {RED}">“{q}”</strong><br>{a}</div>' for q, a in (('No tengo impresora.', 'Lleva los archivos a cualquier papelería o centro de copiado. Te sale baratísimo.'), ('No tengo tiempo.', 'Imprimes, recortas y armas. Los niños te ayudan y se vuelve parte de la diversión.'), ('No soy buena para las manualidades.', 'Si sabes usar una tijera, sabes armarlo. Cada modelo trae instrucciones simples.')))}
</section>

<!-- 8. ASÍ QUEDA -->
<section style="background: #F6EAD2; padding: 34px clamp(14px, 4.6vw, 20px); display: flex; flex-direction: column; gap: 12px">
<h2 style="{H2}; color: {GREEN}">Así queda tu Navidad en casa</h2>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">
<figure style="grid-column: 1 / -1; margin: 0; display: flex; flex-direction: column; gap: 6px"><img src="familia.webp" alt="Personajes navideños con las caras de toda la familia" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 14px; border: 4px solid #FFFFFF; display: block"><figcaption style="font-size: 13px; line-height: 1.35; text-align: center; color: #4A4236">Toda la familia convertida en personajes</figcaption></figure>
<figure style="margin: 0; display: flex; flex-direction: column; gap: 6px"><img src="deco.webp" alt="Sala decorada con letras Feliz Navidad y calendario de adviento de casitas de papel" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 14px; border: 4px solid #FFFFFF; display: block"><figcaption style="font-size: 13px; line-height: 1.35; text-align: center; color: #4A4236">Decoración y calendario de adviento</figcaption></figure>
<figure style="margin: 0; display: flex; flex-direction: column; gap: 6px"><img src="actividades.webp" alt="Niños coloreando actividades navideñas impresas" style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 14px; border: 4px solid #FFFFFF; display: block"><figcaption style="font-size: 13px; line-height: 1.35; text-align: center; color: #4A4236">Actividades lejos de las pantallas</figcaption></figure>
</div>
</section>

<!-- 9. GARANTÍA -->
<section style="padding: 34px clamp(14px, 4.6vw, 22px); display: flex; flex-direction: column; gap: 12px; align-items: center; text-align: center">
<svg width="90" height="90" viewBox="0 0 24 24" fill="none" stroke="{RED}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3z"></path><path d="M8.5 12l2.5 2.5 4.5-5"></path></svg>
<h2 style="{H2}; color: {GREEN}">Garantía de 7 días: riesgo cero</h2>
<p style="margin: 0; font-size: 16px; line-height: 1.55">Si por cualquier motivo no te encanta, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. <strong>O tus hijos viven la Navidad más mágica, o no pagas nada.</strong></p>
</section>

<!-- 10. OFERTA FINAL -->
<div class="cane"></div>
<section class="snow" style="color: #FFFFFF; padding: 40px clamp(14px, 4.6vw, 20px); display: flex; flex-direction: column; gap: 14px; text-align: center">
<h2 style="{H2}">Tus hijos solo van a ser niños por unas pocas Navidades.</h2>
<p style="margin: 0; font-family: 'Mountains of Christmas', serif; font-size: 30px; color: #FFE08A">Haz que esta sea inolvidable</p>
<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px">Valor de todo el kit: <s>US$&nbsp;97</s></span><span style="font-family: 'Lilita One', sans-serif; font-size: clamp(44px, 13vw, 58px); line-height: 1">US$&nbsp;4,90</span></div>
<p style="margin: 0; font-size: 14px; color: #FFE9E9">Pago único · Acceso inmediato · Garantía de 7 días</p>
{btn('SÍ, QUIERO LA NAVIDAD MÁS MÁGICA PARA MIS HIJOS')}
<p style="margin: 0; font-size: 15px; font-weight: 700">Faltan <span class="cd-d">0</span> días para Navidad. Empieza hoy tu calendario de adviento.</p>
</section>

<!-- 11. FAQ -->
<section style="background: #F6EAD2; padding: 34px clamp(14px, 4.6vw, 20px); display: flex; flex-direction: column; gap: 10px">
<h2 style="{H2}; color: {GREEN}; margin-bottom: 6px">Preguntas frecuentes</h2>
{''.join(faq_item(i, q, a) for i, (q, a) in enumerate(FAQ))}
<div style="margin-top: 10px; display: flex; flex-direction: column">{btn('QUIERO MI KIT POR US$&nbsp;4,90')}</div>
</section>

<footer style="padding: 20px 20px 24px; text-align: center; font-size: 13px; color: #5A5145">Producto 100% digital, no se envía nada físico · Soporte: <a href="mailto:mentora.ao@gmail.com" style="color: #A50E1E; font-weight: 700">mentora.ao@gmail.com</a></footer>
<div class="sticky" style="position: sticky; bottom: 0; background: {GREEN}; padding: 10px 14px; display: flex; gap: 12px; align-items: center; justify-content: space-between; border-top: 3px solid {GOLD}">
<span style="color: #FFFFFF; font-size: 14px; line-height: 1.3"><s style="color: #F2B8B8">US$&nbsp;97</s> <strong style="font-size: 20px; color: #FFE08A">US$&nbsp;4,90</strong><br>⏰ Precio sube el 01/12</span>
<a class="buy sbtn" href="{CK}" style="background: #12A150; color: #FFFFFF; text-decoration: none; font-weight: 800; font-size: 16px; padding: 14px 18px; border-radius: 12px; white-space: nowrap">COMPRAR AHORA</a>
</div>

</div>
</div>
'''
import re
names=iter(['hero_top','hero','personajes','oferta','final','faq','sticky'])
body=re.sub(r'<a class="buy', lambda m: f'<a data-pos="{next(names)}" class="buy', body)
open('index.html', 'w').write(head + body + tail)
print('ok', len(head + body + tail))
