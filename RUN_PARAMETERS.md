# Parámetros para poner en funcionamiento DevMatch

Este documento describe los pasos y variables necesarias para ejecutar la aplicación DevMatch localmente con la conexión a Supabase.

## 1. Activar el entorno virtual

Desde el directorio del proyecto:

```bash
cd /home/ec2-user/workshop
source .venv/bin/activate
```

## 2. Variables de entorno necesarias

Asegúrate de que el archivo `.env` exista con estas variables:

```env
DATABASE_URL=postgresql+asyncpg://postgres:O0FT28nup16RvaUz@db.snardferfmneudmclypf.supabase.co:5432/postgres
SECRET_KEY=devmatch_super_secret_key_2o9HjLqT1z6sF
```

- `DATABASE_URL`: URL de conexión a tu base de datos Supabase, con `postgresql+asyncpg://`.
- `SECRET_KEY`: clave secreta usada por la aplicación para firmar JWT internos.

## 3. Comando de ejecución

Inicia la aplicación con Uvicorn:

```bash
uvicorn app.main:app --reload
```

## 4. Verificación

Prueba que la aplicación responde correctamente:

```bash
curl http://127.0.0.1:8000/health
```

Debes recibir:

```json
{"status":"ok"}
```

## 5. Notas adicionales

- Si no existe `.env`, crea uno copiando `.env.example` y ajusta los valores.
- Si necesitas cambiar la clave secreta, reemplaza `SECRET_KEY` por otra cadena segura.
- El `public key` de Supabase no se usa en esta configuración.
