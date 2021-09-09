# Gpy-mail

Basic program for managing events through Google's gmail API

## Description

is currently able establish API connection and send emails based on YAML file specified as an argument

## Getting Started

### Dependencies

* Python 3 or greater.
* The pip package management tool
* A Google Cloud Platform project with the API enabled. To create a project and enable an API, refer to Create a project and enable the API
* enable the "Gmail API".
* Authorization credentials for a desktop application. To learn how to create credentials for a desktop application, refer to Create credentials.
* A Google account with Gmail enabled.

### Installing

* Install pip for python 3
* (recommended) Create Python [Virtual Environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments) to locally install dependencies and run code --- on Unix-like OS, run
```
python3 -m venv env
source env/bin/activate
```
* From within virtual environment, install  dependencies with:
```
(env)[user@host]$ pip install -r requirements.txt
```


### Executing program

* How to run the program
* Step-by-step bullets
```
python main.py sample_email.yml
```

## Help

Any advise for common problems or issues.


## Authors

Contributors names and contact info

ex. Christopher Rock

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [gmail-python-quickstart](https://github.com/googleworkspace/python-samples/tree/master/gmail/quickstart)