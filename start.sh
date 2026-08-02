#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

if [ ! -f .env ]; then
  echo "Error: .env not found. Copia .env.example a .env y ajusta los valores antes de continuar."
  exit 1
fi

if [ ! -d .venv ]; then
  echo "Creando entorno virtual .venv..."
  PY=""
  for CANDIDATE in python3 python py; do
    if command -v "$CANDIDATE" >/dev/null 2>&1; then
      if [ "$CANDIDATE" = "py" ]; then
        OUT=$(py -3 --version 2>&1 || true)
      else
        OUT=$($CANDIDATE --version 2>&1 || true)
      fi
      if [ $? -eq 0 ] && ! echo "$OUT" | grep -qi "Microsoft Store"; then
        PY="$CANDIDATE"
        break
      fi
    fi
  done

  if [ -z "$PY" ]; then
    echo "Error: no se encontró una instalación válida de Python 3."
    echo "En Windows instala Python 3 desde https://www.python.org/downloads/ y activa la casilla 'Add Python to PATH'."
    echo "Luego vuelve a ejecutar ./start.sh."
    exit 1
  fi

  if [ "$PY" = "py" ]; then
    py -3 -m venv .venv
  else
    "$PY" -m venv .venv
  fi
fi

if [ -f .venv/bin/python ]; then
  VENV_PY=".venv/bin/python"
elif [ -f .venv/Scripts/python.exe ]; then
  VENV_PY=".venv/Scripts/python.exe"
else
  echo "Error: no se encontró python del virtualenv."
  exit 1
fi

"$VENV_PY" -m pip install --upgrade pip setuptools wheel
"$VENV_PY" -m pip install -r requirements.txt

echo "Iniciando DevMatch..."
exec "$VENV_PY" -m uvicorn app.main:app --reload
