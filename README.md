# Command-Line Project Management Tool

A lightweight, object-oriented CLI tool built in Python for managing users, projects, and tasks. The tool persists data locally in JSON format and provides conditional validation using Python property decorators.

---

## 📁 Project Structure

```text
project_tracker/
│
├── main.py                 # CLI entry point using argparse
├── models/                 # Class definitions with property decorators
│   ├── __init__.py
│   ├── user.py             # User model
│   ├── project.py          # Project model
│   └── task.py             # Task model
├── data/                   # Local JSON storage (created automatically)
│   └── tracker_data.json
└── utils/                  # Utility hooks
    ├── __init__.py
    └── storage.py          # JSON save and load logic
```

---

## 🛠️ Requirements & Installation

- **Python:** 3.8+
- **External Dependencies:** None (uses standard Python libraries `argparse`, `json`, `os`).

### Setup Instructions

1. **Clone or download the project** to your local machine.
2. **Navigate into the project folder:**

   ```bash

   cd project_tracker

   ```

---

## 🚀 How to Run (CLI Usage)

All actions are executed through `main.py` using terminal subcommands and arguments.

### 1. Add a New User

```bash

python main.py add-user --name "Alice Smith" --email "alice@example.com"

```

### 2. List All Users

```bash

python main.py list-users

```

### 3. Add a Project to a User

```bash

python main.py add-project --user "alice@example.com" --title "Website Redesign" --desc "Build new user dashboard" --due "2026-12-31"

```

### 4. List Projects for a User

```bash

python main.py list-projects --user "alice@example.com"

```

### 5. Add a Task to a Project

```bash

python main.py add-task --user "alice@example.com" --project "Website Redesign" --title "Setup Database" --assigned "Alice"

```

### 6. Mark a Task as Complete

```bash

python main.py complete-task --user "alice@example.com" --project "Website Redesign" --task "Setup Database"

```

### 7. View Help Menu

```bash

python main.py --help

```

---

## ✨ Features & Architecture

- **Property Decorators (`@property`):** Ensures clean, Pythonic encapsulation with data validation (e.g., verifying valid email format, enforcing non-empty titles, and restricting task status values).
- **Class Methods (`.get()`, `.all()`):** Class-level tracking in the `User` model allowing instance retrieval.
- **Auto Data Persistence:** Data is automatically saved to and loaded from `data/tracker_data.json`. The `data/` folder is auto-created if missing.
- **Serialization:** Built-in `to_dict()` and `from_dict()` methods handle conversion between Python objects and JSON format.
