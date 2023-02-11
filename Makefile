download.model.all:
	 download.model.18 download.model.50

download.model.18:
	wget https://dl.dropboxusercontent.com/s/dlww6malzd6pwtj/FRCNN-R18.pth

download.model.50:
	wget https://dl.dropboxusercontent.com/s/y3jmxt69p9uswnc/FRCNN-R50.pth

setup.all:
	pip install icevision[all]
	pip install icevision[all]

sibi.run:
	python3 app.py

sibi.all:
	setup.all
	download.model.all
	sibi.run

docker.build:
	docker-compose build

docker.run:
	docker-compose run --rm -d icevision

docker.all:
	docker.build docker.run