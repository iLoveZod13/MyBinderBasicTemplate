FROM python:3.8-slim
# install the notebook package
RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache notebook && \
    pip install --no-cache numpy==1.18.5 && \
    pip install --no-cache pandas==1.0.4 && \
    pip install --no-cache xlrd==1.2.0 && \
    pip install --no-cache jupyter_contrib_nbextensions && \
    pip install --no-cache jupyter-offlinenotebook

# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
USER ${USER}

RUN jupyter-contrib-nbextension install --user

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
