# ⚡ Quick Start Guide

## 🎯 Production URLs
- **Frontend**: https://shaznuz.com
- **Backend Admin**: https://admin.shaznuz.com

## 📋 Pre-Deployment Checklist

### Backend (Render)
- [ ] Push code to GitHub
- [ ] Create Web Service on Render
- [ ] Set environment variables (DATABASE_URL optional - SQLite will be used by default)
- [ ] Run migrations (or auto-run via build.sh)
- [ ] Create superuser (or auto-create via build.sh)
- [ ] Configure custom domain (admin.shaznuz.com)

### Frontend (Vercel)
- [ ] Push code to GitHub
- [ ] Import project to Vercel
- [ ] Set environment variable: `VITE_API_BASE_URL=https://admin.shaznuz.com`
- [ ] Configure custom domain (shaznuz.com)

## 🔑 Required Environment Variables

### Backend (Render)
```
SECRET_KEY=<generate-secure-key>
DEBUG=False
ALLOWED_HOSTS=admin.shaznuz.com
CORS_ALLOWED_ORIGINS=https://shaznuz.com,https://www.shaznuz.com
CSRF_TRUSTED_ORIGINS=https://shaznuz.com,https://www.shaznuz.com
PYTHON_VERSION=3.11.0
```
**Note**: `DATABASE_URL` is optional. If not set, SQLite will be used automatically.

### Frontend (Vercel)
```
VITE_API_BASE_URL=https://admin.shaznuz.com
```

## 🚀 Deployment Steps

### 1. Backend on Render

1. **Create Web Service**:
   - New → Web Service
   - Connect GitHub repo
   - Root Directory: `backend`
   - Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start: `gunicorn portfolio.wsgi:application`

3. **Set Environment Variables** (see above - DATABASE_URL is optional)

4. **Migrations & Superuser**:
   - Will run automatically via `build.sh`
   - Or manually in Render Shell:
     ```bash
     python manage.py migrate
     python manage.py createsuperuser
     ```

5. **Add Custom Domain**: `admin.shaznuz.com`

### 2. Frontend on Vercel

1. **Import Project**:
   - Add New → Project
   - Import GitHub repo
   - Root Directory: `frontend`
   - Framework: Vite

2. **Set Environment Variable**:
   - `VITE_API_BASE_URL=https://admin.shaznuz.com`

3. **Add Custom Domain**: `shaznuz.com`

## ✅ Post-Deployment

1. **Login to Admin**: https://admin.shaznuz.com/admin/
2. **Configure Mailjet**: Admin Panel → Email Settings
3. **Add Content**: Hero, Education, Skills, Projects, Footer
4. **Test**: Visit https://shaznuz.com

## 🆘 Need Help?

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed instructions.
