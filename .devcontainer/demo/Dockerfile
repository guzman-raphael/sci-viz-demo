# Note: You can use any Debian/Ubuntu based image you want. 
FROM mcr.microsoft.com/devcontainers/python:3.7-bullseye

RUN \
    apt update && \
    apt-get install bash-completion graphviz default-mysql-client -y && \
    pip install black faker ipykernel datajoint

ENV PHARUS_HOST fakeservices.datajoint.io
ENV PHARUS_USER root
ENV PHARUS_PASSWORD simple
