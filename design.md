# DevMatch Design Document

## Overview
DevMatch es una plataforma de emparejamiento para desarrolladores basada en lógica técnica y colaboración de código. El diseño presenta una interfaz oscura, futurista y de alta tecnología, con foco en:

- Dashboard de descubrimiento de talentos.
- Perfil de desarrollador con habilidades y estado de disponibilidad.
- Retos de programación activos con editor de código y chat colaborativo.
- Flujos de "match" que simulan una experiencia de "dating app" gamificada.
- Proceso de onboarding para definir perfil técnico.
- Login estilo terminal cibernética.

## Principales pantallas

1. **Landing / Discover**
   - Hero con mensaje central: "Connect through code. Match through logic.".
   - Botones principales: `Initiate Protocol`, `View Git Log`.
   - Secciones de pasos: Code together, Solve challenges, Reveal identity.
   - Footer de enlaces de sistema y social.

2. **Discover / Perfil de match**
   - Sidebar con navegación: Profile, Discover, Active Challenges, Settings.
   - Tarjeta principal con información de candidato: nombre, edad, rol, descripción, skills.
   - Acciones tipo swipe: rechazar, aprobar, navegar.

3. **Active Challenges**
   - Layout dividido: editor de código a la izquierda y chat de sesión a la derecha.
   - Indicadores de sesión, sugerencias, score de match.
   - Botón `Submit Solved` y cronómetro.

4. **Match Reveal / Success**
   - Pantalla central de éxito con círculo y estado de sincronización.
   - Cards de detalle: nivel de desafío, eficiencia, stack compartido.
   - Botones de acción: `Initiate Chat`, `View Solution`.

5. **Onboarding / Profile Setup**
   - Formulario paso a paso con barra de progreso.
   - Selección de arquetipo y texto descriptivo.
   - Campos de perfil técnico y bio estilo terminal.

6. **Auth / Login**
   - Pantalla de autenticación estilo consola.
   - Campos: username/root, access_key.
   - Botón `Authenticate Session`.

## Estilo visual

- Paleta principal: azul cian neón, púrpura, negro y gris azulado.
- Tipografía moderna y legible: headings en tamaño grande con contraste.
- Bordes redondeados suaves y cards con glow interno sutil.
- Animaciones suaves en hover y foco.
- Uso de iconografía tech y elementos de terminal.

## Arquitectura propuesta

- Backend con FastAPI + Jinja2 para páginas SSR.
- Base de datos PostgreSQL/Supabase para escalabilidad.
- SQLAlchemy como ORM y Alembic para migraciones.
- Autenticación con JWT y sesiones seguras.
- Modularización por capas: `models`, `schemas`, `routes`, `services`, `templates`, `static`.

## Entidades clave

- `User`: credenciales y estado.
- `Profile`: información pública del desarrollador.
- `Match`: lógica de emparejamiento y estado del desafío.
- `Challenge` (futuro): código, estado, tiempo.

## Observaciones

- Se buscará mantener el estilo visual del diseño lo más cercano posible con CSS moderno.
- El backend ofrecerá CRUD y protección de rutas desde el inicio.
- La integración con Supabase será compatible configurando `DATABASE_URL` para PostgreSQL.
