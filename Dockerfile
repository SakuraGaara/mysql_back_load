FROM python:3.6-alpine3.13

MAINTAINER SakuraGaara

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories && \
    apk add tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    mkdir -p /mysql_back_load /data/backup

WORKDIR /mysql_back_load

ADD ./ /mysql_back_load/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "auto.py"]