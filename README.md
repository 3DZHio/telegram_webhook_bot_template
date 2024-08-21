![Static Badge](https://img.shields.io/badge/Python-008000?style=for-the-badge&logo=python&logoColor=white&link=https://www.python.org/downloads/)
![Static Badge](https://img.shields.io/badge/ReDiS-d92b09?style=for-the-badge&logo=redis&logoColor=white&link=https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/)
![Static Badge](https://img.shields.io/badge/PostgreSQL-3a6790?style=for-the-badge&logo=postgresql&logoColor=white&link=https://www.postgresql.org/download/linux/)

## 🔗 REPOSITORY

```shell
git clone https://github.com/3DZHio/telegram_webhook_bot_template.git
cd telegram_webhook_bot_template
mv .env.example .env
```

---

## ⚙️ DEPENDENCIES

### [Install Docker](https://www.docker.com/)

### SSL Certificate ( Make Sure it works correctly | Remove --dry-run )

```shell
EMAIL=
DOMAIN=

# Get #
sudo docker run \
  --publish "80:80" \
  --volume "./data/ssl:/etc/letsencrypt" \
  certbot/certbot \
  certonly --dry-run --standalone --email "${EMAIL}" --agree-tos --domain "${DOMAIN}"

# Renew #
sudo docker run --name "${DOMAIN}" --detach \
  --publish "8000:80" \
  --volume "./data/ssl:/etc/letsencrypt" \
  certbot/certbot \
  renew --dry-run --quiet --pre-hook "nginx stop" --post-hook "nginx start"
```

### Fill .env

---

## 📦 DOCKER

### 🚀 Build and Up

```shell
make build up
```

### 🛑 Down

```shell
make down
```

### 📌 MakeFile Info

```shell
cat Makefile
```

---