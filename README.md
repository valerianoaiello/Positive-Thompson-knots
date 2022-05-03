# Positive Thompson Knots

## Start Project on Local Machine
### Create the Environment
```bash
python3 -m venv <env_folder>
```
### Activate Environment
```bash
source <env_floder>/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Start main.py
```bash
python src/main.py
```

## Update Dependencies
### Install New Package
```bash
pip install <package_name>
```
### Update requirements.txt
```bash
pip freeze > requirements.txt
```
## Utilities
### Programming Structure
- https://en.wikipedia.org/wiki/Formal_grammar
- https://en.wikipedia.org/wiki/Binary_tree
### Git
If you want to push your changes to the remote branch:
- add files in stage:
```bash
git add <file_1> <file_2> ... <file_n>
```
- commit changes:
```bash
git commit -m "Commit message"
```
- push changes to remote repository
```bash
git push
```

If you want to update your local branch to the new version:
```bash
git pull
```
