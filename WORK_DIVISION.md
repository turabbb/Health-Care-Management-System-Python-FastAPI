# Work Division and Contributions

This file documents the team members and their responsibilities for the project and for the work included on branch `feat/testing-docs`.

Team
- turabbb — Repository owner, overall architecture, backend API design, CI/CD review
- umarm — Tests, documentation, local dev setup, basic CI validation

Contributions on this branch
- umarm
  - Added basic pytest smoke tests in `tests/test_basic.py`
  - Created `README.md`, `devops_report.md`, and `WORK_DIVISION.md`

- turabbb
  - Project author and maintainer
  - Review and merge pull requests; implement core features and DB models

Suggested next tasks and owners
- Expand unit tests to cover `crud/` and `api/` routes — owner: umarm / turabbb
- Add GitHub Actions workflows for linting, tests, and image build — owner: turabbb
- Add integration tests for Docker Compose environment — owner: umarm

Notes
- Replace or expand this file with real team member names and specific task breakdowns as the project grows.
