# ssh2docker
A utility allowing the user to copy ssh keys to a given devcontainer

## Usage
````bash
usage: ssh2docker.py [-h] keyName container_user container_name

Copy GitHub SSH-Keys to any given devcontainer

positional arguments:
  keyName         The Key Name (No File Extension / No File Path)
  container_user  The user inside the decontainer
  container_name  The actual container to copy the files to

optional arguments:
  -h, --help      show this help message and exit
````
