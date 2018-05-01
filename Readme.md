# Nashville Software School Instructor Issue Migrator

Team Leads: [Meg Ducharme](https://github.com/megducharme), [Steve Brownlee](https://github.com/stevebrownlee)

Willed to life by: [Chris Miller](https://github.com/camilleryr), [Garrett Ward](https://github.com/Gward2489), [Peter Forrest](https://github.com/RillistikPete), [John Dulaney](https://github.com/john-dulaney), [Kolden Prue](https://github.com/KAPrueved), and [Jared Fuller](https://github.com/jaredshane).

## Overview
This application was developed by Nashville Software School graduates for use by the instructors. Its function is to facilitate certain GitHub processes for instructors. The application eliminates steps for instructors to delegate project issues to multiple student / team repositories.

---
## Getting Setup
The application is hosted [here](migrator.bangazon.com). (:construction: currently not online :construction:)

This application assumes Git has been installed previously. Follow [this link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for help with Git.

In order to run the application, it is also assumed that you have a grasp of terminal and have a package manager. To get set up we need to install the following 4 dependencies. 

1. Node.js's package manager NPM [Download here](https://nodejs.org/en/).

1. Requires installation of the latest version of Python - [Python version 3.6.5](https://www.python.org/downloads/).

1. PIP (Python Installation Package) should be included with Python installation. For help with installation follow [this link](https://docs.python.org/3/installing/).

1. Requires installation of ```pipenv```.

    On MacOS: Enter `brew install pipenv` in the terminal.

    Otherwise: Enter `pip install pipenv`
 

## Running the App

1. Navigate to the directory where you wish to install the application and type:
```
git clone origin git@github.com:PythonWizards/Ticket_Migrator.git
```
1. When download is complete, type `cd ./ticket_migrator/migrator_app/static/migrator_app`, then type  `npm i`. This will install any package dependencies. 

1. Navigate back to the folder that contains the file `manage.py`.

1. Enter `python manage.py migrate`. Something similar to the following will appear indicating a successful migration:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, migrator_app, sessions
Running migrations:
  Applying migrator_app.0007_auto_20180501_1502... OK
```

1. Next, enter virtual environment by typing `pipenv shell`.

1. Install environment packages/dependencies by running the command `pipenv install`.

1. Finally we run the application using `python manage.py runserver` and navigate in `127.0.0.1.8000` in a web browser.

:fire: Bazinga. You're in.

---

## Using the Application

Once opened in your browser, the application will be directed to the login page.

1. Login or create an account by clicking `Register`.

1. Follow steps to register new user. GitHub Personal Access Token is required to authenticate to GitHub when:
    - You're using two-factor authentication
    - Accessing protected content in an organization that uses SAML single sign-on (SSO). Tokens used with organizations that use SAML SSO must be authorized.

1. Navigate to GitHub in a new tab. In the upper-right corner of any page, click your profile photo, then click **Settings**.
1. In the left sidebar, click **Developer settings**.
1. In the left sidebar, click **Personal access tokens**.
1. Click **Generate new token**.
1. Give your token a descriptive name.
1. Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select repo.
1. Click **Generate token**.
1. Copy the token to your clipboard. For security reasons, after you navigate off the page, you will not be able to see the token again.
1. Once you have pasted the token into the register page, click **Create Account**.

### Home Page

Upon creating an account, the user will be directed to the application home page.  Here the user is presented with the option to select a source repository from which to pull issues to create a new sprint. If any sprints have been previously created, they will be displayed in the **Saved Sprints** section, where the user can click `Migrate` or `Details`.
(To edit your access token, click `Profile` in the top right of the page next to `Login`.)

### Drag and Drop Issues Page

Once a source repository is selected and the user clicks **Select**, the user will be directed to the "drag and drop" page.  Here you must enter a **Sprint Name** and drag any issues from the box on the right into the box on the left.  The left container will migrate all dropped issues into the saved sprint upon clicking **Save Sprint**.

`Sprint Saved` will appear in a modal with three options:
    - **Home**: navigate to home page, where the saved sprint will be **Saved Sprints** section.
    - **Create Additional**: refreshes the drag and drop page to create an additional sprint.
    - **Migrate**: will direct user to migrate page (Once user selects **OK** on migrate page, the sprint will no longer be shown on home page under **Saved Sprints**).

### Migrate Page

On the migrate page, user will see the Sprint name, repository link, and all issues selected in previous page.  The user will be prompted to select target reposotory/repositories (into which the sprint issues will be migrated).

Upon clicking **OK**, a loading screen (GIF) will appear.  Once complete, the user will see a "SUCCESS" page indicating a successful migration. :smiley:










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