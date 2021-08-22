PACKAGE_DIR="./django-ingredient-field"

buildpip:
	pip uninstall django-ingredient-field;
	cd $(PACKAGE_DIR) && python setup.py sdist && python setup.py install;
test: buildpip 
	coverage run python manage.py test dj_ingredient_field sample_app;
coverage: test
	coverage report
	coverage html