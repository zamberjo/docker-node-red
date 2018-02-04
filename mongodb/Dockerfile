FROM mongo:3.6.2-jessie

COPY docker-healthcheck /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-healthcheck

HEALTHCHECK --interval=5s --timeout=5s --retries=3 CMD ["docker-healthcheck"]

CMD mongod --smallfiles --logpath=/dev/null # --quiet
