export LC_CTYPE="en_US.UTF-8"

migrate:
	python src/manage.py migrate

run:
	@cd src && python manage.py runserver

css:
	sh ./build_css.sh


clean:
	find . -name "*.pyc" -delete

deps:
	yarn
	pip install -r requirements.txt
	make css
	make migrate
	python src/manage.py collectstatic --noinput --clear
	# python src/manage.py compress
