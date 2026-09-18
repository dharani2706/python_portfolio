# Python Developer Portfolio

A complete Django portfolio website for a Python / Django developer. It is ready for local development with SQLite and for production deployment on Render with PostgreSQL, Gunicorn, and WhiteNoise.

Live content (projects, skills, education, certifications, and contact messages) is managed from Django Admin.

## What this project includes

- Single-page portfolio: Home, About, Skills, Projects, Education, Certifications, Contact, Footer
- Downloadable resume PDF
- Light / dark mode toggle
- Contact form with validation and database storage
- Production settings from environment variables
- Render build and start configuration

## Important files

| File | Purpose |
| --- | --- |
| `manage.py` | Django command-line entry point |
| `portfolio_project/settings.py` | Project settings, database, static/media, security |
| `portfolio_project/urls.py` | Root URL configuration |
| `portfolio_project/wsgi.py` | WSGI entry point used by Gunicorn |
| `portfolio/` | Main app: models, views, forms, admin |
| `templates/` | HTML templates |
| `static/` | CSS, JavaScript, images, resume PDF |
| `media/` | Uploaded project images |
| `requirements.txt` | Python dependencies |
| `build.sh` | Render build: install packages, collect static files, migrate |
| `render.yaml` | Optional Render Blueprint |
| `.env.example` | Sample environment variables |
| `runtime.txt` | Python version for Render |

## Local setup (Windows)

Open PowerShell in the project folder, then run:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py seed_portfolio
python manage.py createsuperuser
python manage.py runserver
```

If PowerShell blocks the virtual environment script, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then open http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

## How to add content

1. Sign in to `/admin/`
2. Add or edit **Skills**, **Projects**, **Education**, and **Certifications**
3. Upload a project image if you have one
4. Replace `static/files/resume.pdf` with your real resume
5. Update your name, email, GitHub, and LinkedIn in `.env`

Contact messages appear under **Contact messages** in admin.

## GitHub

```powershell
git init
git add .
git commit -m "Add Django developer portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Do not commit `.env`, `venv/`, or `db.sqlite3`. Those are already in `.gitignore`.

## Deploy on Render

1. Push this project to GitHub.
2. In Render, create a PostgreSQL database and copy the **Internal Database URL**.
3. Create a new **Web Service** and connect the GitHub repository.
4. Set the build command:

   ```bash
   bash build.sh
   ```

5. Set the start command:

   ```bash
   gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:$PORT
   ```

6. Add environment variables:

   - `SECRET_KEY` — a long random string
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — your Render hostname, for example `your-app.onrender.com`
   - `CSRF_TRUSTED_ORIGINS` — `https://your-app.onrender.com`
   - `DATABASE_URL` — the Render PostgreSQL URL
   - `SITE_NAME`, `SITE_EMAIL`, `SITE_GITHUB`, `SITE_LINKEDIN`

   Render also provides `RENDER_EXTERNAL_HOSTNAME`, which this project adds to `ALLOWED_HOSTS` automatically.

7. Deploy. `build.sh` already runs `migrate` and `collectstatic`.
8. After the first deploy, open the Django admin on your live URL and create a superuser from the Render shell:

   ```bash
   python manage.py createsuperuser
   python manage.py seed_portfolio
   ```

9. Open the live website, submit the contact form, and confirm static files load.

You can also create both the web service and database from `render.yaml` using Render Blueprints.

## Useful commands

```powershell
python manage.py check
python manage.py test
python manage.py collectstatic
```
