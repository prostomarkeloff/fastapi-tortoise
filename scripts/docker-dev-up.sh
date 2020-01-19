#!/usr/bin/env bash

force_recreate=$1
if [ ! "$force_recreate" ]
then
  docker-compose -f docker-compose-dev.yml up -d --build
else
  docker-compose -f docker-compose-dev.yml up -d --build --force-recreate
fi
