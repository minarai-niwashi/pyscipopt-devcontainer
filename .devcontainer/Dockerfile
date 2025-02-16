FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

RUN apt-get update && apt-get install --no-install-recommends -y \
    libblas3=3.9.0-3+deb11u1 \
    libcliquer1=1.21-2 \
    libgfortran5=10.2.1-6 \
    libgslcblas0=2.6+dfsg-2 \
    libgsl25=2.6+dfsg-2 \
    liblapack3=3.9.0-3+deb11u1 \
    libopenblas0=0.3.13+ds-3+deb11u1 \
    libtbb2=2020.3-1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -P /tmp/ https://github.com/scipopt/scip/releases/download/v911/SCIPOptSuite-9.1.1-Linux-debian11.deb \
    && dpkg -i /tmp/SCIPOptSuite-9.1.1-Linux-debian11.deb \
    && rm /tmp/SCIPOptSuite-9.1.1-Linux-debian11.deb

ARG USERNAME=vscode
USER $USERNAME
