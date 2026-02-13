FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

RUN rm -f /etc/apt/sources.list.d/yarn.list /etc/apt/sources.list.d/yarn*.list || true

RUN apt-get update && apt-get install --no-install-recommends -y \
    libblas3 \
    libcliquer1 \
    libgfortran5 \
    libgslcblas0 \
    libgsl25 \
    liblapack3 \
    libopenblas0 \
    libtbb2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -P /tmp/ https://github.com/scipopt/scip/releases/download/v911/SCIPOptSuite-9.1.1-Linux-debian11.deb \
    && dpkg -i /tmp/SCIPOptSuite-9.1.1-Linux-debian11.deb \
    && rm /tmp/SCIPOptSuite-9.1.1-Linux-debian11.deb

ARG USERNAME=vscode
USER $USERNAME
