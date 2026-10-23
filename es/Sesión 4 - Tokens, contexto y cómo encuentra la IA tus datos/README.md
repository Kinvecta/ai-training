# Sesión 4 · Tokens, contexto y cómo encuentra la IA tus datos

[![Ver en YouTube](https://img.shields.io/badge/ver-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/_XREIO0OWW0) [![Diapositivas](https://img.shields.io/badge/ver-diapositivas%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcripción](https://img.shields.io/badge/leer-transcripci%C3%B3n-lightgrey)](transcripci%C3%B3n/Sesi%C3%B3n%204%20-%20Tokens%2C%20contexto%20y%20c%C3%B3mo%20encuentra%20la%20IA%20tus%20datos%20-%20transcripci%C3%B3n.txt)

<a href="https://youtu.be/_XREIO0OWW0"><img src="thumbnail.png" width="560" alt="Ver Sesión 4: Tokens, contexto y cómo encuentra la IA tus datos"></a>

**Duración:** 8:17 · **Para:** Todos · **Versión en aula:** 90 minutos

¿Por qué te sorprendió la factura de la IA? ¿Por qué se le olvidó lo que dijiste? ¿Por qué no encontró la tabla? Las tres quejas tienen la misma causa: lo que el modelo puede ver. La Sesión 4 de la Capacitación en IA de Kinvecta explica los tokens (los pedazos de texto que el modelo lee y escribe), la ventana de contexto y las distintas formas en que las herramientas de IA obtienen tus datos.

## Vas a aprender

- Qué es un token y por qué los códigos y las cifras cuestan más
- Los tipos de tokens (entrada, salida, razonamiento, caché, imagen, herramientas y embedding) y cuánto cuesta cada uno
- Qué llena la ventana de contexto y por qué el caché abarata las instrucciones que no cambian
- Por qué los chats largos cuestan más en cada turno
- Cómo encuentra la IA tus datos: búsqueda semántica, por palabras clave, agéntica, consultas estructuradas y recuperación multimodal
- Cómo elegir el buscador según los datos, y por qué un índice de búsqueda es un tema de seguridad
- La regla de oro: manda menos, guarda en caché lo que no cambia y usa el buscador correcto

## La regla de oro

> **Manda menos. Guarda en caché lo que no cambia. Usa el buscador correcto.**

El modelo solo ve lo que le mandas y lo que le regresan los buscadores.

## Ideas clave

- Un token son más o menos cuatro caracteres, unas tres cuartas partes de una palabra en inglés. Los códigos y las cifras usan más, y cada proveedor cuenta distinto.
- La ventana de contexto es un solo presupuesto fijo que comparte todo: instrucciones, herramientas, historial, documentos, la pregunta y la respuesta. Lo que mandas cuesta más que lo que recibes.
- Los chats largos salen más caros en cada turno porque se reenvía toda la conversación. Empieza un chat nuevo cuando cambie el tema.
- El caché abarata el inicio que no cambia: un prefijo estable con las instrucciones, las definiciones de herramientas y los documentos de referencia.
- El modelo solo ve lo que le regresan los buscadores. Hay seis formas de obtener datos: todo en el contexto, búsqueda semántica, búsqueda por palabras clave, búsqueda agéntica, consultas estructuradas y recuperación multimodal. Elige según el dato, no según la moda.
- Un índice de búsqueda es una copia de tus datos, muchas veces guardada en otro lado. Necesita las mismas reglas de acceso y aprobaciones que la fuente.

## Términos clave

| Término | Qué significa |
|---|---|
| Token | Un pedazo de texto que el modelo lee y escribe; más o menos tres cuartas partes de una palabra en inglés |
| Ventana de contexto | El presupuesto fijo de tokens que comparten instrucciones, herramientas, historial, documentos, pregunta y respuesta |
| Prompt de sistema | Las instrucciones que el arnés (en inglés, harness) agrega a cada solicitud antes de tu pregunta |
| Caché (guardar en caché) | Reutilizar el prefijo que no cambia entre solicitudes para que cueste menos; en México se dice "el caché" |
| Tokens de razonamiento | Los tokens que el modelo gasta pensando antes de responder; también se cobran |
| Embedding | Una representación numérica del significado de un texto; es lo que usa la búsqueda semántica |
| Búsqueda semántica | Encuentra pasajes por significado, aunque no usen las mismas palabras |
| Búsqueda por palabras clave | Encuentra coincidencias exactas: números de ticket, nombres, códigos |
| Consulta estructurada | Una pregunta a una base de datos o a una hoja de cálculo; la respuesta correcta para sumas y totales |
| RAG (generación aumentada por recuperación) | El patrón de buscar primero y mandarle al modelo solo los pasajes que encontró |
| Índice de búsqueda | Una copia de tus datos preparada para buscar; necesita las mismas reglas de acceso que la fuente |

## Pruébalo

Un ejercicio de autoestudio de 15 minutos, basado en el ejercicio del video (capítulo 6:40).

1. **Cuéntalo (7 minutos).** Pega uno de tus propios prompts, que no sea sensible, en un contador de tokens aprobado (casi todos los proveedores publican uno). Anota los tokens de entrada y de salida. Multiplica por cuántas veces se corre al mes. Luego pregúntate: ¿cuánto ahorraría un prompt más corto, o el caché del prefijo que no cambia?
2. **Encuéntralo (6 minutos).** Para seis preguntas reales, elige el buscador correcto (todo en el contexto, semántica, palabras clave, agéntica, consulta estructurada o recuperación multimodal): una política de trabajo remoto; un número de ticket; el gasto total por proveedor; una diapositiva del organigrama; la lógica de reintentos en tu código; y un reporte de tres páginas.
3. **Cierra (2 minutos).** Si elegiste búsqueda semántica para el gasto total, piénsalo otra vez: los totales salen de una consulta estructurada, no de pasajes parecidos.

## Pon a prueba lo aprendido

Las seis preguntas de repaso de la guía maestra. Intenta responder antes de abrir cada respuesta.

1. ¿Más o menos cuánto texto es un token?
   <details><summary>Respuesta</summary>Unos cuatro caracteres, o tres cuartas partes de una palabra en inglés. Los códigos y las cifras usan más.</details>
2. ¿Por qué los chats largos cuestan más en cada turno?
   <details><summary>Respuesta</summary>Cada turno reenvía el prompt de sistema y todo el historial.</details>
3. ¿Qué comparte la ventana de contexto?
   <details><summary>Respuesta</summary>Todo lo que se manda y la respuesta: instrucciones, herramientas, historial, documentos, la pregunta y la salida.</details>
4. ¿Qué abarata el caché?
   <details><summary>Respuesta</summary>Un prefijo estable que se repite: instrucciones, definiciones de herramientas, documentos de referencia.</details>
5. Menciona tres formas en que la IA obtiene datos.
   <details><summary>Respuesta</summary>Tres de estas: todo en el contexto, búsqueda semántica, búsqueda por palabras clave, búsqueda agéntica, consultas estructuradas, recuperación multimodal.</details>
6. ¿Por qué un índice de búsqueda es un tema de seguridad?
   <details><summary>Respuesta</summary>Es una copia de los datos, muchas veces guardada en otro lado, así que necesita las mismas reglas de acceso y aprobaciones que la fuente.</details>

## Para leer más

- [Comprender y contar tokens](https://ai.google.dev/gemini-api/docs/tokens?hl=es-419), la explicación de Google en español: qué es un token, cuántos caracteres son y cómo contarlos antes de mandar una solicitud
- [Introducción a los modelos de lenguaje grandes](https://developers.google.com/machine-learning/crash-course/llm?hl=es-419), módulo en español sobre tokens y contexto en los modelos de lenguaje
- [Generación aumentada por recuperación (RAG)](https://learn.microsoft.com/es-es/azure/search/retrieval-augmented-generation-overview), la descripción de Microsoft Learn en español del patrón de buscar primero y mandar solo lo encontrado
- [Top 10 2025 de riesgos y mitigaciones para LLMs y aplicaciones de IA generativa](https://genai.owasp.org/resource/top-10-2025-de-riesgos-y-mitigaciones-para-llms-y-aplicaciones-de-ia-generativa/), la traducción oficial de OWASP al español; mira LLM08 (debilidades de vectores y embeddings) y LLM10 (consumo sin límites)

## Capítulos

- 0:00 Bienvenida: ¿qué puede ver el modelo?
- 0:34 Lo que vas a poder hacer
- 0:57 Tres quejas, una sola causa
- 1:24 Qué es un token
- 2:01 Tipos de tokens
- 2:37 La ventana de contexto: un solo presupuesto
- 3:20 Por qué los chats largos cuestan más
- 3:52 Seis razones por las que importan los tokens
- 4:26 Cómo encuentra la IA tus datos
- 5:18 Seis formas en que la IA obtiene datos
- 5:59 Elige el buscador según los datos
- 6:27 La regla de oro
- 6:40 Ejercicio: cuéntalo y encuéntralo
- 7:20 Pon a prueba lo aprendido
- 7:53 Lo que sigue: APIs, endpoints y contenedores (Sesión 5)

## En esta carpeta

| Archivo | Qué es |
|---|---|
| [`slides.pdf`](slides.pdf) | Las diapositivas del video, una página por diapositiva |
| [`transcripción/Sesión 4 - Tokens, contexto y cómo encuentra la IA tus datos - transcripción.txt`](transcripci%C3%B3n/Sesi%C3%B3n%204%20-%20Tokens%2C%20contexto%20y%20c%C3%B3mo%20encuentra%20la%20IA%20tus%20datos%20-%20transcripci%C3%B3n.txt) | La narración en texto, con los tiempos de cada capítulo |

Ve la serie completa en orden en la [lista de YouTube](https://www.youtube.com/playlist?list=PLPYZqM8a_06M). [Volver al curso](../README.md) · [English version](../../Session%204%20-%20Tokens%2C%20Context%20and%20How%20AI%20Finds%20Your%20Data/)
