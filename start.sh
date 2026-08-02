#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

if [ ! -f .env ]; then
  echo "Error: .env not found. Copia .env.example a .env y ajusta los valores antes de continuar."
  exit 1
fi

if [ ! -d .venv ]; then
  echo "Creando entorno virtual .venv..."
  python3 -m venv .venv
  . .venv/bin/activate
  pip install --upgrade pip setuptools wheel
  pip install -r requirements.txt
else
  . .venv/bin/activate
fi

echo "Iniciando DevMatch..."
exec uvicorn app.main:app --reload
