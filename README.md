# CSE120 GitHub Workshop

## 1. Create a GitHub Repository from Template

### 1.1 Steps:
1. Create a new GitHub repository using the template: [CSE120-Template](https://github.com/cse120-ucm/template).
2. Name the repository as `cse120-workshop`
3. Add your partner as a collaborator to the repository.
4. Make sure to enable GitHub features: Projects, Discussions, WIKI, Codespaces for the repository
5. Update Readme.md with project details.
6. Create a new project board for task management(Use Iteration template).
7. Rename default branch to `main`.
8. Make sure main branch is protected (Require pull request reviews before merging, Require status checks to pass before merging).

### 1.2 Update Issue Labels

#### Make sure you have the following issue labels:

- **Bug** - An unexpected problem or behavior
- **Documentation** - Improvements or additions to project documentation, wiki, README, etc
- **Feature** - A request, idea, or new functionality
- **Discussion** - Further information is requested or issue requires a discussion
- **Task** - A specific piece of work

### 1.3 Create first issue

Create an issue to update Readme.md with project details.

- Use documentation template
- Assign the issue to yourself and your partner.
- Add the issue to the project board.

**Hints:**

- **Title:** Update Readme.md with project details
- **Description:** Update Readme.md with project details including project name, team members, project description
- **Label:** Documentation

### 1.4 Update `Readme.md` with project details.

- Project Name
- Team Members
- Project Description
- Technologies Used
- Setup Instructions

### 1.5 Create & Merge a PR

1. Create a new branch from main branch. Name the branch as `update-readme`.
2. Update Readme.md with project details.
3. Commit the changes with a meaningful commit message.
4. Push the branch to the remote repository.
5. Create a pull request from `update-readme` branch to `main` branch.
6. Request a review from your partner.
7. Once the review is approved, merge the pull request.
8. Delete the `update-readme` branch after merging.

## 2. Create milestones for the project:

We will use these milestones and issue for the second part of this workshop next week.

### Steps:
1. Create the milestones in the GitHub repository
2. Create issues for each milestone using appropriate templates.
3. Show project board and how to link issues to the project board.
4. Assign issues

### Milestone 1: Project Scaffolding

This milestone focuses on setting up the initial project structure, including a FastAPI backend with a health check endpoint, basic tests, CI/CD integration, and Docker support.

#### Issue 1 (Feature Request) - Initial FastAPI App - (Michael)
**Summary:** Create initial FastAPI app with a single /health endpoint for uptime checks.

**Motivation / Rationale:** Establishes an executable service anchor for CI, tests, future UI integration.

**Proposed Implementation:** 
- [ ] Add `app/main.py` with FastAPI instance `Average Workshop API`; 
- [ ] `/health` returns {"status":"ok"}. No extra routes.
- [ ] Service runs `uvicorn app.main:app` and curl returns expected JSON.

#### Issue 2 (Task) - Add first tests - (Michael)

**Objective:** Add pytest ensuring `/health` returns 200 + exact JSON.

**Details / Subtasks:**
- [ ] Create `tests/test_health.py`
- [ ] Use TestClient
- [ ] Assert status + JSON

**Acceptance Criteria:** Test passes locally; fails if contract changes.

#### Issue 3 (Task) - Introduce CI and Docker - (Michael)

**Objective:** Introduce CI workflow and Dockerfile for baseline.

**Details / Subtasks:**
- [ ] Add GitHub Actions workflow (lint, type, test) on PR
- [ ] Add minimal Dockerfile (python:3.11-slim, uv install, run uvicorn)
- [ ] Add GitHub Actions job to build and publish Docker image

**Acceptance Criteria:** 
- [ ] CI passes on PR
- [ ] Docker image builds successfully

#### Issue 4 (Feature Request) - Add NiceGUI Shell - (Santosh)

**Summary:** Add NiceGUI shell with the website title and subtitle at root page.

**Motivation / Rationale:** Establish UI integration boundary before adding logic.

**Proposed Implementation:** Add NiceGUI to the project, create a main page with a title and subtitle using NiceGUI components.

### Milestone 2: Average Calculation

This milestone focuses on implementing the core functionality of calculating the average of user-provided numeric tokens.

#### Issue 5 (Feature Request) - Average Calculation Form - (Michael)

**Summary:** Add form for users to input comma/space separated numeric tokens, compute average.

**Motivation / Rationale:** Introduces interactive computation; core learning objective.

**Proposed Implementation:** Parse tokens by splitting on commas then spaces; convert to float; display mean; no non-numeric guard yet.

