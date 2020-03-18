********************
Empezando con python
********************

Cómo preparar un entorno virtual
================================

``virtualenv MyVE``

``source MyVE/bin/activate``

``pip install -r requirements.txt``



Virtualenvwrapper
=================

mkdir ~/.virtualenvs

apt install virtualenvwrapper
pip install virtualenvswrapper

si no está el pip, instalar: (virtualenv y python-setuptools)

sudo apt install python3-pip


----------poner esto en .bashrc
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
export VIRTUALENVWRAPPER_PYTHON=$(which python3)                                                                                      

Que puede fallar:

1) virtualenvwrapper

La ubicacion del script virtualenvwrapper.sh depende de la
distribucion de linux:

Mint:
source /usr/local/bin/virtualenvwrapper.sh

CBPP:
source $HOME/.local/bin/virtualenvwrapper.sh


1) virtualenv

en la variable VIRTUALENVWRAPPER_VIRTUALENV
poner la ubicación de virtualenv:

$ which virtualenv


3) python

Si da este error:

 source $HOME/.local/bin/virtualenvwrapper.sh
/usr/local/bin/python3: Error while finding module specification for 'virtualenvwrapper.hook_loader' (ModuleNotFoundError: No module named 'virtualenvwrapper')
virtualenvwrapper.sh: There was a problem running the initialization hooks.

If Python could not import the module virtualenvwrapper.hook_loader,
check that virtualenvwrapper has been installed for
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 and that PATH is
set properly.

probar hacer esto:

reemplazar:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
por:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python


Mode info `here <https://stackoverflow.com/questions/33216679/usr-bin-python3-error-while-finding-spec-for-virtualenvwrapper-hook-loader>`_.


LEARN MORE:
`Command reference for wirtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html>`_

`Virtualenvwrapper readthedics <https://virtualenvwrapper.readthedocs.io/en/latest/>`_


Cómo se usa:

* workon
* mkvirtualenv --python=$(which python3) MyVE
* lsvirtualenv
* workon MyVE
* rmvirtualenv MyVE




Usando git con GitHub
=====================


Un buen tutorial sobre `GitHub <https://guides.github.com/introduction/flow/>`_.


En la version simple, cuando solo un usuario edita:

1. git clone (one time only)
2. git pull
3. edit files
4. add files to the version control stack
5. commit changes
6. push changes
7. go to 2.

 

Varios usuarios:

1. git clone (one time only)
2. git pull
3. edit files
4. add files to the version control stack
5. before commit, git pull and resolve conflicts (if any)
5. commit changes
6. push changes
7. go to 2.

 
