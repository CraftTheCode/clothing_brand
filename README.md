# 🚀 Getting Started with the Clothing Brand Django Project

Welcome! This guide will help you set up and start developing with this Django project, even if you’re new to Django.

---

## 1. **Activate the Virtual Environment**

If you haven’t already, create and activate a virtual environment:

**Windows:**
```sh
.venv\Scripts\activate
```

**macOS/Linux:**
```sh
source .venv/bin/activate
```

---

## 2. **Install All Dependencies**

We use [uv](https://github.com/astral-sh/uv) for dependency management.

```sh
uv sync
```
This will install everything listed in `pyproject.toml` and lock it in `uv.lock`.

---

## 3. **Run Python Commands with uv**

Instead of `python`, use `uv run` for running scripts.  
For example, to run Django management commands:

```sh
uv run manage.py <command>
```

---

## 4. **Create Your First Django App**

To create a new app (e.g., `products`):

```sh
uv run manage.py startapp products
```

Add your new app to the `INSTALLED_APPS` list in `settings.py`.

---

## 5. **Run the Development Server**

Start the server with:

```sh
uv run manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 6. **Format Your Code**

We use [ruff](https://docs.astral.sh/ruff/) for code formatting.

**To format all code:**
```sh
uv run ruff format .
```

**To check formatting (without making changes):**
```sh
uv run ruff format . --check
```

---

## 7. **Other Useful Commands**

- **Apply migrations:**  
  ```sh
  uv run manage.py migrate
  ```
- **Create a superuser:**  
  ```sh
  uv run manage.py createsuperuser
  ```
- **Run tests:**  
  ```sh
  uv run pytest
  ```

---

## 8. **Project Structure Overview**

- `pyproject.toml` — Dependency and project config
- `uv.lock` — Locked dependencies
- `src` — Django project source code
- `manage.py` — Django’s main command-line utility

---

## 9. **Resources**

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

---

**Happy coding! If you have questions, check the docs above or drop a mail**