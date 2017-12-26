# Contributing

Follow these guidelines if you'd like to contribute to the project!

---

### Table of Contents

Read through these guidelines before you get started:

1. [Questions & Concerns](#questions--concerns)
2. [Issues & Bugs](#issues--bugs)
3. [Feature Requests](#feature-requests)
4. [Submitting Pull Requests](#submitting-pull-requests)
5. [Code Style](#code-style)

### Questions & Concerns

If you have any questions about using or developing for this project, reach out
to @{user} or send an [email][1].

### Issues & Bugs

Submit an [issue][2] or [pull request][3] with a fix if you find any bugs in
the project. See [below](#submitting-pull-requests) for instructions on sending
in pull requests, and be sure to reference the [code style guide](#code-style)
first!

When submitting an issue or pull request, make sure you're as detailed as possible
and fill in all answers to questions asked in the templates. For example, an issue
that simply states "X/Y/Z isn't working!" will be closed.

### Feature Requests

Submit an [issue][2] to request a new feature. Features fall into one of two
categories:

1. **Major**: Major changes should be discussed with me via [email][1]. I'm
always open to suggestions and will get back to you as soon as I can!
2. **Minor**: A minor feature can simply be added via a [pull request][3].

### Submitting Pull Requests

Before you do anything, make sure you check the current list of [pull requests][4]
to ensure you aren't duplicating anyone's work. Then, do the following:

1. Fork the repository and make your changes in a git branch: `git checkout -b my-branch base-branch`
2. Read and follow the [code style guidelines](#code-style).
3. Make sure your feature or fix doesn't break the project! Test thoroughly.
4. Commit your changes, and be sure to leave a detailed commit message.
5. Push your branch to your forked repo on GitHub: `git push origin my-branch`
6. [Submit a pull request][3] and hold tight!
7. If any changes are requested by the project maintainers, make them and follow
this process again until the changes are merged in.

### Code Style

Please follow the coding style conventions detailed below:

{guidelines}

[1]: mailto:{bart@mikasoftware.com}
[2]: https://github.com/mikasoftware/mortgagekit-py/issues/new
[3]: https://github.com/mikasoftware/mortgagekit-py/compare
[4]: https://github.com/mikasoftware/mortgagekit-py/pulls

### Developers Notes
If you would like to contribute to this project, and you are new to developing open source projects with Django, this article is for you; furthermore, misc related info is posted here.

#### Installation
1. Clone the project to your local development folder.

  ```bash
  git clone https://github.com/MikaSoftware/django-trapdoor.git
  ```

2. Setup our virtual environment

  ``bash
  virtualenv -p python3.6 env
  ```

3. Activate virtual environment

  ```bash
  source env/bin/activate
  ```

4. Run the following commands to install dependent libraries.

  ```bash
  pip install -r requirements
  pip install django
  ```

5. Create our sample ``Django`` project as a harness for our library. Just FYI, do not worry about having a django web-app in this library as we have updated the ``.gitignore`` to not have any of the django stuff except code related to our library. Also note that the period in this command is not a mistake, it will create the project inside this directory. If you would like to learn more, read about the [startproject](https://docs.djangoproject.com/en/dev/ref/django-admin/#startproject) command.

  ```bash
  django-admin startproject sample_project .
  ```

6. Add ``starterkit`` to your ``INSTALLED_APPS``.

7. Finally run the following in your console

  ```bash
  python manage.py migrate
  ```

8. You are ready to start programming! Here are some commands to get you started.

  ```bash
  python manage.py test
  python manage.py runserver
  ```

#### Versioning
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.
