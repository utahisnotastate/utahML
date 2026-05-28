# Releasing utahML

This project can be released to GitHub and PyPI with the following sequence.

## 1) Prerequisites

- Python 3.9+
- `git` authenticated for `utahisnotastate/utahML`
- PyPI API token with publish rights for `utahml`

Install tools:

```bash
py -m pip install --upgrade build twine
```

## 2) Build and verify package

```bash
py -m build
py -m twine check dist/*
```

## 3) Publish to PyPI

Use a token from [PyPI account settings](https://pypi.org/manage/account/token/):

```bash
py -m twine upload dist/*
```

If prompted:

- username: `__token__`
- password: `<your-pypi-token>`

## 4) Push to GitHub

```bash
git add .
git commit -m "release: polish docs, packaging, and watcher workflow"
git push origin main
```

## 5) Tag release

```bash
git tag v1.1.0
git push origin v1.1.0
```

## 6) Optional: create GitHub release

Create a release from tag `v1.1.0` with highlights:

- multi-audience docs and tutorials under `docs/`
- enhanced `.gitignore` hygiene
- packaging metadata + modern `pyproject.toml`
- watcher-ready `; wishes` workflow docs
