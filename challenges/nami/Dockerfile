# Usamos una imagen base de Ubuntu
FROM ubuntu:22.04

# Evitar interactividad en la instalación de paquetes
# ARG DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    sudo \
    python3 \
    python3-pip \
    python3-dev \
    git \
    vim \
    nano \
    curl \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Crear un usuario "nami" y darle una contraseña
RUN useradd -ms /bin/bash nami && echo "nami:FLAG_7a9ee38e32eb180cd2db21f2a39fddd0" | chpasswd && adduser nami sudo

# Deshabilitamos el acceso directo como root para que los alumnos no inicien con permisos de administrador
RUN passwd -l root

# Establecer el directorio de trabajo
WORKDIR /home/nami

# Copiar los archivos del reto dentro del contenedor
COPY ./ONEPIECE /home/nami/ONEPIECE

# Cambiar la propiedad de los archivos al usuario nami
RUN chown -R nami:nami /home/nami

# Cambiar al usuario "nami" por defecto
USER nobody

EXPOSE 8000 
# Script de inicio
CMD ["bash"]