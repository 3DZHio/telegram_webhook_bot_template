S=sudo
E=@echo
D=docker
DS=docker system
DC=docker compose


## DOCKER ##
ps:
	$(S) $(D) ps --all

rm:
	$(E) USAGE: make rm id=
	$(S) $(D) rm --force $(id)

images:
	$(S) $(D) images --all

rmi:
	$(E) USAGE: make rmi id=
	$(S) $(D) rmi --force $(id)


## DOCKER SYSTEM ##
prune:
	$(S) $(DS) prune --volumes --force


## DOCKER COMPOSE ##
build:
	$(S) $(DC) build

up:
	$(S) $(DC) up --remove-orphans

upd:
	$(S) $(DC) up --detach --remove-orphans

down:
	$(S) $(DC) down

logs:
	$(S) $(DC) logs --follow


## EXTENSION ##
rebuild: down build

reup: down up