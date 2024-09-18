FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

RUN apt-get update && apt-get install --no-install-recommends -y \
    libblas3 \
    libcliquer1 \
    libgfortran5 \
    libgsl25 \
    liblapack3 \
    libopenblas0 \
    libtbb2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -P /tmp/ https://github.com/scipopt/scip/releases/download/v911/SCIPOptSuite-9.1.1-Linux-debian11.deb
RUN dpkg -i /tmp/SCIPOptSuite-9.1.1-Linux-debian11.deb \
    && rm /tmp/SCIPOptSuite-9.1.1-Linux-debian11.deb
