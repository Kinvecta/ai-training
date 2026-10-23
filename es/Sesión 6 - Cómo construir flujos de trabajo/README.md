# Sesión 6 · Cómo construir flujos de trabajo

[![Ver en YouTube](https://img.shields.io/badge/ver-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/tPIvXhqWdog) [![Diapositivas](https://img.shields.io/badge/ver-diapositivas%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcripción](https://img.shields.io/badge/leer-transcripci%C3%B3n-lightgrey)](transcripci%C3%B3n/Sesi%C3%B3n%206%20-%20C%C3%B3mo%20construir%20flujos%20de%20trabajo%20-%20transcripci%C3%B3n.txt)

<a href="https://youtu.be/tPIvXhqWdog"><img src="thumbnail.png" width="560" alt="Ver Sesión 6: Cómo construir flujos de trabajo"></a>

**Duración:** 8:20 · **Para:** Quienes automatizan · **Versión en aula:** 90 minutos

Pegas el mismo prompt cada lunes, el flujo se rompe y nadie se da cuenta, y no te aprueban agentes. La Sesión 6 de la Capacitación en IA de Kinvecta explica cómo convertir una tarea repetida en un flujo de trabajo: una ruta fija y segura, con una revisión de cada resultado y una persona que aprueba antes de entregar.

## Vas a aprender

- La diferencia entre un chatbot, un flujo de trabajo y un agente: ¿quién elige cada paso?
- Hasta dónde puedes llegar solo con chat y una API, sin agentes
- Las seis señales de un buen primer flujo de trabajo
- La anatomía de un flujo: disparador, entradas, prompt guardado, validación, revisión humana y entrega
- Cómo la validación detecta un resultado malo antes de que se entregue
- Cómo ejecutarlo con seguridad: contenedor, lista de permitidos, registros y límites de costo
- Cómo probar y dar versión a un prompt antes de liberarlo, y cómo medir si funciona
- La regla de oro: fija la ruta, revisa cada resultado y una persona aprueba antes de entregar

## La regla de oro

> **Fija la ruta. Revisa cada resultado. Una persona aprueba antes de entregar.**

El script decide cada paso, la revisión detecta lo que está mal y nada se entrega sin aprobación.

## Ideas clave

- En un flujo de trabajo, quien lo diseña fija la ruta antes de que corra. En un chatbot la persona elige cada paso; en un agente, la IA.
- Chat más una API alcanza para la Etapa 3: automatización que funciona, en un contenedor. No necesitas agentes para empezar.
- Un buen primer flujo se repite cada semana, tiene la misma forma cada vez, hay un resultado de referencia, ya se revisa, su nivel de sensibilidad está aprobado y su tiempo se puede medir.
- Un flujo de trabajo tiene seis pasos fijos: disparador, traer las entradas, prompt guardado, validar, revisión humana y entregar. Cada paso escribe en el registro de auditoría.
- Un resultado malo se marca, nunca se pasa. Si falla la validación, la ejecución se manda a una persona y no se entrega nada.
- Una versión nueva del prompt es una liberación nueva: se prueba con casos de referencia y un caso difícil antes de salir. Luego se mide con cuatro números: tiempo ahorrado por ejecución, errores detectados en la revisión, flujos en producción y cuántos equipos reutilizan tus prompts. Primero toma la línea base de la tarea a mano.

## Términos clave

| Término | Qué significa |
|---|---|
| Flujo de trabajo | Una ruta fija de pasos que quien lo diseña decide por adelantado; el script la sigue igual en cada ejecución |
| Disparador | Lo que arranca el flujo: una hora, un correo nuevo, un archivo que llega |
| Prompt guardado | El prompt como archivo con versión y revisado, en un lugar compartido y aprobado; no escrito a mano en cada flujo |
| Validación | La revisión automática de cada resultado: formato, enlaces, destinatarios o acciones inesperados |
| Revisión humana (punto de aprobación) | El paso en el que una persona aprueba antes de que algo se entregue |
| Marcar | Detener una ejecución y mandarla a una persona en vez de dejarla pasar |
| Registro de auditoría | El registro que escribe cada paso: qué entró, qué salió y quién aprobó |
| Casos de referencia | Entradas conocidas con su resultado esperado, para probar cada versión nueva del prompt |
| Caso difícil | Una entrada diseñada para romper el flujo, como un reporte que dice "ignora tus reglas" |
| Liberación | Publicar una versión nueva del prompt o del flujo después de pasar las pruebas |
| Low-code | Herramientas que arman flujos con poco o nada de código; sirven igual que un script si llaman al modelo por la API |

## Pruébalo

Un ejercicio de autoestudio de 20 minutos, basado en el ejercicio del video (capítulo 6:27).

1. **Diséñalo (10 minutos).** Elige una tarea semanal y llena una tarjeta de flujo de trabajo: el disparador, las entradas, los pasos como prompts guardados, la validación, quién revisa y cómo se entrega. La tarjeta del reporte de estatus en `slides.pdf` es tu ejemplo.
2. **Rómpelo (8 minutos).** Corre seis escenarios contra tu diseño y, en cada uno, decide si tu flujo lo marca o lo deja pasar: cambió la plantilla de entrada; falta un reporte; el resultado trae un enlace desconocido; se actualizó la versión del modelo; un reporte dice "ignora tus reglas"; la ejecución entra en ciclo y sigue llamando al modelo.
3. **Cierra (2 minutos).** Lo que pasaría en silencio es una revisión que falta. Agrega esa validación a tu tarjeta antes de cerrar.

## Pon a prueba lo aprendido

Las seis preguntas de repaso de la guía maestra. Intenta responder antes de abrir cada respuesta.

1. ¿Quién decide los pasos en un flujo de trabajo?
   <details><summary>Respuesta</summary>Quien lo diseña, por adelantado. El script sigue la misma ruta en cada ejecución.</details>
2. ¿Qué puede construir un equipo solo con chat y una API?
   <details><summary>Respuesta</summary>Flujos con scripts o low-code que llaman al modelo por la API, con servidores MCP como pasos fijos. Eso es la Etapa 3.</details>
3. Nombra tres señales de un buen primer flujo de trabajo.
   <details><summary>Respuesta</summary>Tres de estas: se repite cada semana, tiene la misma forma cada vez, hay un resultado de referencia, ya se revisa, el nivel de sensibilidad está aprobado, el tiempo se puede medir.</details>
4. ¿Qué pasa cuando falla una revisión de validación?
   <details><summary>Respuesta</summary>La ejecución se marca y se manda a una persona. No se entrega nada.</details>
5. ¿Dónde deben vivir los prompts de un flujo de trabajo?
   <details><summary>Respuesta</summary>Como archivos guardados, con versión y revisados, en un lugar compartido y aprobado; no escritos a mano en cada flujo.</details>
6. Un reporte en las entradas dice "ignora tus reglas". ¿Qué dos partes del flujo impiden que eso se entregue?
   <details><summary>Respuesta</summary>La revisión de validación, que marca enlaces, destinatarios o acciones inesperados, y el punto de aprobación humana. El caso difícil del conjunto de prueba también lo detecta antes de la liberación.</details>

## Para leer más

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (en inglés), la distinción entre flujos de trabajo (rutas de código fijas) y agentes, y por qué conviene empezar por lo más simple
- [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) (en inglés), la guía de OWASP con validación de salida, mínimo privilegio y aprobación humana para acciones de alto impacto
- [Promptfoo](https://www.promptfoo.dev/docs/intro/) (en inglés), una herramienta de código abierto para correr casos de referencia contra cada versión nueva de un prompt
- [Top 10 2025 de riesgos y mitigaciones para LLMs y aplicaciones de IA generativa](https://genai.owasp.org/resource/top-10-2025-de-riesgos-y-mitigaciones-para-llms-y-aplicaciones-de-ia-generativa/), la traducción oficial de OWASP al español; mira LLM05 (manejo inadecuado de la salida)

## Capítulos

- 0:00 Bienvenida: tres lunes, una ruta fija
- 0:38 Lo que vas a poder hacer
- 1:03 Por qué importa: tres quejas comunes
- 1:34 ¿Quién elige cada paso? Chatbot, flujo y agente
- 2:18 Hasta dónde puedes subir con lo que tienes hoy
- 2:58 Elige tu primer flujo de trabajo
- 3:26 Anatomía de un flujo de trabajo
- 4:14 Validación: revisa cada resultado
- 4:49 Ejecución segura: sellado, registrado y con límites
- 5:22 Antes de liberar: pruébalo y dale versión
- 5:55 Mídelo: cuatro números
- 6:11 La regla de oro
- 6:27 Ejercicio: diséñalo y luego rómpelo
- 7:12 Pon a prueba lo aprendido
- 7:55 Lo que sigue: Herramientas, MCP e inyección de prompts (Sesión 7)

## En esta carpeta

| Archivo | Qué es |
|---|---|
| [`slides.pdf`](slides.pdf) | Las diapositivas del video, una página por diapositiva |
| [`transcripción/Sesión 6 - Cómo construir flujos de trabajo - transcripción.txt`](transcripci%C3%B3n/Sesi%C3%B3n%206%20-%20C%C3%B3mo%20construir%20flujos%20de%20trabajo%20-%20transcripci%C3%B3n.txt) | La narración en texto, con los tiempos de cada capítulo |

Ve la serie completa en orden en la [lista de YouTube](https://www.youtube.com/playlist?list=PLPYZqM8a_06M). [Volver al curso](../README.md) · [English version](../../Session%206%20-%20Building%20Workflows/)
