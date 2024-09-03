#!/bin/bash


## Variables ##
source .env 2>/dev/null || source .env.example


## ReName .env.example To .env ##
if [ -f .env.example ]; then
  mv .env.example .env
fi


## GitIgnore ##
if [ "${SAVE_ENV}" == "1" ]; then
    sed -i "s/^.env$/##.env/" .gitignore
fi


## Redis Memory OverCommit ##
if [ "$(sudo cat /proc/sys/vm/overcommit_memory)" != "1" ]; then
    echo 1 | sudo tee /proc/sys/vm/overcommit_memory
fi


## SSL Certificate ##
sudo docker run --rm \
  --publish "80:80" \
  --volume "./init/ssl:/etc/letsencrypt" \
  certbot/certbot \
  certonly "$(if [ "${DRY_RUN}" == "1" ]; then echo "--dry-run"; fi)" --non-interactive --standalone --email "${EMAIL}" --agree-tos --domain "${WEBHOOK_DOMAIN}"
