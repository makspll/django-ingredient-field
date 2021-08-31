PACKAGE_DIR="./django-ingredient-field"
MKFILE_PATH=$(shell pwd)
buildpip:
	pip uninstall --yes django-ingredient-field;
	cd $(PACKAGE_DIR) && python setup.py sdist && python setup.py install;
test: 
	coverage run --branch --include=/**/dj_ingredient_field/*.py --omit=**admin*,**apps*,**tests*,**enums* manage.py test dj_ingredient_field --nocapture;
migrate:
	python manage.py makemigrations dj_ingredient_field
coverage: test
	coverage html
	coverage xml
coverage-open: coverage 
	-open "$(MKFILE_PATH)/htmlcov/index.html"
	-xdg-open $(MKFILE_PATH)/htmlcov/index.html;
docs:
	cd ${PACKAGE_DIR}/docs && make html
docs-open: docs
	-open ${PACKAGE_DIR}/docs/_build/html/index.html;
	-xdg-open ${PACKAGE_DIR}/docs/_build/html/index.html;