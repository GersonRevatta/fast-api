# README

## **Estructura del Proyecto**

El proyecto está diseñado siguiendo principios de **Arquitectura Hexagonal**, **CQRS**, y **Bundle-contexts**, con el objetivo de garantizar independencia del dominio, modularidad y escalabilidad. La estructura del código es la siguiente:

```
my_project/
  app/
    api/
      v1/
        endpoints/
          user.py  # Endpoints para el contexto de usuarios
    core/
      config.py    # Configuración general del proyecto
    database.py    # Configuración de la base de datos
    init_db.py     # Inicialización de la base de datos
    main.py        # Punto de entrada de la aplicación
    models/
      user.py      # Modelos de la base de datos
    schemas/
      user.py      # Esquemas de validación (Pydantic)
    crud/
      user.py      # Lógica CRUD relacionada con usuarios
  consumers/
    user_consumer.py # Publicación de mensajes a RabbitMQ
  tests/           # Pruebas unitarias e integrales
  Dockerfile       # Configuración para construir la imagen Docker
  docker-compose.yml # Configuración de servicios Docker
  requirements.txt # Dependencias del proyecto
```

### **Contextos Modulares**
- **Usuarios (User)**: Manejo de la lógica relacionada con la creación y consulta de usuarios.
- **Infraestructura**: Manejo de la base de datos y el sistema de mensajería.
- **API**: Exposición de endpoints REST.

## **Cómo Ejecutar el Proyecto**

### **Prerrequisitos**
1. Docker y Docker Compose instalados.
2. Python 3.10 o superior (si no usas Docker).

### **Configuración Inicial**
1. Clona este repositorio:
   ```bash
   git clone git@github.com:GersonRevatta/fast-api.git
   cd project
   ```

2. Configura las variables de entorno en un archivo `.env` (opcional, usa valores predeterminados si no lo configuras):
   ```env
   DATABASE_URL=sqlite:///./app.db
   RABBITMQ_URL=amqp://guest:guest@localhost:5672/
   ```

### **Ejecutar con Docker**
1. Construye y levanta los servicios:
   ```bash
   docker-compose up --build
   ```
2. La API estará disponible en: [http://localhost:8000](http://localhost:8000)

### **Ejecutar Localmente (sin Docker)**
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicializa la base de datos:
   ```bash
   python app/init_db.py
   ```
3. Ejecuta el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

## **Cómo Ejecutar las Pruebas**

### **Pruebas Unitarias e Integrales**
1. Asegúrate de tener las dependencias de pruebas instaladas:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta todas las pruebas:
   ```bash
   pytest tests/
   ```
3. Generar reporte de cobertura:
   ```bash
   pytest --cov=app tests/
   ```
   
## **Decisiones Arquitectónicas**

### **1. Arquitectura Hexagonal**
- **Independencia del dominio**:
  - Los modelos (`app/models/user.py`) y esquemas (`app/schemas/user.py`) son independientes de la infraestructura.
  - Las dependencias externas (bases de datos, RabbitMQ) están encapsuladas en adaptadores específicos.
- **Puertos y Adaptadores**:
  - Los endpoints REST (`app/api/v1/endpoints/user.py`) actúan como puertos.
  - La base de datos y RabbitMQ están implementados como adaptadores en `app/database.py` y `consumers/user_consumer.py`.

### **2. CQRS (Command Query Responsibility Segregation)**
- Las operaciones de lectura y escritura están separadas:
  - **Comandos**: `POST /api/v1/users/` maneja la creación de usuarios y publica eventos en RabbitMQ.
  - **Consultas**: `GET /api/v1/users/{user_id}` devuelve información de un usuario directamente desde el modelo de datos.
- RabbitMQ se utiliza para manejar eventos de comandos y facilitar la escalabilidad del sistema.

### **3. Bundle-contexts**
- El código está organizado para agrupar lógicamente los componentes relacionados con usuarios.
- Plan de extensión para incluir otros contextos como `auth` o `products` siguiendo la misma estructura modular.

### **4. Escalabilidad y Modularidad**
- La estructura permite añadir nuevos contextos de manera sencilla al agregar nuevas carpetas (`auth/`, `products/`) con dominios, aplicaciones e infraestructuras independientes.

### **5. Inyección de Dependencias**
- FastAPI facilita la inyección de dependencias con `Depends`, utilizado para manejar sesiones de base de datos (`get_db`).
- Posibilidad de integrar `Dependency Injector` para inyección más robusta y desacoplada en el futuro.

---

Este diseño asegura que el proyecto sea mantenible, escalable y fácil de extender con nuevas funcionalidades o contextos.

