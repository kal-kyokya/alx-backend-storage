# 0x01. NoSQL

This directory is home to all files/scripts creating during learning and practicing on the topic of NoSQL through the tasks provided and assigned by ALX Africa (www.alxafrica.com) to the members of its specialization program in Software Engineering.

## Requirements

### MongoDB Command File

	->	All files will be interpreted/compiled on:
			* Ubuntu 18.04 LTS:
				Using:
					* MongoDB (version 4.2)
	->	All files should end with a new line
	->	The first line of all files should be a comment:
			* '// my comment'
	->	A README.md file, at the root of the folder of the project, is mandatory

### Python Scripts

	->	All files will be interpreted/compiled on:
			* Ubuntu 18.04 LTS
				Using:
					* python3 (version 3.7) and
					* PyMongo (version 3.10)
	->	All files should end with a new line
	->	The first line of all files should be exactly:
			* #!/usr/bin/env python3
	->	A README.md file, at the root of the folder of the project, is mandatory
	->	All code should use:
			* The pycodestyle style (version 2.5.*)
	->	All modules should have a documentation:
			python3 -c 'print(__import__("my_module").__doc__)'
	->	All functions should have a documentation:
			python3 -c 'print(__import__("my_module").my_function.__doc__)'
	->	All code should not be executed when imported, by using:
			'if __name__ == "__main__":'

## More Info

### Install MongoDB 4.2 in Ubuntu 18.04

Install MongoDB
```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
```
Check installation via status and version requests
```
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
```
Install pymongo
```
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

## Use “container-on-demand” to run MongoDB

* Ask for container Ubuntu 18.04 - MongoDB
* Connect via SSH
* Or via the WebTerminal
* In the container, you should start MongoDB before playing with it:

```
$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$
```
