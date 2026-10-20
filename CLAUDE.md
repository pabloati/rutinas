# Rutinas de entrenamiento en casa — contexto del proyecto

Este archivo resume una conversación previa con Claude (claude.ai) donde se diseñaron estas rutinas.
Úsalo como contexto completo. Responde al usuario en **español**, con vocabulario sencillo
(no es nativo de inglés; le gustan las analogías, pero sin abusar).

## El usuario

- Trabaja en bioinformática (long-read transcriptomics), cómodo con terminal y git.
- Objetivo: perder grasa (sobre todo abdominal) y ganar fuerza general.
- Nivel: hace ejercicio ocasional. Entrena 3 días por semana.
- Puede hacer **pocas dominadas** (empezar con negativas y asistidas).
- Usa las rutinas sobre todo **en el móvil** mientras entrena.

## Material disponible

- Mancuernas regulables, hasta 10 kg (no está claro si 10 kg cada una o el juego completo; los pesos van en rangos).
  **Los discos son redondos**: ruedan, no sirven como apoyo (afecta al remo renegado y a la plancha con arrastre).
- Comba.
- Barra de dominadas (agarre ancho prono y agarre neutro, palmas mirándose).
- Gomas de fuerza (las tiene, pero en la rutina C pidió no usarlas).
- Una silla resistente.

## Reglas de diseño (pedidas por el usuario)

1. Sesiones de **45–50 min**.
2. **Un solo peso por circuito**: nunca cambiar las mancuernas dentro de un circuito.
   Cada circuito lleva un recuadro `.wt` con el peso.
3. **60 s de descanso** entre rondas de los circuitos (excepción propuesta: 90 s en el circuito de barra de la rutina Pull).
4. **Sin comba en el calentamiento** (la comba sí en bloques de cardio/core).
5. Estructura típica: calentamiento 7 min → 2–3 circuitos de 3 ejercicios × 3 rondas → bloque core/cardio 40 s trabajo / 20 s descanso × 2 vueltas → estiramientos 4 min.
6. Planificar y comentar con el usuario **antes** de generar archivos cuando pida "vamos a hablar primero".

## Estado actual del repo

| Archivo | Contenido |
|---|---|
| `index.html` | Página de inicio: enlaces a las seis rutinas y rotación semanal (Push A/B alternando). |
| `rutina_push.html` | Push A: pecho, hombro, tríceps + cuádriceps. 3 circuitos (60 s), core + comba. |
| `rutina_push_B.html` | Push B (octubre 2026, el usuario notó demasiado hombro y poco tríceps en la A): sin press de hombro ni elevaciones laterales. C1 press en el suelo codos pegados + sentadilla con mancuernas a los lados (8–10 kg); C2 aperturas en el suelo, extensión de tríceps tumbado, patada de tríceps (4–6 kg); C3 flexiones diamante, fondos en silla, extensión de tríceps en la silla; core: comba, plancha lateral, comba, elevación de piernas. Se alterna con la A de una semana a otra. |
| `rutina_pull.html` | Pull: espalda, bíceps + glúteo/isquios. Circuito 1 de barra (90 s) con tabla de progresión, 2 circuitos de mancuernas (60 s), core + comba. |
| `rutina_A.html` | Full body A: piernas + empuje. 2 circuitos (90 s de descanso), core + comba. |
| `rutina_B.html` | Full body B: 3 circuitos (60 s), con brazos (curl, tríceps). Circuito 3 con gomas y silla. |
| `rutina_C.html` | Full body C: cardio, hombro, core de estabilidad. Sin gomas, con saltos. |

Rotación semanal (en `index.html`): Push – Pull – una full body rotando (semana 1 A, semana 2 B, semana 3 C). Alternativa: A-B-C.

### Funciones ya implementadas (en los tres HTML)

Cada HTML es **un único archivo autocontenido** (CSS y JS inline, SVG inline). Solo usa Google Fonts (Barlow / Barlow Condensed) con fallback de sistema.

- **Esquemas SVG** de cada ejercicio (figuras de palitos, `viewBox 0 0 160 110`, suelo en y=100). Clases: `.s` trazo, `.h` cabeza, `.w` peso (color de acento), `.a` flechas con `marker url(#m)`, `.f` suelo, `.bench` silla.
- **Modo claro/oscuro** con tokens en `:root` y `prefers-color-scheme`.
- **Zoom** con botones A−/A+ (CSS `zoom` en `main`, guardado en localStorage `rutina-zoom`).
- **Cronómetros** `button.tm[data-t]` en todo lo que va por tiempo (también los descansos `.rest`).
  `data-split` = aviso a mitad para cambiar de lado. Pitidos en los 3 últimos segundos, vibración, wake lock.
  Emite el evento `tmdone`. Expone `window.tmDraw` y `window.tmBeep`.
- **Tiempos editables**: botones −/+ (5 s; 10 s si hay split) que actualizan también el texto de la etiqueta.
  Guardado en localStorage con clave `rutina-t:<pathname>:<índice>`. Botón "Restablecer los tiempos originales".
- **Modo continuo**: botón "▶ Bloque seguido" en cada sección con 2+ cronómetros. Encadena ejercicios, descansos
  (leídos del texto `.sub`: "N s de descanso"; si no, 5 s "Prepárate"), vueltas ("N veces") y lados ("por lado").
  Barra inferior fija con tiempo, ejercicio actual/siguiente, pausa, saltar y parar.
- **Contador de rondas** (`.rnd`, creado por JS tras cada `.rest` cuyo `.sub` dice "N rondas"): "Ronda r / N" con botones −/+.
  Sube solo cuando acaba el cronómetro del descanso (evento `tmdone`), topa en N ("Última ronda", borde de acento).
  Se guarda en localStorage `rutina-r:<pathname>` con marca de tiempo y caduca a las 3 h (para que la sesión siguiente empiece en 1).
