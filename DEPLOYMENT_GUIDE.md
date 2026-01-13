# 🚀 Deployment Guide - Shaznuz Portfolio

This guide will help you deploy the portfolio website to production.

## 📋 Overview

- **Backend**: Django on Render (admin.shaznuz.com)
- **Frontend**: React on Vercel (shaznuz.com)
- **Database**: SQLite (default) or PostgreSQL (optional)

---

## 🔧 Backend Deployment (Render)

### Step 1: Prepare Backend

1. **Create a new repository** (if not already done) and push your code:
   ```bash
   cd backend
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Create `.env` file** (for local development):
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your local settings.

### Step 2: Deploy on Render

1. **Go to [Render Dashboard](https://dashboard.render.com/)**

2. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository with your backend code
   - Configure:
     - **Name**: `shaznuz-backend`
     - **Region**: Choose closest to you
     - **Branch**: `main`
     - **Root Directory**: `backend`
     - **Environment**: `Python 3`
     - **Build Command**: 
       ```bash
       pip install -r requirements.txt && python manage.py collectstatic --noinput
       ```
     - **Start Command**: 
       ```bash
       gunicorn portfolio.wsgi:application
       ```

3. **Set Environment Variables** in Render:
   ```
   SECRET_KEY=<generate-a-secure-secret-key>
   DEBUG=False
   ALLOWED_HOSTS=admin.shaznuz.com
   CORS_ALLOWED_ORIGINS=https://shaznuz.com,https://www.shaznuz.com
   CSRF_TRUSTED_ORIGINS=https://shaznuz.com,https://www.shaznuz.com
   PYTHON_VERSION=3.11.0
   ```
   **Note**: `DATABASE_URL` is optional. If not set, SQLite will be used automatically.

4. **Run Migrations**:
   - After first deployment, go to "Shell" in Render dashboard
   - Run:
     ```bash
     python manage.py migrate
     python manage.py createsuperuser
     ```
   - Or migrations will run automatically via `build.sh`

6. **Set Custom Domain**:
   - Go to Settings → Custom Domains
   - Add: `admin.shaznuz.com`
   - Follow DNS instructions

### Step 3: DNS Configuration for Backend

Add these DNS records in your domain provider:

```
Type: CNAME
Name: admin
Value: <your-render-service-url>.onrender.com
```

---

## 🎨 Frontend Deployment (Vercel)

### Step 1: Prepare Frontend

1. **Create `.env.local` file** in frontend directory:
   ```bash
   cd frontend
   ```
   Create `.env.local`:
   ```
   VITE_API_BASE_URL=https://admin.shaznuz.com
   ```

2. **Test locally** (optional):
   ```bash
   npm install
   npm run build
   npm run preview
   ```

### Step 2: Deploy on Vercel

1. **Go to [Vercel Dashboard](https://vercel.com/dashboard)**

2. **Import Project**:
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Configure:
     - **Framework Preset**: Vite
     - **Root Directory**: `frontend`
     - **Build Command**: `npm run build`
     - **Output Directory**: `dist`
     - **Install Command**: `npm install`

3. **Add Environment Variable**:
   - Go to Project Settings → Environment Variables
   - Add:
     ```
     Name: VITE_API_BASE_URL
     Value: https://admin.shaznuz.com
     ```
   - Apply to: Production, Preview, Development

4. **Deploy**:
   - Click "Deploy"
   - Wait for build to complete

5. **Set Custom Domain**:
   - Go to Settings → Domains
   - Add: `shaznuz.com` (primary domain)
   - Add: `www.shaznuz.com` (www subdomain)
   - **Important**: Both domains must be added in Vercel

### Step 3: DNS Configuration for Frontend

**Option 1: Use Vercel Nameservers (Recommended - Easiest)**

1. In Vercel Dashboard → Domains → Your domain
2. Copy Vercel's nameservers (usually `ns1.vercel-dns.com`, `ns2.vercel-dns.com`)
3. Go to your domain provider
4. Replace your current nameservers with Vercel's nameservers
5. Wait 24-48 hours for DNS propagation

**Option 2: Manual DNS Records**

Add these DNS records in your domain provider:

```
Type: A
Name: @
Value: 76.76.21.21
TTL: 3600

Type: CNAME
Name: www
Value: cname.vercel-dns.com
TTL: 3600
```

**Important Notes:**
- Both `shaznuz.com` and `www.shaznuz.com` must be added in Vercel Dashboard
- DNS propagation can take 24-48 hours
- SSL certificates will be automatically issued by Vercel
- Check DNS propagation: https://dnschecker.org

**If you see DNS_PROBE_FINISHED_NXDOMAIN error:**
- Verify both domains are added in Vercel
- Check DNS records are correctly configured
- Wait for DNS propagation (can take up to 48 hours)
- See `DNS_SETUP_GUIDE.md` for detailed troubleshooting

---

## 🔐 Post-Deployment Setup

### 1. Create Admin User

1. Go to `https://admin.shaznuz.com/admin/`
2. Click "Create superuser" or use Render Shell:
   ```bash
   python manage.py createsuperuser
   ```

### 2. Configure Mailjet Settings

1. Login to admin panel: `https://admin.shaznuz.com/`
2. Go to "Email Settings" (Mailjet Settings)
3. Add your Mailjet API credentials:
   - API Key
   - API Secret
   - Admin Email (where you'll receive contact form submissions)
   - Sender Email
   - Sender Name

### 3. Configure Website Settings

1. Go to "Website Settings"
2. Set:
   - Website Name
   - Upload Favicon (SVG file)

### 4. Add Content

1. Add Hero Info
2. Add Education entries
3. Add Skills and Categories
4. Add Projects
5. Add Footer content
6. Add Social Icons

---

## 🧪 Testing

### Test Backend API:
```bash
curl https://admin.shaznuz.com/api/homepage/
```

### Test Frontend:
- Visit: `https://shaznuz.com`
- Check if data loads from backend
- Test contact form

---

## 🔄 Updating Content

1. **Backend Changes**:
   - Push to GitHub
   - Render will auto-deploy

2. **Frontend Changes**:
   - Push to GitHub
   - Vercel will auto-deploy

---

## 🐛 Troubleshooting

### Backend Issues:

1. **Database Connection Error**:
   - If using SQLite (default): No configuration needed
   - If using PostgreSQL: Check `DATABASE_URL` in Render environment variables
   - Ensure database is running (if using PostgreSQL)

2. **Static Files Not Loading**:
   - Run `python manage.py collectstatic` in Render Shell
   - Check `STATIC_ROOT` in settings.py

3. **CORS Errors**:
   - Verify `CORS_ALLOWED_ORIGINS` includes your frontend domain
   - Check `CSRF_TRUSTED_ORIGINS`

### Frontend Issues:

1. **API Connection Error**:
   - Check `VITE_API_BASE_URL` in Vercel environment variables
   - Verify backend is accessible

2. **Build Errors**:
   - Check Node.js version (should be 18+)
   - Clear `.next` or `dist` folder and rebuild

---

## 📝 Important Notes

1. **Never commit**:
   - `.env` files
   - `db.sqlite3`
   - `__pycache__/` folders

2. **Always use environment variables** for:
   - SECRET_KEY
   - DATABASE_URL
   - API keys

3. **Keep DEBUG=False** in production

4. **Regular backups**:
   - Export database from Render dashboard
   - Backup media files

---

## 🎉 You're Done!

Your portfolio should now be live at:
- Frontend: https://shaznuz.com
- Backend Admin: https://admin.shaznuz.com

Happy deploying! 🚀
