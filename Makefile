run:
	python2 manage.py runserver
makemigr:
	python2 manage.py makemigrations vdag
migr:
	python2 manage.py migrate
shell:
	python2 manage.py shell
migrDB:
	make makemigr
	make migr
clean:
	rm vdag/migrations/000*
superuser:
	python2 manage.py createsuperuser
