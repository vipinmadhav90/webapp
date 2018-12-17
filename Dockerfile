FROM centos:7

MAINTAINER Vipin M "vipinmadhav90@gmail.com"

RUN yum update -y && \
    yum -y install epel-release && \
    yum -y install python-pip MySQL-python

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

EXPOSE 8080

RUN pip install -r requirements.txt

COPY . /webapp

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
