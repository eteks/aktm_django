# ahkrweb
ENVIRONMENT SETUP :-
	sudo apt-get install python3-pip
	pip3 install virtualenv
	pip install --upgrade pip
	python3 -m virtualenv django111
	source django111/bin/activate
	pip install django==1.11.4
	sudo apt-get install python3-dev libmysqlclient-dev
	pip install mysqlclient
	pip install Pillow
	pip install django-suit==0.2.25

CREATE PROJECT:-
	django-admin startproject ahkrweb

