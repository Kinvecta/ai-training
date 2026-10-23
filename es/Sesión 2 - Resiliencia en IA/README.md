# Sesión 2 · Resiliencia en IA: cambia de modelo o de proveedor sin reconstruir

[![Ver en YouTube](https://img.shields.io/badge/ver-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/U_vd79sScWU) [![Diapositivas](https://img.shields.io/badge/ver-diapositivas%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcripción](https://img.shields.io/badge/leer-transcripci%C3%B3n-lightgrey)](transcripci%C3%B3n/Sesi%C3%B3n%202%20-%20Resiliencia%20en%20IA%20-%20transcripci%C3%B3n.txt)

<a href="https://youtu.be/U_vd79sScWU"><img src="thumbnail.png" width="560" alt="Ver Sesión 2: Resiliencia en IA: cambia de modelo o de proveedor sin reconstruir"></a>

**Duración:** 9:48 · **Para:** Todos · **Versión en aula:** 90 minutos

Los modelos se retiran, los términos cambian y lo que seguridad aprueba hoy puede cambiar mañana. ¿Qué es tuyo y sobrevive a un cambio? La Sesión 2 de la Capacitación en IA de Kinvecta explica cómo volver agnóstica a tu organización: poder cambiar el modelo, o todo el proveedor, sin reconstruir tu trabajo.

## Vas a aprender

- Qué rentas (modelos, apps y arneses) y qué es tuyo
- Los cuatro niveles de cambio: versión del modelo, proveedor, endpoint y arnés (en inglés, harness)
- Los siete fundamentos que le pertenecen a tu organización, de las herramientas MCP a las evals guardadas
- Cómo cambiar de modelo se vuelve un cambio de una línea en la configuración
- Cómo escribir una skill una vez y probarla en cada arnés
- Cómo las evals detectan la deriva del modelo y la deriva del caso de uso
- La regla de oro: renta el modelo; quédate con las conexiones, el know-how y las pruebas

## La regla de oro

> **Renta el modelo. Quédate con las conexiones. Quédate con el know-how. Y quédate con las pruebas.**

Las conexiones son tus herramientas MCP y tu capa de API; el know-how, tus skills y prompts; las pruebas, tus evals guardadas.

## Ideas clave

- Ser agnóstico significa que puedes cambiar el modelo, o todo el proveedor, sin reconstruir tu trabajo.
- Hay cuatro niveles de cambio: la versión del modelo, el proveedor, el endpoint (la dirección a la que tu código manda las solicitudes) y el arnés. Cada uno cuesta más que el anterior.
- Siete fundamentos facilitan el cambio y son tuyos: herramientas MCP aprobadas, contenedores, escaneo, skills, paquetes de código, una capa de API multiproveedor y evals guardadas.
- Deja el nombre del modelo y el endpoint en la configuración, con la versión fijada, para que cambiar sea un cambio de una línea y no un proyecto.
- Una skill se escribe una vez y se prueba en cada arnés, porque los scripts, las rutas de archivos y los nombres de herramientas pueden cambiar entre arneses.
- Las evals guardadas son tus pruebas. Detectan la deriva del modelo (una versión nueva responde distinto) y la deriva del caso de uso (el negocio o los datos cambian bajo un prompt que sigue igual). Sin ellas, un cambio es una apuesta.

## Términos clave

| Término | Qué significa |
|---|---|
| Agnóstico | Que puede cambiar de modelo o proveedor sin reconstruir su trabajo |
| Dependencia del proveedor (lock-in) | Cuando cambiar de proveedor cuesta tanto que ya no es una opción real |
| Rentar o ser dueño | Rentas el modelo, las apps y los arneses; eres dueño de las conexiones, el know-how y las pruebas |
| Endpoint | La dirección a la que tu código manda las solicitudes |
| Versión fijada | El nombre exacto de la versión del modelo escrito en la configuración, para que no cambie sin que lo decidas |
| Know-how | El conocimiento práctico de tu equipo: skills y prompts |
| Evals (evaluaciones guardadas) | Pruebas guardadas que miden si el modelo sigue respondiendo bien |
| Deriva del modelo | Una versión nueva del modelo responde distinto al mismo prompt |
| Deriva del caso de uso | El negocio, los datos o los usuarios cambian mientras el prompt sigue igual |
| Manual de cambio | Los pasos para cambiar de modelo o de proveedor: prueba antes de cambiar |

## Pruébalo

Un ejercicio de autoestudio de 15 a 20 minutos, basado en el ejercicio del video (capítulo 7:54).

1. **Auditoría de dependencia (8 minutos).** Elige un flujo de trabajo que tu equipo corra cada semana con IA. Para cada uno de los siete fundamentos (herramientas MCP, contenedores, escaneo, skills, paquetes de código, capa de API, evals guardadas), marca una de tres opciones: es de tu organización, es del proveedor o falta.
2. **Simulacro de retiro (8 minutos).** Imagina que el modelo detrás de ese flujo se retira en treinta días. Responde por escrito: ¿dónde se nombra el modelo, en la configuración o en el código? ¿Qué evals probarían que el nuevo funciona? ¿Qué prompts o skills podrían necesitar cambios? ¿Quién aprueba el cambio? ¿Qué haría más fácil el siguiente cambio?
3. **Cierra (2 minutos).** Nombra tu hueco más grande. Para la mayoría de los equipos, son las evals. Si es tu caso, escribe tres casos de prueba con su resultado de referencia antes de cerrar la sesión.

## Pon a prueba lo aprendido

Las seis preguntas de repaso de la guía maestra. Intenta responder antes de abrir cada respuesta.

1. En una oración, ¿qué hace agnóstica a una organización?
   <details><summary>Respuesta</summary>Puede cambiar el modelo, o todo el proveedor, sin reconstruir su trabajo.</details>
2. Nombra cuatro de los siete fundamentos.
   <details><summary>Respuesta</summary>Cuatro de estos: herramientas MCP aprobadas, contenedores, escaneo, skills, paquetes de código, una capa de API multiproveedor, evals guardadas.</details>
3. ¿Por qué las evals guardadas importan tanto al cambiar?
   <details><summary>Respuesta</summary>Son la única evidencia de que el modelo nuevo funciona tan bien como el anterior. Sin ellas, un cambio es una apuesta.</details>
4. ¿Qué diferencia hay entre la deriva del modelo y la deriva del caso de uso?
   <details><summary>Respuesta</summary>Deriva del modelo: una versión nueva del modelo responde distinto. Deriva del caso de uso: el negocio, los datos o los usuarios cambian mientras el prompt sigue igual.</details>
5. ¿Dónde deben vivir el nombre del modelo y el endpoint?
   <details><summary>Respuesta</summary>En la configuración, con la versión fijada, no escritos en el código.</details>
6. ¿Por qué probar una skill en cada arnés si el formato es el mismo?
   <details><summary>Respuesta</summary>Los scripts, las rutas de archivos y los nombres de herramientas pueden cambiar entre arneses, así que una skill puede fallar aunque el formato sea el mismo.</details>

## Para leer más

- [Configuración](https://12factor.net/es/config), el factor III de la metodología de doce factores, en español: la configuración vive en el entorno, no en el código
- [Deprecations](https://developers.openai.com/api/docs/deprecations) (en inglés) y [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) (en inglés), dos ejemplos de cómo los proveedores anuncian el retiro de sus modelos y los plazos que dan
- [Agent Skills](https://agentskills.io/) (en inglés), el formato abierto para escribir una skill una vez y usarla en cualquier arnés compatible
- [Promptfoo](https://www.promptfoo.dev/docs/intro/) (en inglés), una herramienta de código abierto para guardar evals y correrlas contra varios modelos y proveedores
- [¿Qué es el Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro) (en inglés), el estándar abierto detrás de las conexiones que son tuyas

## Capítulos

- 0:00 Bienvenida: ¿qué es tuyo y sobrevive a un cambio?
- 0:30 Lo que vas a poder hacer
- 0:56 Por qué importa la resiliencia
- 1:25 Rentar o ser dueño
- 2:04 Cuatro niveles de cambio
- 2:44 Cuatro creencias que hay que corregir
- 3:21 Siete fundamentos, un ciclo
- 4:16 Las siete cosas que son tuyas
- 5:02 Cambia de modelo en una sola línea
- 5:44 Una skill, escrita una vez, en cada arnés
- 6:21 Las evals te dicen si un cambio funcionó
- 7:01 La regla de oro
- 7:20 Manual de cambio: prueba antes de cambiar
- 7:54 Ejercicio: auditoría de dependencia
- 8:34 Pon a prueba lo aprendido
- 9:13 Lo que sigue: Prompts seguros y verificación (Sesión 3)

## En esta carpeta

| Archivo | Qué es |
|---|---|
| [`slides.pdf`](slides.pdf) | Las diapositivas del video, una página por diapositiva |
| [`transcripción/Sesión 2 - Resiliencia en IA - transcripción.txt`](transcripci%C3%B3n/Sesi%C3%B3n%202%20-%20Resiliencia%20en%20IA%20-%20transcripci%C3%B3n.txt) | La narración en texto, con los tiempos de cada capítulo |

Ve la serie completa en orden en la [lista de YouTube](https://www.youtube.com/playlist?list=PLPYZqM8a_06M). [Volver al curso](../README.md) · [English version](../../Session%202%20-%20AI%20Resilience/)
