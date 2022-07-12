FROM node:14-slim

ARG root_dir=/opt/frontend
ARG env

RUN set -eux; \
    apt-get update; \
    apt-get install  -y --no-install-recommends \
            locales; \
    locale-gen ja_JP.UTF-8;

WORKDIR $root_dir/app

COPY ./docker-entrypoint.sh $root_dir
COPY ./$env/docker-command.sh $root_dir


ENTRYPOINT ["/opt/frontend/docker-entrypoint.sh"]
CMD ["/opt/frontend/docker-command.sh"]
