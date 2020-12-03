FROM python:3.7.3

MAINTAINER jason <jinsong@shanshu.ai>

RUN apt-get -y update && apt-get install -y \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install numpy==1.16.2 scipy==1.2.1 scikit-learn==0.20.2 lightgbm xgboost pandas flask gevent gunicorn && \
    rm -rf /root/.cache

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY funsion_model /opt/program

WORKDIR /opt/program

