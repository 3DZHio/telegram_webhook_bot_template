## VARIABLES ##
S=sudo
E=@echo
D=docker
DC=docker compose


## DOCKER ##
ps:
	$(S) $(D) ps --all

rm:
	$(E) USAGE: make rm rm=
	$(S) $(D) rm --force $(rm)

images:
	$(S) $(D) images --all

rmi:
	$(E) USAGE: make rmi rmi=
	$(S) $(D) rmi --force $(rmi)

prune:
	$(S) $(D) system prune --volumes --force


## DOCKER COMPOSE ##
build:
	$(S) $(DC) build

up:
	$(S) $(DC) up --detach --remove-orphans

down:
	$(S) $(DC) down

logs:
	$(E) USAGE: make logs logs=
	$(S) $(DC) logs --follow $(logs)