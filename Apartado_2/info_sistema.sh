#!/bin/bash

# Función para obtener la MAC (intenta usar ip link, compatible con la mayoría de Linux modernos)
obtener_mac() {
    # Busca líneas que contengan 'ether' (Ethernet/WiFi) y saca la segunda columna
    ip link show | awk '/ether/ {print $2}' | head -n 1
}

# Obtener Usuario
USUARIO=$(whoami)

# Obtener Nombre del Equipo (Hostname)
EQUIPO=$(hostname)

# Obtener Sistema Operativo
# Intentamos leer el archivo os-release para obtener el nombre completo
if [ -f /etc/os-release ]; then
    # Importamos las variables del archivo
    . /etc/os-release
    SISTEMA=$PRETTY_NAME
else
    # Fallback genérico si no existe el archivo
    SISTEMA=$(uname -sr)
fi

# Obtener MAC
MAC=$(obtener_mac)

# Si no se encuentra MAC
if [ -z "$MAC" ]; then
    MAC="No detectada (Verifique permisos o interfaz)"
fi

# Salida con toda la informacion
echo "El usuario '$USUARIO' está conectado en el equipo '$EQUIPO', ejecutando el sistema '$SISTEMA' con dirección MAC: $MAC"
