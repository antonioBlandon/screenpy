# Screenpy

This repository was created to practice with Screenpy framework.
In this repository you can find out three kind of framework uses.

1. API test automation (api) 
2. Web app test automation (web)
3. Mobile app test automation (mobile)

## Project structure
## Tools

- [Python 3.7.9](https://www.python.org/)
- [Pip 22.0.4](https://pypi.org/project/pip/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Screenpy](https://screenpy-docs.readthedocs.io/en/latest/)
- [Pycharm community edition](https://www.jetbrains.com/pycharm/download/#section=windows)

## Config Project
This repository was work on Windows, then the below configuration is focus on Windows. 
I recommend [this tutorial](https://platzi.com/clases/1540-flask/18833-instalacion-de-python-pip-y-virtualenv/?utm_source=google&utm_medium=cpc&utm_campaign=17739691128&utm_adgroup=&utm_content=&gclid=Cj0KCQiAsdKbBhDHARIsANJ6-jfNmCSIyDqAeeDWsCcQaswT1DE5N7W0TLFzrSWfbYI6_e6o1X8yQegaAi0QEALw_wcB&gclsrc=aw.ds) 
like pre-steps. Besides, please, you should run the next commands on project root.

1. **Create environment**:

    `python -m venv env`

You could need to use python3, it depends on your python installation.

2. **Launch environment**:

    `env/Scripts/activate`

3. **Install dependencies**:

   `pip install -r requirements.txt`

4. **Execute test**

    `python -m pytest -v api/features/get_single_user.py --alluredir allure_report`

5. **Launch report**

   `allure serve allure_report`

6. **Clean report**

   `allure generate --clean --output allure_report`

7. **Exit environment**

   `deactivate`

## Execute Test
## Extra documentation
