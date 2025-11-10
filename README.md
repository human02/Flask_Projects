# Poetry Setup Guide for Flask Project

## 1. Configure Poetry to create virtual environment in project folder
```bash
poetry config virtualenvs.in-project true
```

**What it does:**
- Creates `.venv` folder inside your project directory instead of Poetry's cache
- Makes the virtual environment easier for IDEs (VS Code) to detect
- Better for version control and project portability

**Note:** This is a global setting that applies to all future Poetry projects.

---

## 2. Create a new Poetry project
```bash
poetry new project_01
```

**What it does:**
- Creates a new project directory with standard Python package structure
- Generates `pyproject.toml` (Poetry configuration file)
- Creates `README.md`, `tests/` folder, and package directory
- Initializes the project structure

**Project structure created:**
```
project_01/
├── pyproject.toml
├── README.md
├── project_01/
│   └── __init__.py
└── tests/
    └── __init__.py
```

---

## 3. Add Flask framework
```bash
poetry add flask
```

**What it does:**
- Installs Flask and its dependencies
- Adds Flask to `[project.dependencies]` in `pyproject.toml`
- Updates `poetry.lock` file with exact versions
- Required for running your web application

**Usage:** Production dependency - needed to run the app

---

## 4. Add HTTP requests library
```bash
poetry add requests
```

**What it does:**
- Installs the `requests` library for making HTTP requests
- Adds to production dependencies in `pyproject.toml`
- Useful for consuming external APIs

**Usage:** Production dependency - for API calls and HTTP operations

---

## 5. Add pytest (incorrect - creates duplicate)
```bash
poetry add pytest
```

**⚠️ Note:** This adds pytest as a **production** dependency, which is incorrect since pytest is only needed for development/testing.

**Better approach:** Skip this command and use step 6 instead.

---

## 6. Add testing dependencies (development only)
```bash
poetry add --group dev pytest pytest-flask
```

**What it does:**
- Installs `pytest` (testing framework)
- Installs `pytest-flask` (Flask-specific testing utilities)
- Adds to `[dependency-groups.dev]` in `pyproject.toml`
- These won't be installed in production

**Usage:** Development-only dependencies for writing and running tests

**Key difference:**
- `--group dev` = Development only (testing, linting, etc.)
- No flag = Production (required to run the app)

---

## 7. Install all dependencies
```bash
poetry install
```

**What it does:**
- Reads `pyproject.toml` and `poetry.lock`
- Installs all dependencies (production + dev groups)
- Creates/updates the virtual environment (`.venv/`)
- Required after cloning the project or adding new dependencies

**When to use:**
- After creating a new project
- After cloning from Git
- After adding new packages
- To ensure all dependencies are installed

---

## 8. Sync dependencies with environment
```bash
poetry sync
```

**What it does:**
- Installs all dependencies listed in `pyproject.toml`
- **Removes packages** that are NOT in `pyproject.toml`
- Ensures your environment exactly matches your dependency specifications

**Key difference from `poetry install`:**
- `poetry install` - Only installs/updates packages, keeps extra packages
- `poetry sync` - Installs/updates AND removes unlisted packages

**When to use:**
- After removing dependencies from `pyproject.toml`
- Cleaning up orphaned packages
- Ensuring clean environment before deployment or testing
- After switching branches with different dependencies
- Team collaboration after pulling changes

**Command variations:**
```bash
# Sync everything (production + dev)
poetry sync

# Sync only production dependencies
poetry sync --without dev

# Sync only dev dependencies
poetry sync --only dev
```

---

## Recommended Workflow

**Initial setup:**
```bash
# Configure Poetry (one-time global setting)
poetry config virtualenvs.in-project true

# Create new project
poetry new project_01
cd project_01

# Add production dependencies
poetry add flask requests

# Add development dependencies
poetry add --group dev pytest pytest-flask

# Install all dependencies
poetry install
```

**Running your application:**
```bash
# Activate Poetry shell
poetry shell

# Run Flask app
python -m src.project_01.app

# Or run directly without shell
poetry run python -m src.project_01.app
```

**Running tests:**
```bash
# Run all tests
poetry run pytest

# Run with verbose output
poetry run pytest -v

# Run with coverage
poetry run pytest --cov=src
```

