#Alarm Predictor

Table of Contents

Getting started
Good to Know
Making code changes


Getting started

On your Linux machine

Open your favorite shell, for example, good old
Bourne Again SHell, aka, bash,
the somewhat newer
Z shell, aka, zsh,
or shiny new
fish.
Install Git by running
sudo apt install git-all on Debian-based
distributions like Ubuntu, or
sudo dnf install git on Fedora and closely-related
RPM-Package-Manager-based distributions like
CentOS. For further information see
Installing Git.
Add the public key of an existing or new public and private key pair to your
account on the
Fraunhofer GitLab
and add corresponding private key to the authentication agent by running
ssh-add ~/.ssh/${KEY}, where ${KEY} is the name of the private key.
Clone the source code by running
git clone git@gitlab.cc-asp.fraunhofer.de:ise621/sample-python-project.git
and navigate into the new directory sample-python-project by running
cd sample-python-project.
Prepare your environment by running cp ./.env.sample ./.env and adjusting
the copied environment file to your needs.


With Docker and GNU Make (the easy way but only possible on developer computers)

Install Docker Desktop, and
GNU Make.
List all GNU Make targets by running make help.
Drop into bash with the working directory /app, which is mounted to the
host's working directory, inside a fresh Docker container based on Debian
Linux everything installed by running make shell. If necessary, the Docker
image is (re)built automatically, which takes a while the first time.
Do something with the project like

running non-slow tests and doctests with make tests,
running slow and non-slow tests with make slowtests,
running doctests with make doctests,
type checking the code with make types,
linting the code with make lint,
finding dead code with make dead,
formatting the code with make format, and
generating documentation with make docs.


Drop out of the container by running exit or pressing Ctrl-D.


Without Docker (the hard way)


Install Python version 3.10.4
pip, and support for
Python virtual environments
by running, at least on Debian "bookworm",
apt-get install python3 python3-pip python3-venv.


Create a virtual environment by running
python3 -m venv ./.venv.


Activate the environment by running, on Windows,
.venv\Scripts\activate.bat, and, on Unix or MacOS, in
a bash shell
source ./.venv/bin/activate,
in a csh shell
source ./.venv/bin/activate.csh,
and in a fish shell
source ./.venv/bin/activate.fish.


Upgrade pip to version 22.1.1, and install
setuptools and
wheel by running
pip3 install --upgrade pip==22.1.1 setuptools wheel.


Install development tools, namely

the code formatter Black,
the static type checker mypy,
the testing automator pytest

the linter Pylint,
the dead code finder Vulture, and
the documentation creator Sphinx,

with pip by running
pip3 install -r requirements-development.txt.


Install the package's dependencies in requirements.txt with
pip by running
pip3 install -r requirements.txt.


Install the package in editable mode by running
pip3 install --editable ..


Do something with the project like

running non-slow tests with pytest ./tests,
running slow and non-slow tests with pytest --runslow ./tests,
running doctests with

pytest \
  --doctest-modules \
  --doctest-continue-on-failure \
  --assert=plain \
  -vvv \
  ./sample_python_project



type checking the code with mypy --strict .,
linting the code with pylint ./sample_python_project,
finding dead code with

vulture \
   --exclude ./sample_python_project/__init__.py,./tests/conftest.py,./docs/source/conf.py \
  .



formatting the code with black --target-version py37 ., and
generating documentation with

sphinx-apidoc -f -o ./docs/source ./sample_python_project
sphinx-build -b html ./docs/source ./docs/html






Deactivate the virtual environment by running deactivate.