- **Vídeos**: enlace "▶ Ver vídeo" por ejercicio = búsqueda de YouTube con el nombre en inglés + "tutorial"
  (no enlazar vídeos concretos, pueden desaparecer).

## Hecho (octubre 2026)

- Rutina C: remo renegado → "remo en plancha, mano en el suelo" (una mancuerna); pista de la toalla en la plancha con arrastre.
- Rutina A: añadidos los recuadros `.wt` con el peso de cada circuito.
- Rutinas Push y Pull creadas según el plan de abajo (mismo CSS/JS que A/B/C; la Pull añade `.prog` para la tabla de progresión en la barra).
- `index.html` con las cinco rutinas y la rotación semanal.
- Repo subido a GitHub (`pabloati/rutinas`, rama `main`).

## Tareas pendientes (en este orden)

### 1. Pregunta abierta (no tocar sin confirmar)

- (Opcional, el usuario no lo confirmó) Rutina B circuito 3: sustituir gomas por dos mancuernas de 3–4 kg
  (elevaciones laterales y curl martillo a 15 reps con bajada en 3 s). **Preguntar antes.**

### 2. Diseño de PUSH y PULL (ya implementado, se deja como referencia)

Push = pecho, hombro, tríceps + cuádriceps. Pull = espalda, bíceps + glúteo/isquios.

**PUSH (~46 min)**
- Calentamiento (7 min, sin comba): marcha, círculos de brazos, flexiones contra la pared, rotación de tronco a cuatro apoyos, sentadilla con alcance, flexión pica suave.
- Circuito 1 (dos mancuernas, 8–10 kg): press en el suelo 10, sentadilla frontal con mancuernas en los hombros 12.
- Circuito 2 (dos mancuernas, 4–6 kg): press de hombro de pie 10, elevaciones laterales 12, extensión de tríceps tumbado 12.
- Circuito 3 (sin peso): flexiones con pies en silla (o normales), fondos en silla, flexión pica.
- Core + comba (2 vueltas, 40/20): comba, plancha con toque de hombro, comba, hollow hold.
- Estiramientos: pecho, hombro, tríceps, cuádriceps.

**PULL (~48 min)**
- Calentamiento (7 min, sin comba): marcha, círculos de brazos, gato-camello, bisagra de cadera sin peso, colgarse de la barra, dominada escapular.
- Circuito 1 (barra, **90 s de descanso**): dominadas agarre ancho (3 negativas de 4–5 s), dominadas agarre neutro (5 asistidas con el pie en la silla), elevación de rodillas colgado 8–10.
  Tabla de progresión: 6 negativas buenas → 1–2 completas + negativas; 3 completas → 3 + 2 negativas; después 5 completas.
- Circuito 2 (dos mancuernas, 6–8 kg): remo inclinado 12, peso muerto rumano 12, curl de bíceps 10.
- Circuito 3 (una mancuerna, 8–10 kg): remo a una mano 10/brazo, pullover en el suelo 12, puente de glúteo a una pierna 10/pierna (sin peso).
- Core + comba (2 vueltas, 40/20): comba, dead bug, comba, superman.
- Estiramientos: colgarse relajado de la barra, bíceps, isquios, dorsal en la silla, postura del niño.

### 3. Repeticiones editables + sincronización entre dispositivos

- Botones −/+ junto a cada número de repeticiones (`.reps`), igual que con los tiempos.
  Ojo: en la Pull hay reps con texto ("3 negativas", "5 asistidas", "8–10 reps"); el parser debe tolerar rangos y palabras.
- Guardar **repeticiones y tiempos** de las cinco rutinas en `progreso.json` en **este mismo repositorio (público)**. El usuario acepta que su progreso sea público.
- Lectura: sin token (repo público; ojo al límite de 60 peticiones/hora sin autenticar, cachear en localStorage).
- Escritura: API REST de GitHub (`PUT /repos/{owner}/{repo}/contents/progreso.json`, con el `sha` actual), con un
  **token fine-grained** (solo Contents read/write sobre este repo) que el usuario pega una vez por dispositivo en
  un menú de ajustes y se guarda en localStorage. **El token nunca va en el código ni en el repo.**
- Guardado con debounce; si no hay red o token, guardar en local y sincronizar después. Si falla por `sha` desactualizado, releer y reintentar (gana el último).
- Ojo: cada escritura es un commit. Agrupar cambios (debounce de varios segundos o guardar al terminar la sesión) para no llenar el historial de commits.
- **Pregunta pendiente al usuario**: ¿incluir **historial por sesión** (fecha + repeticiones/tiempos) para ver la evolución, o solo los valores actuales?

### 4. GitHub Pages

Repo público `pabloati/rutinas`, Pages desde la rama `main` (carpeta raíz). URL: https://pabloati.github.io/rutinas/.
Si no está activado: Settings → Pages → Source "Deploy from a branch" → `main` / `/ (root)`.

## Notas técnicas

- Sin build ni dependencias: HTML estático.
- Las pruebas de la conversación anterior se hicieron con `jsdom` en Node (simulando `Date.now` para acelerar los cronómetros). Mantener los IDs/clases existentes para no romper los scripts.
- Diseño: fondo `#EEF1F4`, tinta `#16202B`, acento cobalto `#2F6FE4` (modo oscuro: `#121820` / `#E6EBF0` / `#6C9EFF`). Números de repeticiones grandes en Barlow Condensed.
- Contenido de salud: no dar planes de dieta con cifras; las rutinas no sustituyen consejo médico.
