# DevMatch

DevMatch es una aplicación web Full Stack construida con FastAPI, Jinja2 y SQLAlchemy. Está diseñada para ofrecer una experiencia tipo plataforma de emparejamiento de desarrolladores con un diseño oscuro futurista y flujos de interacción tipo "match".

## Características

- Backend en FastAPI
- Plantillas HTML con Jinja2
- CSS responsive y estilo inspirado en el diseño DevMatch
- Autenticación JWT
- Modelos de usuario, perfil y match
- Rutas principales: `/`, `/login`, `/dashboard`, `/discover`, `/matches`, `/profile`
- Compatible con PostgreSQL / Supabase y SQLite local

## Requisitos previos

- Python 3.12+
- `pip` instalado
- PostgreSQL o Supabase (opcional)

## Instalación

1. Clona el repositorio o copia los archivos al directorio del proyecto.
2. Crea un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Copia `.env.example` a `.env` y ajusta variables según tu entorno:

```bash
cp .env.example .env
```

5. Si usas PostgreSQL/Supabase, configura `DATABASE_URL` con tu cadena de conexión:

```env
DATABASE_URL=postgresql+asyncpg://user:password@host:port/databasename
SECRET_KEY=<una-clave-fuerte>
```

6. Para desarrollo local con SQLite, puedes dejar la configuración por defecto en `.env`.

## Ejecución

1. Activa el entorno virtual:

```bash
cd /home/ec2-user/workshop
source .venv/bin/activate
```

2. Asegúrate de que el archivo `.env` exista con estas variables:

```env
DATABASE_URL=postgresql+asyncpg://postgres:O0FT28nup16RvaUz@db.snardferfmneudmclypf.supabase.co:5432/postgres
SECRET_KEY=devmatch_super_secret_key_2o9HjLqT1z6sF
```

- `DATABASE_URL`: URL de conexión a tu base de datos Supabase.
- `SECRET_KEY`: clave secreta usada por la aplicación para firmar JWT internos.

3. Inicia la app con Uvicorn:

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

4. Verifica la conexión:

```bash
curl http://127.0.0.1:8000/health
```

Debes recibir:

```json
{"status":"ok"}
```

## Rutas principales

- `/` → Landing page
- `/login` → Página de autenticación
- `/dashboard` → Tablero principal
- `/discover` → Página Discover
- `/matches` → Pantalla de match
- `/profile` → Perfil del usuario

## Configuración de la base de datos

La app crea las tablas automáticamente en el arranque.

### Usar Supabase / PostgreSQL

Cambia la variable `DATABASE_URL` en `.env` a tu conexión de PostgreSQL.

### Usar SQLite local

Usa la cadena por defecto:

```env
DATABASE_URL=sqlite+aiosqlite:///./devmatch.db
```

## Testing rápido

1. Inicia el servidor.
2. Abre `http://127.0.0.1:8000`.
3. Navega a `/login`.
4. Registra usuarios mediante la API o crea un usuario manualmente en la base de datos.

## Notas

- El proyecto está pensado para continuar con CRUD y autenticación completa.
- El diseño está adaptado al estilo mostrado en las capturas.
- Para futuras mejoras, puedes añadir: un sistema real de `challenges`, registro de usuario con validación, páginas protegidas y endpoints REST completos.
