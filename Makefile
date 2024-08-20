D=docker
DS=docker system
DC=docker compose


## MAIN ##



## DOCKER ##
ps:
	sudo $(D) ps --all

images:
	sudo $(D) images --all


## DOCKER SYSTEM ##
prune:
	sudo $(DS) prune --volumes --force


## DOCKER COMPOSE ##
build:
	sudo $(DC) build

up:
	sudo $(DC) up --remove-orphans

upd:
	sudo $(DC) up --detach --remove-orphans

down:
	sudo $(DC) down

logs:
	sudo $(DC) logs --follow


## EXTENSION ##
rebuild: down build

reup: down up