**Daily development workflow:**
```bash
# Pull latest changes
git pull origin main

# Sync dependencies (removes old, adds new)
poetry install --sync

# Start development
poetry shell
```

---

## Common Poetry Commands

| Command                            | Description                                       |
| ---------------------------------- | ------------------------------------------------- |
| `poetry install`                   | Install all dependencies from `pyproject.toml`    |
| `poetry install --sync`            | Install dependencies and remove unlisted packages |
| `poetry add <package>`             | Add production dependency                         |
| `poetry add --group dev <package>` | Add development dependency                        |
| `poetry remove <package>`          | Remove a dependency                               |
| `poetry update`                    | Update all dependencies to latest versions        |
| `poetry show`                      | List all installed packages                       |
| `poetry show --tree`               | Show dependency tree                              |
| `poetry shell`                     | Activate virtual environment                      |
| `poetry run <command>`             | Run command in virtual environment                |
| `poetry env info`                  | Show virtual environment info                     |
| `poetry env remove python`         | Remove virtual environment                        |
| `poetry lock`                      | Update `poetry.lock` without installing           |

---

## Installing on a New Machine

When cloning your project on another machine:
```bash
# Clone the repository
git clone <your-repo-url>
cd project_01

# Install all dependencies (production + dev)
poetry install

# Or install only production dependencies
poetry install --without dev
```

---

## Important Files

- **`pyproject.toml`** - Project configuration and dependencies (commit to Git)
- **`poetry.lock`** - Locked dependency versions for reproducibility (commit to Git)
- **`.venv/`** - Virtual environment folder (add to `.gitignore`)

---

## Fixing the Duplicate pytest Issue

If you ran `poetry add pytest` before `poetry add --group dev pytest`, fix it:
```bash
# Remove pytest from production dependencies
poetry remove pytest

# Ensure it's in dev dependencies
poetry add --group dev pytest pytest-flask

# Reinstall
poetry install
```

Your `pyproject.toml` should look like:
```toml
[project]
dependencies = [
    "flask>=3.1.2",
    "requests>=2.32.5"
]

[dependency-groups]
dev = [
    "pytest>=8.3.4",
    "pytest-flask>=1.3.0"
]
```

---

## Troubleshooting

### Problem: Package I need got removed

**Cause:** Package wasn't in `pyproject.toml`

**Solution:**
```bash
# Add it properly
poetry add package-name

# Or add as dev dependency
poetry add --group dev package-name
```

### Problem: VS Code doesn't recognize virtual environment

**Cause:** Virtual environment not in project folder

**Solution:**
```bash
# Set Poetry to use in-project venv
poetry config virtualenvs.in-project true

# Recreate environment
poetry env remove python
poetry install

# Reload VS Code
# Cmd+Shift+P → "Python: Select Interpreter" → Select .venv
```

### Problem: Sync is slow

**Cause:** Many packages to remove/reinstall

**Solution:**
```bash
# Remove entire virtual environment and reinstall
poetry env remove python
poetry install --sync
```

### Problem: Sync doesn't remove a package

**Cause:** Package might be a dependency of another package

**Solution:**
```bash
# Check dependency tree
poetry show --tree

# The package might be required by something else
```

---

## Best Practices

### ✅ Do:
- Always use `poetry add` to add dependencies
- Commit `pyproject.toml` and `poetry.lock` to Git
- Use `--group dev` for development dependencies
- Run `poetry install --sync` after pulling changes
- Use `poetry shell` or `poetry run` to ensure correct environment

### ❌ Don't:
- Never use `pip install` in Poetry projects
- Don't commit `.venv/` folder to Git
- Don't manually edit `poetry.lock`
- Don't add test/lint tools as production dependencies

---

## Production Deployment
```bash
# Install only production dependencies
poetry install --sync --without dev

# Run application
poetry run python -m src.project_01.app
```

---

## Summary

Poetry provides a modern, reliable way to manage Python dependencies:

1. **Configure** - Set up Poetry to use in-project virtual environments
2. **Create** - Initialize new projects with proper structure
3. **Add** - Install dependencies with automatic version management
4. **Install** - Set up environments on any machine
5. **Sync** - Keep environments clean and consistent
6. **Run** - Execute code in isolated virtual environments

**Golden rule:** Use `poetry install --sync` regularly to keep your environment an exact mirror of `pyproject.toml`.