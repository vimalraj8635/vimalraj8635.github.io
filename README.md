# 🚀 Vimalraj G — DevOps Engineer Portfolio

![Portfolio](https://img.shields.io/badge/Portfolio-Live-brightgreen?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Backend-blue?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions)

> A personal portfolio website for a DevOps Engineer built with HTML/CSS/JS frontend and a Flask + Gmail SMTP backend for the contact form.

🌐 **Live Site:** [vimalraj8635.github.io](https://vimalraj8635.github.io)

---

## 📁 Project Structure

```
vimalraj8635.github.io/
├── index.html                  # Frontend — Portfolio website
├── app.py                      # Backend — Flask email server
├── requirements_backend.txt    # Python dependencies
└── README.md                   # Project documentation
```

---

## ✨ Features

- 🎨 **Dark theme** with colorful accents — DevOps techy look
- 💻 **Animated terminal** in hero section with real commands
- 🛠 **Skills section** — color-coded by category
- 🚀 **Projects section** — CI/CD pipeline, Research, Kubernetes (coming soon)
- 📄 **Resume download** — one-click PDF download
- 📩 **Working contact form** — sends email via Flask + Gmail SMTP
- 📱 **Fully responsive** — works on mobile, tablet, desktop

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask, Flask-Mail, Flask-CORS |
| Email | Gmail SMTP |
| Fonts | Fira Code, Inter (Google Fonts) |
| Hosting | GitHub Pages (frontend) + Render (backend) |

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.8+
- Gmail account with 2-Step Verification enabled
- Git

---

### Step 1 — Clone the repository

```bash
git clone https://github.com/vimalraj8635/vimalraj8635.github.io.git
cd vimalraj8635.github.io
```

---

### Step 2 — Install Python dependencies

```bash
pip install flask flask-mail flask-cors
```

Or use the requirements file:

```bash
pip install -r requirements_backend.txt
```

---

### Step 3 — Set up Gmail App Password

> ⚠️ You CANNOT use your regular Gmail password. You must create an App Password.

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click **Security**
3. Enable **2-Step Verification** (if not already enabled)
4. Search for **"App Passwords"**
5. Select **Mail** → Generate
6. Copy the 16-character password

---

### Step 4 — Configure `app.py`

Open `app.py` and update these lines:

```python
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'   # Your Gmail address
app.config['MAIL_PASSWORD'] = 'abcd efgh ijkl mnop'    # Your App Password
```

Also update the recipient email:

```python
recipients=['your_email@gmail.com']   # Where you want to receive messages
```

---

### Step 5 — Run the Flask backend

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

---

### Step 6 — Open the portfolio

Open `index.html` in your browser (double-click or use Live Server in VS Code).

Fill in the contact form and click **Send Message** — you will receive the email instantly! 📩

---

## 🌍 Deployment

### Frontend → GitHub Pages

```bash
# Make sure your repo is named: vimalraj8635.github.io
git add .
git commit -m "Deploy portfolio"
git push origin main
```

Then go to:
**Repo Settings → Pages → Source → main branch → Save**

Your site will be live at: `https://vimalraj8635.github.io`

---

### Backend → Render.com (Free)

1. Push `app.py` and `requirements_backend.txt` to a GitHub repo
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your repo
4. Set these:

| Field | Value |
|---|---|
| Runtime | Python |
| Build Command | `pip install -r requirements_backend.txt` |
| Start Command | `python app.py` |

5. Add Environment Variables in Render dashboard:

| Key | Value |
|---|---|
| `MAIL_USERNAME` | your_email@gmail.com |
| `MAIL_PASSWORD` | your_app_password |

6. After deploy, copy your Render URL (e.g. `https://vimalraj-portfolio-api.onrender.com`)
7. Update `index.html` — replace `localhost:5000` with your Render URL:

```javascript
fetch('https://vimalraj-portfolio-api.onrender.com/send-message', {
```

---

## 🧪 Testing the Contact Form

### Test locally:
1. Run `python app.py`
2. Open browser → `http://localhost:5000/send-message`
3. If you see **"Method Not Allowed"** → Flask is running ✅
4. Open `index.html`, fill the form, and submit

### Common errors:

| Error | Cause | Fix |
|---|---|---|
| `Failed to fetch` | Flask not running | Run `python app.py` |
| `CORS error` | flask-cors missing | `pip install flask-cors` |
| `Authentication failed` | Wrong App Password | Regenerate App Password |
| `Connection refused` | Wrong port | Make sure Flask runs on port 5000 |

---

## 📸 Screenshots

> Add screenshots of your portfolio here after deployment!

```
Homepage    → hero section with terminal animation
Skills      → color-coded tech stack cards
Projects    → CI/CD pipeline, research, Kubernetes
Contact     → working email form
```

---

## 🗺 Roadmap

- [x] Portfolio frontend with dark theme
- [x] Working contact form with Gmail SMTP
- [x] Responsive mobile design
- [ ] Deploy Flask backend to Render
- [ ] Add Kubernetes project to projects section
- [ ] Add Jenkins project to projects section
- [ ] Add custom domain

---

## 👨‍💻 Author

**Vimalraj G** — Aspiring DevOps Engineer

| Platform | Link |
|---|---|
| 📧 Email | vimalraj8635@gmail.com |
| 💼 LinkedIn | [linkedin.com/in/vimalraj-g-41641a259](https://linkedin.com/in/vimalraj-g-41641a259) |
| 🐱 GitHub | [github.com/vimalraj8635](https://github.com/vimalraj8635) |
| 📍 Location | Chennai, Tamil Nadu, India |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Built with ♥ by <strong>Vimalraj G</strong> | Chennai, India</p>
