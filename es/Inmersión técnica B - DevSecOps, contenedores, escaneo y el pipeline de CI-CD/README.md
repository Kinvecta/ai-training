# Inmersión técnica B · DevSecOps, contenedores, escaneo y el pipeline de CI/CD

[![Ver en YouTube](https://img.shields.io/badge/ver-YouTube-red?logo=youtube&logoColor=white)](https://youtu.be/aNNY7x1pb8c) [![Diapositivas](https://img.shields.io/badge/ver-diapositivas%20%28PDF%29-8A2BE2)](slides.pdf) [![Transcripción](https://img.shields.io/badge/leer-transcripci%C3%B3n-lightgrey)](transcripci%C3%B3n/Inmersi%C3%B3n%20t%C3%A9cnica%20B%20-%20DevSecOps%2C%20contenedores%2C%20escaneo%20y%20el%20pipeline%20de%20CI-CD%20-%20transcripci%C3%B3n.txt) [![Investigación](https://img.shields.io/badge/leer-investigaci%C3%B3n%20%28ingl%C3%A9s%29-blue)](../../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/research-brief.md)

<a href="https://youtu.be/aNNY7x1pb8c"><img src="thumbnail.png" width="560" alt="Ver Inmersión técnica B: DevSecOps, contenedores, escaneo y el pipeline de CI/CD"></a>

**Duración:** 23:39 · **Para:** Quienes construyen y revisan · **Versión en aula:** 120 minutos

¿Cómo liberas software en el que de verdad puedes confiar, y sigues confiando en él? Esta inmersión técnica de la Capacitación en IA de Kinvecta recorre DevSecOps (seguridad integrada en cada etapa del desarrollo y la operación) para cargas de trabajo de IA, de principio a fin: qué es realmente un contenedor, dónde corren los contenedores, cómo endurecer una imagen, dónde viven los secretos, cómo funcionan el escaneo y el triaje, cómo la firma demuestra que publicaste la misma caja que escaneaste, cómo el pipeline de CI/CD (la línea automática que lleva el código a producción) lo hace cumplir todo y cómo los firewalls lo cercan, en ambas direcciones.

## Vas a aprender

- DevSecOps: seguridad en cada etapa, no un solo punto de control (gate) al final; llevar la seguridad al inicio (shift left) y seguir vigilando hasta producción
- Imágenes, contenedores y registries (registros de contenedores), y por qué el digest, no la etiqueta, es la identidad real
- Dónde corren los contenedores: laptop, un solo servidor, contenedores serverless, Kubernetes, el edge (borde de la red) y redes aisladas de internet (air-gapped), y quién parcha qué
- Cómo endurecer un Dockerfile: base mínima fijada, build multietapa, sin secretos y sin root
- Dónde viven los secretos: nunca en la imagen ni en el repositorio; gestores de secretos, identidad de la carga de trabajo con OIDC e inyección en tiempo de ejecución
- Los tipos de escaneo (secretos, SAST, SCA, IaC, imagen, SBOM, DAST) y las herramientas de código abierto y comerciales para cada uno
- Un triaje que funciona: primero KEV, luego EPSS, luego los críticos con corrección, y VEX para lo que no aplica
- Firma, atestaciones y control de admisión (Cosign, SBOM, procedencia, Kyverno)
- Un pipeline real de GitHub Actions, anotado, y por qué se fijan las actions por SHA de commit completo
- Firewalls y controles de red: WAF, firewalls de nube y de host, la trampa de Docker y ufw, NetworkPolicy y listas de permitidos para el tráfico de salida (egress)
- Puntos de control específicos de IA: modelos y prompts fijados, evals, escaneo de MCP y skills, y control de salida

## La regla de oro

> **Fija todas las versiones. Escanea antes de publicar. Firma y publica el mismo digest.**

Una imagen escaneada, firmada, promovida sin cambios y cercada en ambas direcciones es software en el que puedes confiar.

## Ideas clave

- DevSecOps significa seguridad en cada etapa, no un solo punto de control al final: lleva la seguridad al inicio y sigue vigilando hasta producción.
- Una imagen es una caja sellada; su digest es su identidad real, mientras que una etiqueta se puede mover. La misma imagen corre en una laptop, un servidor, contenedores serverless, Kubernetes o el edge; cambia quién parcha qué, pero tu imagen, tu código, tus llaves y tus reglas de red siguen siendo tuyos.
- Endurece la imagen (base mínima fijada por digest, build multietapa, sin root) y mantén los secretos fuera de las imágenes y los repositorios: inyéctalos en tiempo de ejecución desde un gestor de secretos. Cada paso del Dockerfile es una capa permanente, así que una llave "borrada" sigue ahí.
- Usa varios escáneres y luego haz el triaje por riesgo real: primero lo que se explota activamente (KEV), luego lo que probablemente se explotará (EPSS), luego lo crítico y alto que tiene corrección. Documenta con VEX lo que no aplica.
- Firma y atestigua el digest, verifícalo en la admisión y promueve el mismo digest de staging a producción, nunca reconstruido. Fija las actions de CI a SHAs de commit completos, porque tu escáner también es una dependencia.
- Firewalls: denegar por defecto en ambas direcciones, capa por capa. Un puerto publicado con Docker se salta ufw, y las cargas de IA solo deben llegar a la API del LLM y a los backends aprobados, con una lista de permitidos para el tráfico de salida.

## Términos clave

| Término | Qué significa |
|---|---|
| DevSecOps | Seguridad integrada en cada etapa del desarrollo y la operación, no una revisión al final |
| Imagen y contenedor | La imagen es la caja sellada con tu código y sus dependencias; el contenedor es esa imagen corriendo |
| Registry (registro de contenedores) | El almacén desde donde se publican y descargan las imágenes |
| Digest | La huella sha256 que identifica los bytes exactos de una imagen; a diferencia de la etiqueta, no se puede mover |
| Build multietapa | Un Dockerfile que compila en una etapa y copia solo lo necesario a una imagen final mínima |
| Gestor de secretos | El servicio que guarda llaves y contraseñas y las inyecta en tiempo de ejecución, para que nunca vivan en la imagen ni en el repositorio |
| SBOM | El inventario de todo lo que trae una imagen |
| CVE | El identificador de una falla conocida |
| KEV | El catálogo de vulnerabilidades que ya se están explotando; lo primero que se corrige |
| EPSS | La probabilidad de que una vulnerabilidad se explote en los próximos treinta días |
| VEX | Una nota firmada que dice que un hallazgo no te afecta, y por qué |
| Atestación y procedencia | Declaraciones firmadas sobre cómo y de dónde se construyó una imagen |
| Control de admisión | La revisión en el clúster que solo deja correr imágenes firmadas y verificadas |
| Punto de control (gate) | Una estación del pipeline que detiene la línea si encuentra un problema por encima del límite |
| Tráfico de salida (egress) | Las conexiones que salen de tu contenedor; se limitan con una lista de permitidos |

## Pruébalo

Un ejercicio de autoestudio de 20 minutos, basado en el ejercicio del video (capítulo 21:13). Las diapositivas del ejercicio están en `slides.pdf`.

1. **Encuentra los problemas (12 minutos).** Lee el Dockerfile y el pipeline del ejercicio y encuentra al menos ocho problemas. Revisa la etiqueta de la imagen base, lo que se copia adentro, dónde vive la llave y con qué usuario corre la app. Luego revisa cómo está fijada la action, el orden del push y del escaneo, y qué pasa cuando el escaneo falla. Una pista: fíjate bien en `|| true`. Nombra una corrección para cada problema.
2. **Haz el triaje (8 minutos).** Aplica la política de la diapositiva a los seis hallazgos: bloquea todo lo que esté en KEV, todo lo que tenga un EPSS de 0.1 o más, y cualquier crítico con corrección. Si todavía no hay corrección, escribe una excepción con fecha límite y un responsable. Si el código nunca se llama, escribe una nota VEX.
3. **Comprueba.** Un buen resultado: encontraste al menos ocho problemas con su corrección, y en el triaje tres hallazgos bloquean la liberación y puedes explicar por qué en cada caso.

## Pon a prueba lo aprendido

Las seis preguntas de repaso de la guía maestra. Intenta responder antes de abrir cada respuesta.

1. ¿Por qué firmar y desplegar por digest y no por etiqueta?
   <details><summary>Respuesta</summary>Una etiqueta es un rótulo que se puede mover; un digest es un hash de los bytes exactos. Garantiza que lo que se escaneó y aprobó es lo que corre.</details>
2. Se agregó una llave en un paso y se borró en el siguiente. ¿Es seguro publicar la imagen?
   <details><summary>Respuesta</summary>No. Cada paso es una capa permanente, así que la llave sigue ahí. Rótala ya, reconstruye con inyección en tiempo de ejecución o montajes de secretos de build, y agrega escaneo de secretos.</details>
3. Un escaneo muestra 40 hallazgos HIGH. ¿Qué corriges primero?
   <details><summary>Respuesta</summary>Primero KEV, luego EPSS alto, luego críticos y altos con corrección, enfocándote en lo que de verdad corre. Documenta el resto con VEX. Muchas veces una imagen base mínima más nueva es la corrección más rápida.</details>
4. Escaneo contra firma: ¿por qué necesitas ambos?
   <details><summary>Respuesta</summary>El escaneo revisa el contenido en busca de problemas conocidos; la firma demuestra la identidad y el origen, y que nada cambió. Sin firma, alguien puede cambiar la caja; sin escaneo, publicas fielmente algo vulnerable.</details>
5. ufw niega lo entrante, pero un puerto publicado con `docker run -p` sigue accesible. ¿Por qué? Da dos correcciones.
   <details><summary>Respuesta</summary>Docker publica los puertos con sus propias reglas NAT, que se saltan ufw. Enlaza el puerto a localhost detrás de un proxy inverso, o pon reglas en la cadena DOCKER-USER. Trata el grupo de seguridad de la nube como el perímetro real y prueba desde afuera con nmap.</details>
6. Secuestraron la GitHub Action de un escáner. ¿Qué dos controles limitan el daño?
   <details><summary>Respuesta</summary>Fijar las actions a SHAs de commit completos (y las imágenes de los escáneres por digest), y mantener CI con mínimo privilegio: credenciales OIDC de vida corta, permisos mínimos y rotación rápida de secretos.</details>

## Para leer más

- [Referencia de uso seguro de GitHub Actions](https://docs.github.com/es/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions), la guía oficial de GitHub en español: fijar las actions a un SHA de commit completo, permisos mínimos y OIDC
- [Políticas de red (NetworkPolicy)](https://kubernetes.io/es/docs/concepts/services-networking/network-policies/), la documentación oficial de Kubernetes en español para denegar por defecto en ambas direcciones
- [Building best practices](https://docs.docker.com/build/building/best-practices/) (en inglés), la guía oficial de Docker: imagen base fijada, build multietapa y nada de secretos en la imagen; y [Docker and ufw](https://docs.docker.com/engine/network/packet-filtering-firewalls/) (en inglés) sobre por qué un puerto publicado se salta el firewall del host
- [Cosign](https://docs.sigstore.dev/cosign/) (en inglés), la documentación de Sigstore para firmar, atestar y verificar imágenes por digest
- [Known Exploited Vulnerabilities Catalog (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (en inglés) y [EPSS](https://www.first.org/epss/) (en inglés), las dos fuentes del triaje: lo que ya se explota y lo que probablemente se explotará

## Capítulos

- 0:00 Bienvenida: una caja, confiable en todos lados
- 0:37 Lo que vas a poder hacer
- 1:05 Tres problemas que resuelve un buen pipeline
- 1:47 DevSecOps: seguridad en cada etapa
- 2:42 Imagen, contenedor, registry y digest
- 3:34 Dónde corren los contenedores
- 4:50 Endurecer la imagen
- 5:50 Lee un Dockerfile endurecido
- 7:08 Dónde viven los secretos
- 8:18 Un escáner en cada estación
- 9:20 Herramientas de escaneo por categoría
- 10:45 Triaje: corrige primero lo que ya se explota
- 11:59 Firmar, atestar y verificar
- 12:59 Herramientas de firma, registry, admisión y runtime
- 14:12 La línea de CI/CD y sus puntos de control
- 15:15 Un pipeline de GitHub Actions, anotado
- 16:24 Cuando el escáner es el ataque
- 17:20 Firewalls: denegar por defecto, en ambas direcciones
- 18:34 Capas de red y sus herramientas
- 20:04 Puntos de control específicos de IA
- 20:56 La regla de oro
- 21:13 Ejercicio: encuentra los problemas y haz el triaje
- 22:19 Pon a prueba lo aprendido
- 23:18 Cierre: constrúyelo, empácalo, publícalo

## En esta carpeta

| Archivo | Qué es |
|---|---|
| [`slides.pdf`](slides.pdf) | Las diapositivas del video, una página por diapositiva |
| [`transcripción/Inmersión técnica B - DevSecOps, contenedores, escaneo y el pipeline de CI-CD - transcripción.txt`](transcripci%C3%B3n/Inmersi%C3%B3n%20t%C3%A9cnica%20B%20-%20DevSecOps%2C%20contenedores%2C%20escaneo%20y%20el%20pipeline%20de%20CI-CD%20-%20transcripci%C3%B3n.txt) | La narración en texto, con los tiempos de cada capítulo |
| [Investigación](../../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/research-brief.md) | La investigación detrás de la sesión, con fuentes (en inglés) |

Ve la serie completa en orden en la [lista de YouTube](https://www.youtube.com/playlist?list=PLPYZqM8a_06M). [Volver al curso](../README.md) · [English version](../../Deep%20Dive%20B%20-%20DevSecOps%20Containers%2C%20Scanning%20and%20CI-CD/)
