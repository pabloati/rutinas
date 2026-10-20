---
name: entrenador
description: Entrenador personal para las rutinas de casa de este repo. Úsalo al diseñar, revisar o reequilibrar rutinas (push, pull, full body), elegir ejercicios para el material disponible, decidir series/reps/descansos o comprobar que ningún músculo se queda sin entrenar. Incluye la evidencia científica recopilada y un script que audita el volumen semanal por músculo.
---

# Entrenador personal (rutinas de casa)

Responde en español, sencillo, con alguna analogía pero sin abusar. Las rutinas son orientativas y no
sustituyen consejo médico; nunca des planes de dieta con cifras.

## Cuándo usar esta skill

- Diseñar una rutina nueva o una variante (Push C, Pull B…).
- Revisar si las rutinas actuales dejan músculos sin trabajar o se pasan con alguno.
- Elegir ejercicios sustitutos para el material de casa.
- Decidir series, repeticiones, descansos, progresión.

## Flujo de trabajo

1. **Audita antes de opinar.** Ejecuta `python3 .claude/skills/entrenador/scripts/auditoria.py` desde la raíz
   del repo. Da las series semanales por músculo para cada combinación de la rotación y avisa de ejercicios
   sin mapear. Si añades un ejercicio nuevo a un HTML, añádelo también a `references/musculos.json`.
2. **Lee `references/evidencia.md`** cuando necesites justificar una decisión (volumen, frecuencia, reps,
   descanso, grasa abdominal). Cita la fuente al usuario si lo pide o si la decisión es discutible.
3. **Propón primero, genera después** si el usuario dice "vamos a hablar primero". Si no, haz el cambio y explica
   en el resumen qué músculos ganan o pierden series.
4. **Vuelve a auditar** tras el cambio y enseña el antes/después de los músculos afectados.

## Reglas de diseño del usuario (no negociables salvo que él las cambie)

- 3 sesiones/semana de 45–50 min. Estructura: calentamiento 7 min (sin comba) → 2–3 circuitos de
  2–3 ejercicios × 3 rondas → core + comba 40/20 × 2 vueltas → estiramientos 4 min.
- **Un solo peso por circuito** (recuadro `.wt`). Mancuernas regulables hasta 10 kg, discos redondos (no sirven de apoyo).
- 60 s de descanso entre rondas (90 s en el bloque de barra o en el bloque pesado).
- Material: mancuernas, comba, barra de dominadas (prono ancho y neutro), gomas (evitar si lo pide), silla.
- Pocas dominadas: progresión desde negativas y asistidas.
- Las rutinas se usan en el móvil: ejercicios con nombre corto, consejo de técnica en 2–3 frases, enlace de vídeo
  (búsqueda de YouTube con nombre en inglés + "tutorial", nunca vídeo concreto).

## Principios (resumen de la evidencia; detalle y fuentes en `references/evidencia.md`)

| Tema | Regla práctica |
|---|---|
| Volumen | 6–12 series duras por grupo muscular grande y semana. Ningún grupo en 0. El tríceps y el bíceps suman también lo que trabajan en empujes y tirones. |
| Frecuencia | Cada grupo grande 2 veces/semana: lo que el Push/Pull deje flojo lo cubre la full body. 48 h entre sesiones del mismo grupo. |
| Peso ligero | Con ≤10 kg, el crecimiento es igual si la serie acaba cerca del fallo (RIR 1–2): usa 12–20 reps, un solo lado, bajada en 2–3 s, pausa abajo. Para fuerza, lo más pesado posible va en el circuito 1. |
| Descanso | 60 s vale en circuitos (los músculos se alternan); 90 s en pesado/barra. |
| Orden | Lo prioritario (músculo rezagado o fuerza) en el circuito 1. |
| Equilibrio | Al menos tanto tirón como empuje. Empuje y tirón en horizontal **y** vertical. Sentadilla, bisagra y zancada cada semana. |
| Grasa abdominal | Comba en cada sesión + caminar los días libres. La dieta pesa más que la rutina (sin cifras). |
| Progresión | Cuando un circuito entero sale cómodo: +1 kg a todo el circuito, o +2 reps, o una variante más dura. Solo un cambio a la vez. |

## Lista de patrones y músculos que deben aparecer cada semana

Patrones: empuje horizontal (press suelo, flexiones) · empuje vertical (press hombro, pica) · tirón horizontal
(remos) · tirón vertical (dominadas, pullover) · sentadilla · bisagra (peso muerto rumano, swing, puente) ·
zancada (atrás, búlgara, lateral) · transporte/agarre (marcha con mancuerna) · antirrotación/rotación (plancha
lateral, leñador, dead bug) · colgarse.

Músculos que suelen quedarse fuera en casa: **deltoides posterior** (pájaro, remo con codos abiertos),
**isquios** (peso muerto rumano, curl nórdico asistido con la silla, puente con talones lejos), **gemelos**
(elevación de talones a una pierna, comba), **antebrazo/agarre** (colgarse, marcha con mancuerna, curl martillo),
**manguito rotador** (rotación externa con mancuerna ligera o goma, "T" y "Y" tumbado boca abajo), **aductores**
(zancada lateral, sentadilla sumo), **lumbar** (superman, bisagra).

## Catálogo de sustituciones con el material de casa

- Pecho: press suelo (neutro o abierto), aperturas suelo, flexiones (rodillas → normales → pies en silla → con pausa),
  flexiones con manos en la silla (más fácil), flexión con una mancuerna bajo la mano (más recorrido).
- Hombro anterior/lateral: press de pie, Arnold, elevación lateral, elevación frontal, pica (pies en silla = más duro).
- Hombro posterior: pájaro inclinado, pájaro tumbado boca abajo en la silla, remo con codos abiertos, "T" boca abajo.
- Tríceps: extensión tumbado, extensión tras nuca con una mancuerna, patada, fondos silla, diamante, extensión en silla.
- Dorsal: dominada (negativa → asistida → completa), remo a una mano, remo inclinado, pullover suelo, remo en plancha.
- Espalda alta/trapecio: remo con codos abiertos, pájaro, encogimientos con mancuernas, "Y" boca abajo.
- Bíceps: curl, curl martillo, curl concentrado, curl con pausa, dominada neutra.
- Cuádriceps: sentadilla goblet/frontal/lados, búlgara, zancada atrás, sentadilla con pausa, sentadilla a una pierna a la silla.
- Glúteo/isquios: peso muerto rumano (dos manos o una pierna), puente (dos piernas → una → talones en la silla),
  swing, curl nórdico asistido (pies bajo la silla), buenos días con mancuerna.
- Gemelos: elevación de talones en un escalón, a una pierna con mancuerna.
- Core: plancha (frontal, lateral, con arrastre, toque de hombro), dead bug, hollow, elevación de piernas,
  leñador, marcha con mancuerna, elevación de rodillas colgado.
- Cardio: comba, skaters, mountain climbers, swing.
