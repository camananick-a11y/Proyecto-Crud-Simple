# 💊 Botica NovaSalud - Backend (Django + Supabase)

Sistema de gestión para la Botica NovaSalud, desarrollado con Django REST Framework y base de datos en Supabase (PostgreSQL).

## 📌 Tecnologías Utilizadas

🐍 Django 6+,
⚡ Django REST Framework,
🔐 SimpleJWT (Autenticación),
🗄️ Supabase (PostgreSQL),
🌐 CORS Headers,
🧪 Python 3.10+

---

## 📊 Estructura de la Base de Datos en Supabase

El sistema está sincronizado con las siguientes tablas en el esquema `public` de Supabase. Todas las tablas incluyen campos de auditoría como `created_at`.

### 🔐 Seguridad y Usuarios
| Tabla | Descripción | Columnas Clave |
| :--- | :--- | :--- |
| **`usuario`** | Almacena al personal de la botica. Soporta login por `usuario` y contraseñas encriptadas. | `id_usuario`, `usuario`, `password`, `nombre`, `last_login`, `id_cargo` |
| **`cargo`** | Define los roles y permisos del sistema (Admin, Vendedor, etc.). | `id_cargo`, `nombre` |

### 👥 Clientes
| Tabla | Descripción | Columnas Clave |
| :--- | :--- | :--- |
| **`cliente`** | Base de datos de clientes con información de contacto y documentos. | `id_cliente`, `nombre`, `tipo_documento`, `numero_documento`, `correo`, `telefono` |

### 💊 Inventario y Medicamentos
| Tabla | Descripción | Columnas Clave |
| :--- | :--- | :--- |
| **`medicamento`** | Catálogo principal de productos con precios y relaciones. | `id_medicamento`, `nombre`, `precio`, `id_laboratorio`, `id_categoria`, `id_presentacion`, `id_unidad` |
| **`stock_medicamento`** | Control de existencias en tiempo real por cada medicamento. | `id_stock`, `id_medicamento`, `cantidad` |
| **`categoria`** | Clasificación de productos (Analgésicos, Antibióticos, etc.). | `id_categoria`, `nombre` |
| **`laboratorio`** | Fabricantes de los medicamentos. | `id_laboratorio`, `nombre` |
| **`presentacion`** | Forma del medicamento (Tabletas, Jarabe, etc.). | `id_presentacion`, `nombre` |
| **`unidad`** | Unidades de medida (Unidad, Caja, Blíster). | `id_unidad`, `nombre` |

### 🧾 Ventas
| Tabla | Descripción | Columnas Clave |
| :--- | :--- | :--- |
| **`comprobante`** | Cabecera de la venta (Boleta/Factura). Registra el total y el cliente. | `id_comprobante`, `serie`, `tipo`, `Fecha`, `total`, `id_cliente`, `id_usuario` |
| **`detalle_venta`** | Detalle de los productos vendidos en cada comprobante. | `id_detalle`, `id_comprobante`, `id_medicamento`, `cantidad`, `precio_unitario`, `subtotal` |

---

## 🚀 Inicio Rápido

### 1. Requisitos
- Python 3.10+
- Virtualenv
- Cuenta en Supabase

### 2. Configuración del Entorno
Crea un archivo `.env` en la carpeta `backend/` con tus credenciales:
```env
DEBUG=True
SECRET_KEY=tu_clave_secreta
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_SECRET_KEY=tu_service_role_key
DB_URL=postgres://postgres:password@db.supabase.co:5432/postgres
```

### 3. Instalación
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Ejecución
```bash
python manage.py runserver
```

---

## 🛠️ Tecnologías Utilizadas
- **Django 6.0.5**: Framework principal.
- **Django REST Framework**: Creación de la API.
- **SimpleJWT**: Autenticación segura por tokens.
- **Supabase**: Base de datos PostgreSQL gestionada.
- **CORS Headers**: Para conexión segura con el Frontend.

---

## 📝 Notas de Desarrollo
- El sistema cuenta con **Control de Acceso Basado en Roles (RBAC)**.
- El stock de medicamentos se descuenta **automáticamente** al realizar una venta.
- Se han implementado validaciones de stock para prevenir ventas sin existencias.
