Programa para Introducción a los Sistemas Inteligentes 2026-1

# Requerimientos

- [x] Python >3.10
- [x] Monitor de 1920x1080
- [x] Windows o Linux (X11)
- [x] Navegador abierto y no en pantalla completa

# Instalación e inicio

1. Clonar el repositorio
```bash
git clone https://github.com/paranimias/misioneros_y_canibales.git
```

2. Crear entorno virtual y activarlo
```bash
cd misioneros_y_canibales
python -m venv .venv

.venv/Scripts/Activate.ps1 #En windows
source .venv/bin/activate #En linux
```

3. Instalar paquetes de requerimientos
```bash
pip install -r requirements.txt
```

4. Correr el programa
```bash
python __init__.py 0 # Para iniciar el juego solo
python __init__.py 1 # Para distintas condiciones iniciales
```
