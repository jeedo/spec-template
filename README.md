# spec-template

A bootstrap template for spec-driven development with [Claude Code](https://claude.ai/code). Instead of repeating the same setup instructions every project, scaffold once and Claude inherits a consistent workflow: architecture-first design, red-green TDD, numbered task management, and CI — wired up from day one.

## What you get

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Workflow instructions Claude reads at every session start |
| `docs/architecture.md` | Blank architecture template (filled in before any code is written) |
| `docs/plan.md` | Blank phased task list (generated from the architecture) |
| `docs/research.md` | Blank research notes template |
| `scripts/renumber_tasks.py` | Renumber all tasks sequentially after edits |
| `scripts/complete_task.py` | Mark a task complete by number |
| `scripts/get_phase_tasks.py` | List tasks for a phase by name or number |
| `.github/workflows/ci.yml` | GitHub Actions CI stub |

## How to start a new project

1. **Create a blank repo** on GitHub and clone it locally
2. **Start Claude Code** in the repo root: `claude`
3. **Tell Claude:** `Scaffold this project from jeedo/spec-template`

Claude will download the latest release, extract the template into your repo, and prompt you to describe what you want to build.

---

## The workflow (once scaffolded)

Claude follows a strict order enforced by `CLAUDE.md`:

1. **Architecture first** — describe your goal; Claude fills in `docs/architecture.md` with you before writing any code
2. **Plan second** — once the architecture is approved, Claude generates a numbered, phased `docs/plan.md`
3. **Feature implementation** — each task gets its own branch, tests are written first (red), then the feature is implemented (green), then a PR is opened
4. **Task tracking** — Claude uses the scripts to keep `docs/plan.md` up to date

---

## For Claude — Bootstrap Instructions

> When the user asks you to scaffold from `jeedo/spec-template`, execute the following steps in order.

### Step 1 — Download the latest release

```bash
# wget (Linux)
wget https://github.com/jeedo/spec-template/releases/latest/download/template.tar.gz

# curl (macOS / alternative)
curl -L https://github.com/jeedo/spec-template/releases/latest/download/template.tar.gz -o template.tar.gz
```

### Step 2 — Extract into the repo root and remove the archive

```bash
tar -xzf template.tar.gz && rm template.tar.gz
```

### Step 3 — Confirm to the user

Tell the user:

> Your project is scaffolded. You now have:
> - **`CLAUDE.md`** — workflow instructions (read automatically at every session start)
> - **`docs/architecture.md`** — define your system design here before writing any code
> - **`docs/plan.md`** — task list, generated from the architecture once it's approved
> - **`docs/research.md`** — scratch space for any research needed before the architecture is finalised
> - **`scripts/`** — task management utilities (renumber, complete, list by phase)
> - **`.github/workflows/ci.yml`** — CI stub to customise for your stack
>
> **What would you like to build?** Describe your project goal and we'll define the architecture together before writing any code.
