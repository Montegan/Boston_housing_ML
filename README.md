# Boston Housing ML End to End Project

## Software And Tools Requirements

1. [Github](https://github.com) Account
2. [Herouku](https://heroku.com) Account
3. [IDE](https://code.visualstudio.com/) depends on personal preference
4. [Git](https://git-scm.com/downloads) CLI

## Building Process

### Step 1: Create a new environment and activate

```
$ python -m venv env_name
```

activate (cmd)

```
$ env_name\Scripts\activate
```

activate (powershell)

```
$ .\myenv\Scripts\Activate.ps1
```

### Step 2: Create a requirements.txt file

Put all the neccessary packages used in the project in "requirements.txt" for ease of installation and management in the future.

```
$ pip install -r requirments.txt
```

If you've already installed your packages in a virtual environment, you can auto-generate the file:

```
pip freeze > requirements.txt
```
