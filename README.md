# Python Web App

Simple Python application to handle message submissions from users. 


## Getting Started

This is a simple Python REST application allows users to post messages, search messages, delete messages and also to list all existing messages. This also identifies if the message is a Palindrome or not. App is setup using Flask, it is a web framework written in Python.


### Prerequisites

This app is designed to run on a Docker environment. You need to have a system with Docker service running.

```
# docker -v
Docker version 18.09.0, build 4d60db4
```


### Installation and Setup

Download docker-compose.yml from git repo and run below command to start the App service within Docker enviroinment,


```
# docker-compose -f docker-compose.yml up -d
Creating network "webapp_default" with the default driver
Creating webapp_db_1_87403bd3da0d ... done
Creating webapp_app_1_58c70b5770b6 ... done
```

You will see following Docker instances on your machine and the App instance is listening on port 80,

```
# docker ps
CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS              PORTS                  NAMES
bfade4e32f90        vipinmadhav90/webapp:4.0   "python app.py"          10 minutes ago      Up 10 minutes       0.0.0.0:80->8080/tcp   webapp_app_1_3aab962a5c84
e8be03c8ca87        mariadb:latest             "docker-entrypoint.s…"   10 minutes ago      Up 10 minutes       3306/tcp               webapp_db_1_b9b41899bf7f
```

This will make the App online and you can access it using  URL http://my-website.com


## Features

Following features are available with this App,

* Allows users to submit/post messages
* Lists received messages
* Retrieves a specific message on demand, and determines if it is a palindrome.
* Allows users to delete specific messages


## Deployment

Python App is dockerized to make the App setup easier. This App is configured with two docker images - first one for database(MariaDB is used) and another for the Python code running(CentOS image is used here).

## Built With

* Flask - The web framework used

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details

