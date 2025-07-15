# 🧠 AutoDoc Generator

---

## 📖 Project Overview

AutoDoc Generator is a developer productivity tool that automates the creation of project documentation (e.g., `README.md`) for public GitHub repositories. It analyzes repository metadata, code structure, and configuration files to generate clean, customizable markdown documentation.

Built using a **microservices architecture**, it offers a modern web interface, REST API integration, and robust MongoDB storage. Ideal for open-source maintainers, hackathon teams, and dev tool builders.

**Key Features:**
- 🔁 Automated README generation from GitHub repositories
- 🎨 Customizable documentation templates
- 🪄 Real-time markdown preview
- ✅ Section toggling (include/exclude)
- 🧠 Template saving with user preferences
- 📡 RESTful API for integrations



**High-Level Architecture:**

```
┌────────────┐      REST API      ┌──────────────┐       ┌────────────┐
│  Frontend  │ <───────────────>  │   Backend    │ <───> │  Database  │
│  (React)   │                    │(Flask/Python)│       │ (MongoDB)  │
└────────────┘                    └──────────────┘       └────────────┘
```

---

## 📑 Table of Contents

- [📖 Project Overview](#-project-overview)
- [🚀 Setup Instructions](#-setup-instructions)
- [⚙️ Environment Variables](#️-environment-variables)
- [🧩 Microservices Breakdown](#-microservices-breakdown)
- [🗃️ Data Schema](#️-data-schema)
- [🧪 API Endpoints](#-api-endpoints)
- [🛠️ Common Troubleshooting Scenarios](#️-common-troubleshooting-scenarios)
- [🐞 Known Issues and Workarounds](#-known-issues-and-workarounds)
- [✅ Running Tests](#-running-tests)
- [💡 Developer Tips](#-developer-tips)
- [🛣️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [📚 Links to Relevant Documentation](#-links-to-relevant-documentation)
- [📞 Support](#-support)

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
   Open http://localhost:3000 in your browser.

---

## ⚙️ Environment Variables

### Backend (.env)
| Variable         | Purpose                      | Example                      |
|------------------|------------------------------|------------------------------|
| GITHUB_API_KEY   | GitHub API token for access  | ghp_1234567890abcdef         |
| MONGO_URI        | MongoDB connection string    | mongodb://localhost:27017    |
| SECRET_KEY       | Flask session security key   | supersecretkey               |

### Frontend (frontend/.env)
| Variable             | Purpose                | Example                |
|----------------------|------------------------|------------------------|
| REACT_APP_API_URL    | Backend API base URL   | http://localhost:5000  |

---

## 🧩 Microservices Breakdown
| Service           | Description                        | Tech Stack           | Port   |
|-------------------|------------------------------------|----------------------|--------|
| Frontend          | UI for interaction and preview     | React, TailwindCSS   | 3000   |
| API Gateway       | Entry point for all backend routes | Flask, Gunicorn      | 5000   |
| GitHub Service    | Parses GitHub metadata and repos   | Python, PyGithub     | 5001   |
| Template Engine   | Renders markdown templates         | Jinja2               | 5002   |
| Storage Service   | Persists docs, templates, history  | MongoDB              | 27017  |

---

## 🗃️ Data Schema

**📁 Repository Document**
```json
{
  "_id": "ObjectId",
  "repo_url": "https://github.com/user/project",
  "name": "project",
  "owner": "user",
  "sections": ["overview", "usage", "api"],
  "generated_at": "2025-07-14T10:30:00Z",
  "readme": "string"
}
```

**📝 Template Document**
```json
{
  "_id": "ObjectId",
  "template_name": "default",
  "structure": {
    "overview": true,
    "usage": true,
    "api": true
  },
  "owner": "user123"
}
```

---

## 🧪 API Endpoints
| Method | Endpoint             | Description                |
|--------|----------------------|----------------------------|
| GET    | /api/status          | Health check               |
| POST   | /api/generate        | Generate README from repo  |
| GET    | /api/templates       | List available templates   |
| POST   | /api/templates       | Create new template        |
| PUT    | /api/templates/:id   | Update template            |
| DELETE | /api/templates/:id   | Delete template            |

**Example Request Body (POST /api/generate):**
```json
{
  "repo_url": "https://github.com/user/project",
  "template_id": "default",
  "include_sections": ["overview", "installation", "usage"]
}
```

---

## 🛠️ Common Troubleshooting Scenarios

**Backend**
- `ModuleNotFoundError`: Install dependencies with `pip install -r requirements.txt`.
- `pymongo.errors.ServerSelectionTimeoutError`: MongoDB not running or misconfigured URI.
- `OSError: Address already in use`: Free up port 5000 or change the backend port.

**Frontend**
- `Cannot find module 'react'`: Run `npm install` inside the frontend directory.
- `Port 3000 in use`: Free it or change it in `package.json`.
- `Network Error`: Make sure backend is running and `REACT_APP_API_URL` is correct.

**GitHub API**
- `401 Unauthorized`: Invalid token or missing scopes.
- `API rate limit exceeded`: Wait or switch token.

**Docker**
- Build errors: Try `docker-compose build --no-cache`, check Docker daemon, and clear disk space.

---

## 🐞 Known Issues and Workarounds

- **Markdown quirks:** Use standard Markdown for better cross-platform rendering.
- **Private repos:** Only public repos are supported. OAuth integration coming soon.
- **Template flexibility:** Advanced templates need manual edits (or community contribution).
- **Windows paths:** Use forward slashes `/` for compatibility.

---

## ✅ Running Tests

**Backend**
```bash
pytest
```
**Frontend**
```bash
npm test
```
GitHub Actions will run these tests automatically on push.

---

## 💡 Developer Tips

- Use curl or Postman to test endpoints.
- Update .env files if any setting changes.
- Frontend logs go to the browser console; backend logs go to terminal.
- Add new templates in `backend/templates/` and restart the Flask server.
- Check `CONTRIBUTING.md` before submitting PRs.

---

## 🛣️ Roadmap

- [ ] Generate README from GitHub URL
- [ ] Template saving and reuse
- [ ] Support private repos via OAuth
- [ ] PDF/HTML export of generated docs
- [ ] AI-enhanced section suggestion
- [ ] Plugin/template marketplace

---

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Make sure to follow the linting and testing guidelines.

---

## 📚 Links to Relevant Documentation

- [AutoDoc GitHub Repo](https://github.com/example/autodoc-generator)
- [API Docs (Swagger)](http://localhost:5000/docs)
- [GitHub REST API](https://docs.github.com/en/rest)
- [React Docs](https://react.dev/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [MongoDB Docs](https://www.mongodb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
- [JIRA Board](https://jira.autodocgen.com/projects/AUTODOC)
- [Confluence](https://confluence.autodocgen.com/display/AUTODOC)

---

## 📞 Support

**Technical Support Contacts:**
| Area        | Contributors                         |
|-------------|-------------------------------       |
| Front End   | Sean Reilly, Lim Alain               |
| Back End    | Alvin Chauhan, Sam Singh             |
| Database    | Sharfraaz Khan, Nihaal, Doyal        |

For general issues or bugs, please open a GitHub Issue or contact support@example.com.

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

Below are the required environment variables for the backend and frontend, with example values and guidance on how to obtain them:

### Backend (.env)
| Variable         | Purpose                                 | Example Value                        | How to Obtain/Notes                                  |
|------------------|-----------------------------------------|--------------------------------------|------------------------------------------------------|
| GITHUB_API_KEY   | GitHub API token for repo access        | ghp_1234567890abcdef                 | Create a personal access token in GitHub settings     |
| MONGO_URI        | MongoDB connection string               | mongodb://localhost:27017/autodoc    | Use your local or cloud MongoDB URI                  |
| SECRET_KEY       | Flask session secret                    | supersecretkey                       | Any random string; used for session security         |

### Frontend (frontend/.env)
| Variable             | Purpose                        | Example Value             | How to Obtain/Notes                  |
|----------------------|--------------------------------|---------------------------|--------------------------------------|
| REACT_APP_API_URL    | Backend API base URL           | http://localhost:5000     | Should match your backend server URL |

---


## 🛠️ Common Troubleshooting Scenarios

1. **Backend fails to start:**
   - Error: `ModuleNotFoundError` or `ImportError`
     - Solution: Ensure Python 3.8+ is installed and run `pip install -r requirements.txt`.
   - Error: `pymongo.errors.ServerSelectionTimeoutError`
     - Solution: Verify MongoDB is running and accessible at the URI specified in `MONGO_URI`.
   - Error: `OSError: [Errno 98] Address already in use`
     - Solution: Make sure no other process is using port 5000, or change the backend port.

2. **Frontend fails to start:**
   - Error: `Error: Cannot find module 'react'`
     - Solution: Run `npm install` in the `frontend` directory.
   - Error: `Port 3000 is already in use`
     - Solution: Stop the process using port 3000 or change the frontend port in `package.json`.
   - Error: `Network Error` when calling API
     - Solution: Confirm `REACT_APP_API_URL` is set correctly and backend is running.

3. **GitHub API errors:**
   - Error: `401 Unauthorized` or `403 Forbidden`
     - Solution: Check that `GITHUB_API_KEY` is valid and has the correct permissions.
   - Error: `API rate limit exceeded`
     - Solution: Wait for rate limit reset or use a different token.

4. **Docker build issues:**
   - Error: `failed to solve: ...` or `npm ERR!`
     - Solution: Ensure Docker is running and you have enough disk space. Try rebuilding with `docker-compose build --no-cache`.

---


## 🐞 Known Issues and Workarounds

- **Markdown rendering quirks:** Some advanced markdown features may not render identically across all platforms. Use standard markdown for best results.
- **Template customization limitations:** Only basic sections are currently supported. For advanced customization, edit the generated markdown manually or contribute a new template.
- **Private repository support:** Only public repositories are supported in this version. For private repo support, request access or update the backend to use OAuth.
- **Windows path issues:** On Windows, use forward slashes `/` in environment variables and config files to avoid path errors.

---


## 💡 Developer Tips

- Use the provided API endpoints to test documentation generation with different repositories.
- Update the `.env` files whenever you change environment settings.
- For debugging, check backend logs in the terminal and browser console for frontend errors.
- To add new documentation templates, edit the `templates/` directory in the backend and restart the backend server.
- Use Postman or curl to test API endpoints directly.
- If using Docker, ensure ports 3000 (frontend) and 5000 (backend) are available.
- Follow the code style guidelines in `CONTRIBUTING.md` for pull requests.
- Run tests before pushing changes: `pytest` for backend, `npm test` for frontend.
- For onboarding, see the [Developer Onboarding Guide](https://confluence.autodocgen.com/display/AUTODOC/Onboarding).

---


## 📚 Links to Relevant Documentation

- [AutoDoc Generator GitHub Repository](https://github.com/example/autodoc-generator)
- [API Reference (Swagger UI)](http://localhost:5000/docs)
- [GitHub REST API Docs](https://docs.github.com/en/rest)
- [React Documentation](https://react.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Sample JIRA Board](https://jira.autodocgen.com/projects/AUTODOC)
- [Sample Confluence Page](https://confluence.autodocgen.com/display/AUTODOC)
- [Developer Onboarding Guide](https://confluence.autodocgen.com/display/AUTODOC/Onboarding)

---

For further support, contact the project maintainer at support@autodocgen.com
