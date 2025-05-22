# 🛡️ Proyecto 1: Cifrados de Flujo – Desafíos en Seguridad

Este repositorio contiene la solución completa del **Proyecto 1** del curso de seguridad informática, centrado en el análisis, ruptura y comprensión de **cifrados de flujo** mediante retos prácticos inspirados en el universo de *One Piece*.

## 📜 Descripción General

El proyecto consistió en resolver cuatro retos de tipo *Capture The Flag (CTF)*, donde se aplicaron distintos algoritmos de cifrado y técnicas criptográficas para descifrar mensajes ocultos. Cada reto involucraba la obtención de una `flag` cifrada y un fragmento narrativo (poneglyph) oculto en los metadatos de imágenes.

### 🧩 Retos incluidos:

| Reto     | Algoritmo         | Técnicas aplicadas                              |
|----------|-------------------|--------------------------------------------------|
| Luffy    | XOR clásico        | Análisis de frecuencia y XOR con clave directa  |
| Zoro     | RC4               | Implementación de RC4 puro y descifrado manual  |
| Usopp    | PRNG personalizado| Fuerza bruta sobre semilla y PRNG débil         |
| Nami     | ChaCha20          | Uso de cifrado moderno con clave y nonce        |

---

## 📁 Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| [`flags.txt`](https://github.com/bsicay/Proyecto1_Cifrados/blob/main/flags.txt) | Contiene todas las flags encontradas en los 4 retos |
| [`poneglyphs.txt`](https://github.com/bsicay/Proyecto1_Cifrados/blob/main/poneglyphs.txt) | Contiene todos los textos extraídos de los metadatos de imágenes |
| [`proyecto1_reporte.pdf`](https://github.com/bsicay/Proyecto1_Cifrados/blob/main/proyecto1_reporte.pdf) | Reporte técnico completo con análisis, código y evidencias |

---

## 🚀 Tecnologías utilizadas

- Python 3.x
- Librerías: `Pillow`, `piexif`, `pycryptodome`
- Docker (entorno aislado por personaje)
- Línea de comandos de Linux

---

## 🧠 Aprendizajes clave

- Importancia del uso adecuado de claves y nonces en cifrados de flujo.
- Identificación de vulnerabilidades criptográficas comunes.
- Implementación de algoritmos como RC4 y ChaCha20 desde un enfoque práctico.
- Extracción de datos ocultos (esteganografía) desde metadatos EXIF en imágenes.

---

## 👨‍💻 Autor

**Brandon Sicay**  
Estudiante de Ingeniería en Ciencias de la Computación  
Universidad del Valle de Guatemala

---

## 📬 Contacto

- GitHub: [bsicay](https://github.com/bsicay)
- Correo: [sic21757@uvg.edu.gt] 

---

¡Gracias por visitar el repositorio!
