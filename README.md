# Python Web App

Simple Python application to handle message submissions from users. 

## Getting Started

This is a simple Python REST application Allows users to post messages, search messages, delete messages and also to list all existing messages. This also identifies if the message is a Palindrome or not. 

### Prerequisites

This app is designed to run on a Docker environment. You need to have a system with Docker service running.

```
# docker -v
Docker version 18.09.0, build 4d60db4
```

### Installation and Setup

Download docker-compose.yml from my git repo and run below command to run the service inside Docker enviroinment,


```
# docker-compose -f docker-compose.yml up -d
Creating network "webapp_default" with the default driver
Creating webapp_db_1_87403bd3da0d ... done
Creating webapp_app_1_58c70b5770b6 ... done
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
