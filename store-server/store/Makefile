create-venv:
	python -m venv venv
activate-venv:
	source ./venv/bin/activate
install-django:
	pip install django==3.2
startproject:
	django-admin startproject projectname
startapp:
	django-admin startapp products
start-server:
	python manage.py runserver
python-console:
	python manage.py shell
make-migrations:
	./manage.py makemigrations
apply-migrations:
	./manage.py migrate
save-object:
	ProductCategory(product_name= 'Одежда', description= 'Описание для одежды').save()
create-superuser:
	./manage.py createsuperuser
dump-categories:
	./manage.py dumpdata products.ProductCategory > categories.json
dump-products:
	./manage.py dumpdata products.Product > prooducts.json
backup-fixtures-categories:
	./manage.py loaddata products/fixtures/categories.json
backup-fixtures-products:
	./manage.py loaddata products/fixtures/products.json