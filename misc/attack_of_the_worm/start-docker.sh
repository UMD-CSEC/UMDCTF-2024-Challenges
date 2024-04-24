#!/bin/sh
docker container rm -f attack_of_the_worm
docker run -d -p7274:7274 --restart=always --name=attack_of_the_worm --privileged attack_of_the_worm