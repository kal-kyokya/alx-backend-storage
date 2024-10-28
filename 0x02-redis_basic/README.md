# 0x02. Redis Basic

This directory is home to all files and script generated during completion of the Redis related tasks by ALX Africa (www.alxafrica.com) to its Software Engineering Specialization program.

## Requirements

	->	All of files will be interpreted/compiled on:
			* Ubuntu 18.04 LTS
				using:
					* python3 (version 3.7)
	->	All of files should end with a new line
	->	A README.md file, at the root of the folder of the project, is mandatory
	->	The first line of all files should be exactly:
			* #!/usr/bin/env python3
	->	All code should use:
			* The pycodestyle style (version 2.5)
	->	All modules should have documentation:
			* python3 -c 'print(__import__("my_module").__doc__)'
	->	All classes should have documentation:
			python3 -c 'print(__import__("my_module").MyClass.__doc__)'
	->	All functions and methods should have documentation:
			* python3 -c 'print(__import__("my_module").my_function.__doc__)'
			* python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
	->	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method
	->	All functions and coroutines must be type-annotated.

Install Redis on Ubuntu 18.04

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
