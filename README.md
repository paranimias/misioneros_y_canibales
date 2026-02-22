Programa para Introducción a los Sistemas Inteligentes 2026-1

# Requerimientos

- [x] Python >3.10
- [x] Monitor de 1920x1080
- [x] Windows o Linux (X11)

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
pip freeze > requirements.txt
```

4. Correr el programa
```bash
python __init__.py
```