FROM python:3.10.5-slim-bullseye

ARG root_dir=/opt/backend
ARG user
ARG user_id
ARG env
WORKDIR $root_dir/app

ENV HOME /home/$user
ENV PATH $HOME/.local/bin:$PATH

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
    gettext; \
    pip install -U pip; \
    useradd -m $user -p $user -u $user_id; \
    chown $user -R $HOME; \
    chown $user -R $root_dir;

USER $user

COPY ./docker-entrypoint.sh $root_dir
COPY ./$env/docker-command.sh $root_dir

ENTRYPOINT ["/opt/backend/docker-entrypoint.sh"]
CMD ["/opt/backend/docker-command.sh"]
