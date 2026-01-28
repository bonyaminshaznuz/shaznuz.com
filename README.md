# 🚀 Shaznuz Portfolio Website

A modern, full-stack portfolio website built with Django (Backend) and React (Frontend).

Live Link: https://www.shaznuz.com/

## 📁 Project Structure

```
shaznuz.com/
├── backend/          # Django Backend API
│   ├── portfolio/   # Django project settings
│   ├── user/        # Main app with models and views
│   └── core/        # Core utilities
├── frontend/         # React Frontend
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── routes/       # Page routes
│   │   └── config/       # Configuration files
│   └── public/       # Static assets
└── DEPLOYMENT_GUIDE.md  # Deployment instructions
```

## 🛠️ Tech Stack

### Backend
- **Django 5.1.6** - Web framework
- **SQLite** - Database (default)
- **PostgreSQL** - Database (optional, via DATABASE_URL)
- **Gunicorn** - WSGI server
- **WhiteNoise** - Static file serving
- **Mailjet** - Email service

### Frontend
- **React 19** - UI library
- **Vite** - Build tool
- **Axios** - HTTP client
- **React Router** - Routing
- **Tailwind CSS** - Styling

## 🚀 Quick Start

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create `.env` file**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your settings.

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**:
   ```bash
   python manage.py runserver
   ```

Backend will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Create `.env.local` file**:
   ```
   VITE_API_BASE_URL=http://127.0.0.1:8000
   ```

4. **Run development server**:
   ```bash
   npm run dev
   ```

Frontend will be available at `http://localhost:5173`

## 📦 Features

- ✅ Dynamic portfolio content management
- ✅ Contact form with email notifications
- ✅ Admin panel for content management
- ✅ Responsive design
- ✅ SEO optimized
- ✅ Email notifications via Mailjet
- ✅ Image and file uploads
- ✅ Skills and projects showcase
- ✅ Education timeline
- ✅ Social media links

## 🌐 Production Deployment

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

**Quick Overview**:
- Backend: Deploy to Render at `admin.shaznuz.com`
- Frontend: Deploy to Vercel at `shaznuz.com`
- Database: PostgreSQL on Render

## 📝 Environment Variables

### Backend (.env)
```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:5173
CSRF_TRUSTED_ORIGINS=http://localhost:5173
```

### Frontend (.env.local)
```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## 🔧 Admin Panel

Access admin panel at: `http://127.0.0.1:8000/admin/` (development)

Features:
- Dashboard with statistics
- Hero section management
- Education entries
- Skills and categories
- Projects
- Footer content
- Social icons
- Contact submissions
- Email settings (Mailjet)
- Website settings

## 📧 Email Configuration

1. Get Mailjet API credentials from [Mailjet](https://www.mailjet.com/)
2. Go to Admin Panel → Email Settings
3. Add:
   - API Key
   - API Secret
   - Admin Email
   - Sender Email
   - Sender Name

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is private and proprietary.

## 👤 Author

**Kazi Bony Amin**
- Portfolio: [shaznuz.com](https://shaznuz.com)
- Email: mdshaznuz@gmail.com

---

Made with ❤️ using Django and React
