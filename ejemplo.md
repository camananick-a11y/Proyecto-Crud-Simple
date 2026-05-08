💊 Botica NovaSalud - Backend (Django + Supabase)

Sistema de gestión para la Botica NovaSalud, desarrollado con Django REST Framework y base de datos en Supabase (PostgreSQL).

📌 Tecnologías Utilizadas
🐍 Django 6+
⚡ Django REST Framework
🔐 SimpleJWT (Autenticación)
🗄️ Supabase (PostgreSQL)
🌐 CORS Headers
🧪 Python 3.10+
📊 Arquitectura del Sistema

El sistema está basado en una arquitectura REST con separación por módulos:

🔐 Autenticación y usuarios (RBAC)
👥 Clientes
💊 Medicamentos e inventario
🧾 Ventas (comprobantes y detalles)
📦 Stock en tiempo real
📊 Reportes
🗄️ Base de Datos (Supabase)
🔐 Seguridad y Usuarios
Tabla	Descripción
usuario	Usuarios del sistema (login + roles)
cargo	Roles del sistema (Admin, Vendedor, etc.)
👥 Clientes
Tabla	Descripción
cliente	Información de clientes (documentos, contacto)
💊 Inventario
Tabla	Descripción
medicamento	Catálogo principal de productos
stock_medicamento	Control de stock en tiempo real
categoria	Clasificación de medicamentos
laboratorio	Fabricantes
presentacion	Forma del medicamento
unidad	Unidad de medida
🧾 Ventas
Tabla	Descripción
comprobante	Cabecera de venta (boleta/factura)
detalle_venta	Detalle de productos vendidos
🚀 Instalación
1. Requisitos
Python 3.10+
Virtualenv
Supabase configurado
2. Clonar proyecto
cd backend
3. Entorno virtual
python -m venv venv
.\venv\Scripts\activate
4. Instalar dependencias
pip install -r requirements.txt
5. Variables de entorno (.env)
DEBUG=True
SECRET_KEY=tu_clave_secreta

SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_SECRET_KEY=tu_service_role_key

DB_URL=postgres://postgres:password@db.supabase.co:5432/postgres
6. Ejecutar servidor
python manage.py runserver
🔐 Seguridad del Sistema
🔑 Autenticación con JWT
👮 Control de acceso por roles (RBAC)
🚫 Validación de stock antes de ventas
🔒 Contraseñas encriptadas
📦 Reglas del Sistema
🧾 Ventas
Se generan boletas o facturas
El stock se descuenta automáticamente
Se registran detalles de venta
📉 Stock
Control en tiempo real
Evita ventas sin existencias
Se actualiza automáticamente
👮 Roles
Rol	Acceso
Admin	Total
Almacenero	Inventario
Vendedor	Ventas + Clientes
🧠 Características clave
✔ API REST completa
✔ Sistema de inventario funcional
✔ Ventas con detalle
✔ Reportes por fechas
✔ Top productos vendidos
✔ Alertas de stock bajo
✔ Integración con Supabase
🛠️ Notas de desarrollo
El sistema usa Django REST Framework
El stock se descuenta automáticamente al vender
Se usa JWT para autenticación segura
Las relaciones están normalizadas en PostgreSQL
🚀 Estado del proyecto

👉 🟢 Backend funcional
👉 🟢 API completa
👉 🟢 Sistema de ventas operativo
👉 🟢 Inventario conectado
👉 🟢 Listo para frontend
