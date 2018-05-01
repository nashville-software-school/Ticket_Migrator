# Nashville Software School Instructor Issue Migrator
:construction: WIP :construction:

Team Leads: [Meg Ducharme](https://github.com/megducharme), [Steve Brownlee](https://github.com/stevebrownlee)

Willed to life by: [Chris Miller](https://github.com/camilleryr), [Garrett Ward](https://github.com/Gward2489), [Peter Forrest](https://github.com/RillistikPete), [John Dulaney](https://github.com/john-dulaney), [Kolden Prue](https://github.com/KAPrueved), and [Jared Fuller](https://github.com/jaredshane).

## Overview
This application was developed by Nashville Software School graduates for use by the instructors. Its function is to facilitate certain GitHub processes for instructors. The application eliminates steps for instructors to delegate project issues to multiple student / team repositories.

---
## Getting Started
The application will be hosted [here](migrator.bangazon.com). (:construction: currently not online :construction:)

This application assumes Git has been installed previously. Follow [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for help with Git.

In order to run the application, it is also assumed that you have a grasp of terminal and have a package manager (This walkthrough will use Node.js's package manager NPM [Download that here](https://nodejs.org/en/)).

Requires installation of the latest version of Python - [Download Python version 3.6.5](https://www.python.org/downloads/).

PIP (Python Installation Package) should be included with Python installation. For help with installation follow [this link](https://docs.python.org/3/installing/).

Requires installation of ```pipenv```.

On MacOS:
```
brew install pipenv
```
Otherwise:
```
pip install pipenv
```




### The first step is cloning the repository to your local machine.

1. Navigate to the directory where you wish to install the application and type:
```
git clone origin git@github.com:PythonWizards/Ticket_Migrator.git
```
2. When download is complete, type `cd ./ticket_migrator/migrator_app/static/migrator_app`, then type  `npm i`. This will install any package dependencies. 

3. Navigate back to the folder that contains the file `manage.py`.

4. Next, enter virtual environment by typing `pipenv shell`.

5. Install environment packages/dependencies by running the command `pipenv install`.

6. Finally we run the application using `python manage.py runserver` and navigate in `127.0.0.1.8000` in a web browser.

:fire: Bazinga. You're in.

---
## Technology Used to create this application

1. [NodeJs](https://nodejs.org/en/)
1. [Python version 3.6.5](https://www.python.org/downloads/)
1. [Visual Studio Code](https://code.visualstudio.com/)
1. [NPM](https://www.npmjs.com/)
1. [Django](https://www.djangoproject.com/start/)
1. [JavaScript](https://www.javascript.com/)
1. [Bulma](https://bulma.io//)
1. [HTML5](https://www.w3.org/TR/html5/)
1. [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
1. [Dragula](https://github.com/bevacqua/dragula)
1. [Jquery](https://jquery.com/)
1. [Git](https://git-scm.com/)
1. [GitHub](https://github.com/)