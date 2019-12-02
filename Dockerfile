FROM python:3.7.5-slim

ENV TZ America/Los_Angeles
ENV SERVICE ftw-etl

WORKDIR /opt/$SERVICE
ENV PYTHONPATH=/opt/$SERVICE

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && groupadd -r etl \
    && useradd -r -g etl etl

RUN apt-get update && apt-get install -y \
      cron \
      build-essential \
      software-properties-common \
      python3-software-properties \
      git

COPY requirements.txt /opt/$SERVICE/requirements.txt

RUN pip3 install -r requirements.txt

RUN rm -rf /var/lib/apt/lists/* \
    && apt-get remove -y \
      build-essential \
      git \
    && apt-get autoremove -y \
    && apt-get clean


# Covert everything above to base image

COPY . /opt/$SERVICE

RUN chown -R etl:etl /opt/$SERVICE
RUN python -m pip install --upgrade pip
CMD python bin/run.py