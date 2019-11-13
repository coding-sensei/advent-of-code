DOCKER_IMAGE = my_docker
DOCKER_ARGS := --rm -v $(CURDIR):$(CURDIR) -w $(CURDIR)
DOCKER_RUN = docker run -t $(DOCKER_ARGS) $(DOCKER_IMAGE)

enter_container: build_image
			docker run -it $(DOCKER_ARGS) $(DOCKER_IMAGE)

run: build_image
			$(DOCKER_RUN) $(command)

test: build_image
			$(DOCKER_RUN) pytest 2015/

check: build_image
			$(DOCKER_RUN) lint test

lint: build_image
			$(DOCKER_RUN) pylint 2018/*.py --disable=C0111,C0103,E0401,R1710,C0200,R0903

build_image: clean
			docker build -t $(DOCKER_IMAGE) .

.PHONY: clean
clean:
			$(DOCKER_RUN) find . -regextype posix-egrep -regex "(.*__pycache__$$)|(.*\.py[oc]$$)" -delete

get-%:
	./get_input.sh $*

