# 💎 LuxeJewels — Multi-Vendor Jewellery Marketplace

A full-stack, enterprise-grade **Multi-Vendor B2B2C Jewellery E-Commerce Marketplace** built with **Django REST Framework (DRF)**, **MongoDB**, and **React (Vite + TailwindCSS)**.

---

## 🚀 Quick Setup Guide

Follow the instructions below to get the project up and running on your local machine.

### Prerequisites
- **Python 3.10+**
- **Node.js 18+ & npm**
- **MongoDB** (Local MongoDB Community Server running on `mongodb://localhost:27017` or free [MongoDB Atlas](https://www.mongodb.com/atlas) URI)

---

### 1. Clone the Repository

```bash
git clone https://github.com/PratikDate01/Jewellery_Marketplace.git
cd Jewellery_Marketplace
```

---

### 2. Backend Setup (Django + MongoDB)

#### A. Create and activate a Python virtual environment:
- **Windows (PowerShell):**
  ```powershell
  cd backend
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **macOS / Linux:**
  ```bash
  cd backend
  python3 -m venv venv
  source venv/bin/activate
  ```

#### B. Install Python dependencies:
```bash
pip install -r requirements.txt
```

#### C. Configure environment variables:
Create a `.env` file inside the `backend/` directory (you can copy `.env.example`):
```bash
cp .env.example .env
```
Ensure your `backend/.env` has:
```env
DJANGO_SECRET_KEY=your-django-secret-key-1234567890
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
MONGO_URI=mongodb://localhost:27017/jewellery_db

# Cloudinary (Optional for local testing if not uploading images)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

#### D. Run database migrations:
```bash
python manage.py migrate
```

#### E. (Optional) Create an Admin Superuser:
```bash
python manage.py createsuperuser
```

#### F. Start the Django backend server:
```bash
python manage.py runserver
```
The backend API is now running at: `http://127.0.0.1:8000/`

---

### 3. Frontend Setup (React + Vite)

Open a new terminal window:

#### A. Navigate to frontend directory:
```bash
cd frontend
```

#### B. Install Node dependencies:
```bash
npm install
```

#### C. Configure environment variables:
Create a `.env` file inside the `frontend/` directory (you can copy `.env.example`):
```bash
cp .env.example .env
```
Ensure `frontend/.env` has:
```env
VITE_API_URL=http://localhost:8000/api
```

#### D. Start the Vite development server:
```bash
npm run dev
```
The frontend application will run at: `http://localhost:5173/`

---

## 🤖 Prompt for AI Assistants (Automatic Setup)

If you are using an AI coding assistant (like Cursor, Antigravity, Copilot, ChatGPT, etc.) inside this project directory, simply copy and paste this prompt:

```text
Please set up and run this full-stack project (Jewellery_Marketplace) on my machine:
1. Backend setup:
   - Create a Python virtual environment inside `backend/` named `venv` and activate it.
   - Install all packages from `backend/requirements.txt`.
   - Ensure `backend/.env` exists (copy from `backend/.env.example` if missing, using `mongodb://localhost:27017/jewellery_db` as default MONGO_URI).
   - Run `python manage.py migrate`.
2. Frontend setup:
   - Navigate to `frontend/`.
   - Install all node dependencies with `npm install`.
   - Ensure `frontend/.env` exists (copy from `frontend/.env.example` if missing with `VITE_API_URL=http://localhost:8000/api`).
3. Verify that MongoDB is accessible and tell me the commands to start both the backend (`python manage.py runserver`) and frontend (`npm run dev`).
```

---

## 📁 Repository Structure

```
Jewellery_Marketplace/
├── backend/
│   ├── config/              # Django settings (base, dev, prod) & URLs
│   ├── accounts/            # Users, JWT auth, and role management
│   ├── products/            # Jewellery catalog & pricing calculation
│   ├── categories/          # Product categories
│   ├── cart/                # Customer cart
│   ├── wishlist/            # Customer wishlist
│   ├── orders/              # Orders and ledger tracking
│   ├── payments/            # Payment integration
│   ├── suppliers/           # Supplier / vendor management
│   ├── coupons/             # Promotional coupons
│   ├── analytics/           # Marketplace analytics
│   ├── requirements.txt     # Python dependencies
│   └── manage.py            # Django CLI
├── frontend/
│   ├── src/                 # React components, pages, context, hooks
│   ├── public/              # Static assets
│   ├── package.json         # Node dependencies & scripts
│   ├── tailwind.config.js   # Tailwind CSS styling configuration
│   └── vite.config.js       # Vite build configuration
├── PROJECT_DOCUMENTATION.md # Detailed technical & architectural docs
└── README.md                # Quickstart and setup guide
```
