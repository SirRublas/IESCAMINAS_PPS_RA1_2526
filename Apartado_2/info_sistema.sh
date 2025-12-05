#!/bin/bash

# Detectar sistema operativo
SO=$(uname -s)

# Obtener usuario
if [[ "$SO" == "Linux" || "$SO" == "Darwin" ]]; then
    USUARIO=$(whoami)
    EQUIPO=$(hostname)

    # Obtener sistema operativo
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        SISTEMA=$PRETTY_NAME
    else
        SISTEMA=$(uname -sr)
    fi

    # Obtener MAC
    MAC=$(ip link show 2>/dev/null | awk '/ether/ {print $2}' | head -n 1)
    if [ -z "$MAC" ]; then
        MAC="No detectada (verifique permisos o interfaz)"
    fi

elif [[ "$SO" == *"MINGW"* || "$SO" == *"CYGWIN"* || "$SO" == *"MSYS"* ]]; then
    # Windows (Git Bash / Cygwin / MSYS)
    USUARIO=$(whoami)
    EQUIPO=$(hostname)
    SISTEMA=$(cmd.exe /c ver | tr -d '\r')
    
    # Obtener MAC desde Windows
    MAC=$(ipconfig /all | awk '/Dirección física/ {print $NF}' | head -n 1)
    if [ -z "$MAC" ]; then
        MAC="No detectada (verifique permisos o interfaz)"
    fi
else
    echo "Sistema operativo no soportado: $SO"
    exit 1
fi

# Mostrar resultado
echo "El usuario '$USUARIO' está conectado en el equipo '$EQUIPO', ejecutando el sistema '$SISTEMA' con dirección MAC: $MAC"
