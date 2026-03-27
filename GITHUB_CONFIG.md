# GitHub Repository Configuration

## Repository Details

**Name**: vikrant-OBLITERATUS  
**Owner**: vikrant-project  
**URL**: https://github.com/vikrant-project/vikrant-OBLITERATUS

## Description (160 chars max)

Advanced abliteration framework: 8-stage pipeline, auto fine-tuning, voice support, real-time collaboration, security scanning | Production-grade LLM liberation

## Topics/Tags (10 recommended)

1. `abliteration`
2. `mechanistic-interpretability`
3. `llm`
4. `refusal-removal`
5. `fine-tuning`
6. `voice-llm`
7. `collaboration`
8. `security`
9. `pytorch`
10. `transformers`

## Branch Protection Rules

### Main Branch (`main`)

✅ **Require pull request reviews before merging**
- Required approving reviews: 1
- Dismiss stale reviews when new commits are pushed

✅ **Require status checks to pass**
- CI (Python 3.10, 3.11, 3.12)
- Linting (ruff)
- Tests (pytest)

✅ **Require branches to be up to date before merging**

✅ **Include administrators**

## GitHub Actions Workflows

### 1. CI (`.github/workflows/ci.yml`)
**Trigger**: Push to `main`, Pull Requests  
**Jobs**:
- Test on Python 3.10, 3.11, 3.12
- Lint with ruff
- Run pytest with coverage

### 2. Publish to PyPI (`.github/workflows/publish.yml`)
**Trigger**: Release published  
**Jobs**:
- Build package
- Publish to PyPI

**Required Secrets**:
- `PYPI_TOKEN`: PyPI API token

### 3. HuggingFace Space Auto-Sync (`.github/workflows/hf_sync.yml`)
**Trigger**: Push to `main` (changes in `vikrant_obl/`, `app.py`, `requirements.txt`)  
**Jobs**:
- Auto-push to HuggingFace Space

**Required Secrets**:
- `HF_TOKEN`: HuggingFace API token

## Repository Settings

### Features
- ✅ Issues
- ✅ Projects
- ✅ Wiki
- ✅ Discussions
- ✅ Preserve this repository (for archival)

### Pull Requests
- ✅ Allow squash merging
- ✅ Allow auto-merge
- ✅ Automatically delete head branches

### Pages (Optional)
- Deploy from: `gh-pages` branch
- Custom domain: `vikrant-obliteratus.ai` (if available)

## Labels

Create these labels for issue management:

- `bug` (red)
- `enhancement` (blue)
- `documentation` (green)
- `good first issue` (purple)
- `help wanted` (yellow)
- `research` (orange)
- `feature: fine-tuning` (cyan)
- `feature: voice` (magenta)
- `feature: collaboration` (teal)
- `feature: scanner` (brown)

## Issue Templates

Create `.github/ISSUE_TEMPLATE/`:

1. `bug_report.md`
2. `feature_request.md`
3. `research_question.md`
4. `commercial_license.md`

## Social Preview Image

Upload a social preview image (1280x640px) showing:
- vikrant-OBLITERATUS logo
- Key features (4 icons: Fine-tune, Voice, Collaborate, Scanner)
- Tagline: "Production-Grade LLM Abliteration"

## About Section

**Website**: https://huggingface.co/spaces/vikrant-project/vikrant-obliteratus  
**Topics**: (see above)  
**Releases**: Link to latest release  
**Packages**: Link to PyPI

## README Badges

Add to top of README:

```markdown
![PyPI](https://img.shields.io/pypi/v/vikrant-obliteratus)
![License](https://img.shields.io/github/license/vikrant-project/vikrant-OBLITERATUS)
![Tests](https://img.shields.io/github/actions/workflow/status/vikrant-project/vikrant-OBLITERATUS/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Space-yellow)
```

## Secrets to Configure

In Settings → Secrets and variables → Actions:

1. `PYPI_TOKEN`: Get from https://pypi.org/manage/account/token/
2. `HF_TOKEN`: Get from https://huggingface.co/settings/tokens
3. (Optional) `CODECOV_TOKEN`: For code coverage reporting

## Wiki Pages

1. **Home**: Project overview
2. **Installation Guide**: Detailed setup instructions
3. **API Reference**: Full API documentation
4. **Tutorials**: Step-by-step guides
5. **Research Papers**: Related academic work
6. **FAQ**: Common questions
7. **Commercial License**: How to purchase

## Recommended Integrations

- **Codecov**: Code coverage reporting
- **Dependabot**: Automated dependency updates
- **CodeQL**: Security scanning
- **pre-commit.ci**: Automated code formatting

## Star History

Add to README:

```markdown
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=vikrant-project/vikrant-OBLITERATUS&type=Date)](https://star-history.com/#vikrant-project/vikrant-OBLITERATUS&Date)
```

## Community Health Files

✅ LICENSE  
✅ README.md  
✅ CONTRIBUTING.md  
✅ SECURITY.md  
☐ CODE_OF_CONDUCT.md (use Contributor Covenant)  
☐ SUPPORT.md (link to Discussions)

## Release Workflow

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create Git tag: `git tag v2.0.0`
4. Push tag: `git push origin v2.0.0`
5. Create GitHub Release (triggers PyPI publish)
6. Announce on Twitter, Discord, HuggingFace

---

**All configured!** Repository is now production-ready.
