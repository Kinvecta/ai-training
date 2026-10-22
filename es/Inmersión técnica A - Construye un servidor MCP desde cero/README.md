# Inmersión técnica A · Construye un servidor MCP desde cero

[![Ver en YouTube](https://img.shields.io/badge/ver-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/1mkqzgpIr80) [![Diapositivas](https://img.shields.io/badge/ver-diapositivas%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcripción](https://img.shields.io/badge/leer-transcripci%C3%B3n-lightgrey)](transcripci%C3%B3n/Inmersi%C3%B3n%20t%C3%A9cnica%20A%20-%20Construye%20un%20servidor%20MCP%20desde%20cero%20-%20transcripci%C3%B3n.txt) [![Laboratorio](https://img.shields.io/badge/abrir-laboratorio-orange)](../../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/lab/)

<a href="https://youtu.be/1mkqzgpIr80"><img src="thumbnail.png" width="560" alt="Ver Inmersión técnica A: construye un servidor MCP desde cero"></a>

**Duración:** 25:21 · **Para:** Quienes desarrollan · **Versión en aula:** 120 minutos

El Model Context Protocol (MCP) cambió en julio de 2026, y la mayoría de los tutoriales ya quedaron viejos. En esta inmersión técnica de la Capacitación en IA de Kinvecta construimos desde cero un servidor MCP pequeño, ticket-desk, con la especificación actual y los kits de la versión dos. Y lo construimos con mentalidad DevSecOps: seguridad en cada paso, no al final.

## Vas a aprender

- Cómo funciona MCP: host, cliente y servidor, y las fronteras de confianza entre ellos
- Cómo se ve hoy una solicitud en el protocolo (especificación 2026-07-28: sin saludo de arranque, sin sesiones, server/discover)
- Herramientas, recursos y prompts, y quién controla cada uno
- La anatomía de la definición de una herramienta, y por qué las descripciones se revisan como código
- Una herramienta de solo lectura en Python, donde las anotaciones de tipo son el esquema
- Una acción que primero le pregunta a una persona, y el bug del rechazo y la cancelación que debes evitar (Python y TypeScript)
- stdio vs. Streamable HTTP, y dónde debe correr un servidor: local, remoto o en un contenedor detrás de un firewall
- Pruebas con el MCP Inspector, y un snapshot de la lista de herramientas en CI
- Cómo conectarlo a Claude Desktop, Claude Code y VS Code
- Inicio de sesión remoto con OAuth 2.1, y por qué el token passthrough está prohibido
- Amenazas reales (envenenamiento de herramientas, rug pull, inyección en los resultados, paquetes maliciosos, DNS rebinding) y el control en el servidor para cada una
- Un ciclo DevSecOps para toda la vida de un servidor

## La regla de oro

> **Pocas herramientas, esquemas estrictos. Una persona confirma cada acción. Valida tu propio token. Nunca lo reenvíes.**

## Capítulos

- 0:00 Bienvenida: un servidor en el que puedas confiar
- 0:44 Lo que vas a poder hacer
- 1:28 Por qué construirlo con cuidado
- 2:33 Host, cliente y servidor
- 3:34 El panorama completo: cuatro capas, tres fronteras de confianza
- 4:32 Herramientas, recursos y prompts
- 5:28 Anatomía de la definición de una herramienta
- 6:17 Cómo se ve hoy una solicitud en el protocolo
- 7:23 Preparación con los kits actuales
- 8:31 Python: una herramienta de solo lectura en 16 líneas
- 10:08 Python: una acción que primero le pregunta a una persona
- 11:18 Cómo pregunta el servidor: solicitudes de varias vueltas
- 12:28 TypeScript: la corrección del rechazo
- 13:35 stdio vs. Streamable HTTP
- 15:01 Dónde corre un servidor MCP
- 15:58 Constrúyelo, inspecciónalo, rómpelo y corrígelo
- 17:03 Conéctalo a un host
- 18:04 OAuth 2.1, y por qué no hay token passthrough
- 19:35 Amenazas y controles en el servidor
- 21:07 DevSecOps para un servidor MCP
- 22:15 La regla de oro
- 22:33 Laboratorio práctico
- 24:03 Pon a prueba lo aprendido
- 24:59 Lo que sigue: contenedores, escaneo y el pipeline de CI/CD (Inmersión técnica B)

## En esta carpeta

| Archivo | Qué es |
|---|---|
| [`slides.pdf`](slides.pdf) | Las diapositivas del video, una página por diapositiva |
| [`transcripción/Inmersión técnica A - Construye un servidor MCP desde cero - transcripción.txt`](transcripci%C3%B3n/Inmersi%C3%B3n%20t%C3%A9cnica%20A%20-%20Construye%20un%20servidor%20MCP%20desde%20cero%20-%20transcripci%C3%B3n.txt) | La narración en texto, con los tiempos de cada capítulo |
| [Laboratorio](../../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/lab/) | El servidor MCP ticket-desk en Python y TypeScript, con pruebas (código y comentarios en inglés) |

Ve la serie completa en orden en la [lista de YouTube](https://www.youtube.com/playlist?list=PLPYZqM8a_06M). [Volver al curso](../README.md) · [English version](../../Deep%20Dive%20A%20-%20Build%20an%20MCP%20Server%20from%20Scratch/)
