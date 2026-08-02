# Configuración de Supabase para DevMatch

Esta guía te lleva paso a paso para crear la base de datos en Supabase y conectar la app DevMatch.

## 1. Crear un proyecto en Supabase

1. Ve a https://app.supabase.com y crea una cuenta si no tienes.
2. Crea un nuevo proyecto.
3. Asigna un nombre y una contraseña segura para la base de datos.
4. Selecciona la región que te quede más cercana.

## 2. Obtener la cadena de conexión

1. En el dashboard del proyecto, ve a `Settings` > `Database` > `Connection string`.
2. Copia la cadena de conexión `PostgreSQL`.
3. Convierte la URL a un formato compatible con SQLAlchemy AsyncPG añadiendo `+asyncpg`:

```env
DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>:<port>/<database>
```

## 3. Configurar variables de entorno

1. En tu proyecto local, copia `.env.example` a `.env`.
2. Actualiza los valores de `DATABASE_URL` y `SECRET_KEY`:

```env
DATABASE_URL=postgresql+asyncpg://user:password@host:port/databasename
SECRET_KEY=una_clave_muy_segura_y_larga
```

## 4. Crear las tablas en Supabase

Puedes usar el SQL Editor de Supabase con este script:

```sql
create table if not exists users (
  id serial primary key,
  username text not null unique,
  email text not null unique,
  hashed_password text not null,
  is_active boolean not null default true,
  is_superuser boolean not null default false,
  created_at timestamp with time zone not null default now()
);

create table if not exists profiles (
  id serial primary key,
  user_id integer not null references users(id) on delete cascade,
  display_name text not null,
  title text,
  bio text,
  skills text,
  availability text default 'Available',
  location text,
  languages text,
  created_at timestamp with time zone default now(),
  updated_at timestamp with time zone default now()
);

create table if not exists matches (
  id serial primary key,
  user_id integer not null references users(id) on delete cascade,
  title text not null,
  description text,
  status text not null default 'active',
  score numeric default 0.0,
  created_at timestamp with time zone not null default now(),
  updated_at timestamp with time zone not null default now()
);
```

## 5. Habilitar acceso desde la app local

No necesitas abrir puertos; la conexión se hace desde tu app local al cluster de Supabase.

## 6. Ejecutar la app

Con el entorno virtual activado y las variables configuradas:

```bash
uvicorn app.main:app --reload
```

Luego abre:

```bash
http://127.0.0.1:8000
```

## 7. Verificar conexión

1. Ejecuta `http://127.0.0.1:8000/health`.
2. Deberías recibir:

```json
{"status":"ok"}
```

## 8. Notas

- Si usas Supabase, la app ya está lista para PostgreSQL mediante la variable `DATABASE_URL`.
- Si prefieres migraciones automáticas, luego puedes agregar Alembic y generar el primer `env.py`.
- En producción, asegúrate de usar `SECRET_KEY` fuerte y `DATABASE_URL` seguro.
