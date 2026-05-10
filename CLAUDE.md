# Claude Instructions

## Session Start

Always read at the beginning of every session:
- [`docs/architecture.md`](docs/architecture.md) — system design and decisions
- [`docs/plan.md`](docs/plan.md) — phased task list with completion status

Then run `python scripts/check_docs.py` and surface any failures to the user before proceeding.

---

## Starting a New Project

When the user defines a project goal:

1. **Architecture first** — collaborate to fill in `docs/architecture.md` section by section. Do not write any code until the user approves it.
2. **Plan second** — only after architecture approval, generate `docs/plan.md` with numbered, phased tasks derived from the architecture.
3. **No implementation** until both documents are approved by the user.

### Required sections in `docs/architecture.md`
- Overview & Goals
- Tech Stack
- System Components
- Data Model / API
- Link to `docs/research.md` if additional research was performed

### Default phases in `docs/plan.md`
- Phase 1: Setup & Scaffolding
- Phase 2: Core Domain
- Phase 3: API / Interface
- Phase 4: Testing & QA
- Phase 5: CI/CD & Deployment

---

## Implementing a Feature

When the user asks to implement a task from `docs/plan.md`:

1. Identify the task number
2. Create a branch: `git checkout -b feature/<task-number>-<short-slug>`
3. **Write tests first** — run them and confirm they **fail** (red phase)
4. Implement the feature until all tests pass (green phase)
5. Mark the task complete: `python scripts/complete_task.py <task-number>`
6. Commit using a conventional commit message (includes the updated `docs/plan.md`)
7. Push and open a PR: `gh pr create`

---

## Branching

- Always branch from `main` — never commit directly to `main`
- Name format: `feature/<task-number>-<short-slug>` (e.g. `feature/7-add-jwt-auth`)

---

## Commit Messages (Conventional Commits)

Format: `<type>(<scope>): <description>`

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`

Examples:
```
feat(auth): add JWT token validation
fix(api): handle empty upstream response
docs(arch): update data model section
test(auth): add edge cases for expired tokens
```

---

## Python Projects

- Always use `uv` — never pip, never poetry
- Add runtime dependency: `uv add <package>`
- Add dev dependency: `uv add --dev <package>`
- Run commands: `uv run <command>`
- Never manually edit dependency lists in `pyproject.toml`

### After any Python file change

Always run the local tools before committing:

```bash
uv run ruff check --fix .
uv run ruff format .
uv run mypy .
uv run pytest
```

Fix all errors before proceeding.

---

## GitHub

Use the `gh` CLI for all GitHub operations:

```bash
gh pr create --title "feat: ..." --body "..."
gh pr status
gh run list        # check CI status
gh issue list
```

---

## Task Management Scripts

Run from the project root:

| Script | Usage | Description |
|--------|-------|-------------|
| `check_docs.py` | `python scripts/check_docs.py` | Validate architecture.md and plan.md (required sections, numbering, TBD markers) |
| `renumber_tasks.py` | `python scripts/renumber_tasks.py` | Restore sequential numbering after adding/removing tasks |
| `complete_task.py` | `python scripts/complete_task.py <N>` | Mark task N as complete |
| `get_phase_tasks.py` | `python scripts/get_phase_tasks.py <phase>` | List tasks for a phase (by name or number) |

---

## Template Repository Structure

This repository (`spec-template`) is itself a template. The `template/` folder contains everything that gets bootstrapped into a new project:

```
template/
├── CLAUDE.md                  ← workflow instructions (this file)
├── .github/workflows/ci.yml   ← CI workflow stub
├── docs/
│   ├── architecture.md        ← blank architecture template
│   ├── plan.md                ← blank plan template
│   └── research.md            ← blank research notes template
└── scripts/
    ├── renumber_tasks.py
    ├── complete_task.py
    └── get_phase_tasks.py
```

### Using the template in a new project

Download and extract the latest release asset into the project root:

```bash
curl -L https://github.com/jeedo/spec-template/releases/latest/download/template.tar.gz | tar -xz
```

To pin to a specific version, replace `latest/download` with `download/v<version>`.

---

## Releasing a New Version

Releases are fully automated via `.github/workflows/release.yml`. To publish a new version:

1. Ensure all changes are merged to `main`
2. Tag the commit and push:
   ```bash
   git tag v<version> && git push origin v<version>
   ```
3. The workflow will:
   - Package the `template/` folder as `template.tar.gz`
   - Create a GitHub release named after the tag with auto-generated notes
   - Attach `template.tar.gz` as a downloadable release asset
