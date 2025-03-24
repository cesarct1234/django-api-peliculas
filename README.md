# 🎬 Django API - Películas

Este proyecto es una API REST desarrollada con Django y Django REST Framework para gestionar películas y géneros. Incluye documentación Swagger y permite realizar consultas personalizadas.

## 🚀 Endpoints principales

| Recurso               | Endpoint                                              |
|-----------------------|--------------------------------------------------------|
| **Admin**             | `http://127.0.0.1:8000/admin/`                         |
| **Películas API**     | `http://127.0.0.1:8000/api/peliculas/`                 |
| **Géneros API**       | `http://127.0.0.1:8000/api/generos/`                   |
| **Buscar Películas**  | `http://127.0.0.1:8000/api/peliculas/buscar/?titulo=`  |
| **Géneros de Película** | `http://127.0.0.1:8000/api/peliculas/{id}/generos/`  |
| **Películas por Género** | `http://127.0.0.1:8000/api/generos/{id}/peliculas/` |
| **Swagger UI**        | `http://127.0.0.1:8000/swagger/`                      |
| **ReDoc (opcional)**  | `http://127.0.0.1:8000/redoc/`                        |

---

## ⚙️ Tecnologías usadas
- Python 3.13
- Django 5.1
- Django REST Framework
- drf-yasg (Swagger / ReDoc)

---

## 📄 Instalación y ejecución local
1. Clona el repositorio:
```bash
git clone https://github.com/cesarct1234/django-api-peliculas.git


