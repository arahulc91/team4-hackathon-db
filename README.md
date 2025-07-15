# AutoDoc Generator

---

## 📖 Project Overview

AutoDoc Generator is a tool designed to automate the creation of project documentation (e.g., README.md) for public GitHub repositories. It analyzes repository metadata and code structure to generate clean, customizable markdown documentation. The project uses a microservices architecture with a React frontend and a Python (Flask) backend, connected to a MongoDB database.

**Key Tech Stack:**
- Frontend: React.js
- Backend: Python (Flask)
- Database: MongoDB
- Other: Docker, GitHub Actions

---

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/example/autodoc-generator.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd autodoc-generator
   ```
3. **Install backend dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Install frontend dependencies:**
   ```bash
   cd frontend
   npm install
   ```
5. **Configure environment variables:**
   - Copy `.env.example` to `.env` in both root and frontend folders.
   - Update the variables as needed (see below).
6. **Run the backend server:**
   ```bash
   python app.py
   ```
7. **Run the frontend app:**
   ```bash
   cd frontend
   npm start
   ```
8. **Access the app:**
   Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## ⚙️ Environment Variables

Below are the required environment variables for the backend and frontend, with example values:

### Backend (.env)
| Variable           | Purpose                                 | Example Value                        |
|--------------------|-----------------------------------------|--------------------------------------|
| GITHUB_API_KEY     | GitHub API token for repo access        | ghp_1234567890abcdef                 |
| MONGO_URI          | MongoDB connection string               | mongodb://localhost:27017/autodoc    |
| SECRET_KEY         | Flask session secret                    | supersecretkey                       |

### Frontend (frontend/.env)
| Variable             | Purpose                        | Example Value             |
|----------------------|--------------------------------|---------------------------|
| REACT_APP_API_URL    | Backend API base URL           | http://localhost:5000     |

---

## 🛠️ Common Troubleshooting Scenarios

1. **Backend fails to start:**
   - Ensure Python 3.8+ is installed.
   - Check that all dependencies are installed (`pip install -r requirements.txt`).
   - Verify MongoDB is running and accessible at the URI specified in `MONGO_URI`.

2. **Frontend fails to start:**
   - Ensure Node.js 16+ is installed.
   - Run `npm install` in the `frontend` directory.
   - Confirm `REACT_APP_API_URL` is set correctly in the frontend `.env` file.

3. **GitHub API errors:**
   - Check that `GITHUB_API_KEY` is valid and has the correct permissions.
   - Ensure you are not exceeding GitHub API rate limits.

---

## 🐞 Known Issues and Workarounds

- **Markdown rendering quirks:** Some advanced markdown features may not render identically across all platforms. Use standard markdown for best results.
- **Template customization limitations:** Only basic sections are currently supported. For advanced customization, edit the generated markdown manually.
- **Private repository support:** Only public repositories are supported in this version. For private repo support, request access or update the backend to use OAuth.

---

## 💡 Developer Tips

- Use the provided API endpoints to test documentation generation with different repositories.
- Update the `.env` files whenever you change environment settings.
- For debugging, check backend logs in the terminal and browser console for frontend errors.
- To add new documentation templates, edit the `templates/` directory in the backend.
- Use Postman or curl to test API endpoints directly.
- If using Docker, ensure ports 3000 (frontend) and 5000 (backend) are available.

---

## 📚 Links to Relevant Documentation

- [AutoDoc Generator GitHub Repository](https://github.com/example/autodoc-generator)
- [GitHub REST API Docs](https://docs.github.com/en/rest)
- [React Documentation](https://react.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Sample JIRA Board](https://jira.example.com/projects/AUTODOC)
- [Sample Confluence Page](https://confluence.example.com/display/AUTODOC)

---

For further support, contact the project maintainer at support@example.com.
