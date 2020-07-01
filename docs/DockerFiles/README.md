# Docker Notes

## WTF is Docker??

###Docker concepts

Docker is a platform for developers and sysadmins to build, run, and share applications with containers. The use of containers to deploy applications is called *containerization*. Containers are not new, but their use for easily deploying applications is.

Containerization is increasingly popular because containers are:

- **Flexible**: Even the most complex applications can be containerized.
- **Lightweight**: Containers leverage and share the host kernel, making them much more efficient in terms of system resources than virtual machines.
- **Portable**: You can build locally, deploy to the cloud, and run anywhere.
- **Loosely coupled**: Containers are highly self sufficient and encapsulated, allowing you to replace or upgrade one without disrupting others.
- **Scalable**: You can increase and automatically distribute container replicas across a datacenter.
- **Secure**: Containers apply aggressive constraints and isolations to processes without any configuration required on the part of the user.

### Images and containers

Fundamentally, a container is nothing but a running process, with some added encapsulation features applied to it in order to keep it isolated from the host and from other containers. One of the most important aspects of container isolation is that each container interacts with its own private filesystem; this filesystem is provided by a Docker image. An image includes everything needed to run an application - the code or binary, runtimes, dependencies, and any other filesystem objects required.

### Containers and virtual machines

A container runs natively on Linux and shares the kernel of the host machine with other containers. It runs a discrete process, taking no more memory than any other executable, making it lightweight.

By contrast, a virtual machine (VM) runs a full-blown "guest" operating system with virtual access to host resources through a hypervisor. In general, VMs incur a lot of overhead beyond what is being consumed by your application logic.

![container](https://github.com/docker/docker.github.io/blob/master/images/Container%402x.png)

![vm](https://github.com/docker/docker.github.io/blob/master/images/VM%402x.png)


## Installing Docker

To get started with Docker Engine on Ubuntu, make sure you
[meet the prerequisites](#prerequisites), then
[install Docker](#installation-methods).

## Prerequisites

### OS requirements

To install Docker Engine, you need the 64-bit version of one of these Ubuntu
versions:

- Ubuntu Eoan 19.10
- Ubuntu Bionic 18.04 (LTS)
- Ubuntu Xenial 16.04 (LTS)

Docker Engine is supported on `x86_64` (or `amd64`), `armhf`, `arm64`, `s390x`
(IBM Z), and `ppc64le` (IBM Power) architectures.

### Installing

    ```bash
    $ sudo apt-get update

    $ sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common
        
    $ sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```
### Postinstall Tasks

1. Create `docker` group

  - `sudo groupadd docker`

2. Add youre user to the `docker` group

  - `sudo usermod -aG docker $USER`

3. Log out of your account and log back in

  - You can also use `$ newgrp docker` to create the group
  
4. Verify that you can run `docker` without `sudo`

  ```bash
  $ docker run hello-world
  ```
  
NOTE
===============

If you recieve an error about the `~/docker/` directory run the following:

  ```bash
  $ sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
  $ sudo chmod g+rwx "$HOME/.docker" -R
  ```

### Configure Docker to start on boot

  ```bash
  $ sudo systemctl enable docker
  $ sudo chkconfig docker on
  ```

## Using Docker

### Pulling Docker images from Docker public hub

Pull images with 

`sudo docker pull IMAGE`

Example

`sudo docker pull drupal`

Output

  ```bash
    $ sudo docker pull drupal
    Using default tag: latest
    latest: Pulling from library/drupal
    b248fa9f6d2a: Pull complete 
    087a082ea6d9: Pull complete 
    77fad012f4b9: Pull complete 
    6174dbcc06b5: Pull complete 
    a2e8d7af5694: Pull complete 
    a107ca22db66: Pull complete 
    8a40191c5b70: Pull complete 
    1c33a219ee9a: Pull complete 
    75ff540b22ba: Pull complete 
    9c13fb8d9e5f: Pull complete 
    0cdf275406f6: Pull complete 
    2a40538458ab: Pull complete 
    b0397bc7fb5f: Pull complete 
    b3163be6f9ad: Pull complete 
    7974513b50ca: Pull complete 
    44fde2f15721: Pull complete 
    Digest: sha256:455df66cc9bfdd7befd0dfdd3c8922aff5393a0ecdb7314f05731a3b48d10d59
    Status: Downloaded newer image for drupal:latest
  ```

Check images with

`sudo docker images`

### Running containers from pulled images

Use the `docker run` command to start a container from an image pulled from Docker repo

Example

`sudo docker run`


1. The Docker client contacts the Docker daemon
2. The Docker daemon checks local store if the image (alpine in this case) is available locally, and if not, downloads it from Docker Store. (Since we have issued docker pull alpine before, the download step is not necessary)
3. The Docker daemon creates the container and then runs a command in that container.
4. The Docker daemon streams the output of the command to the Docker client

#### Check the Docker container

You can use `docker image ls` or use:
  ```bash
   $ docker ps --all

    CONTAINER ID     IMAGE           COMMAND      CREATED            STATUS
    54f4984ed6a8     hello-world     "/hello"     20 seconds ago     Exited (0) 19 seconds ago
  ```

## Aw crap! Now WTF are Dockerfiles

Dockerfiles describe how to assemble a private filesystem for a container, and can also contain some metadata describing how to run a container based on this image.

Dockerfiles usually look like this:

```bash
  # Use the official image as a parent image.
  FROM node:current-slim

  # Set the working directory.
  WORKDIR /usr/src/app

  # Copy the file from your host to your current location.
  COPY package.json .

  # Run the command inside your image filesystem.
  RUN npm install

  # Inform Docker that the container is listening on the specified port at runtime.
  EXPOSE 8080

  # Run the specified command within the container.
  CMD [ "npm", "start" ]

  # Copy the rest of your app's source code from your host to your image filesystem.
  COPY . .
```
  
### Building images from Dockerfiles

Make sure you are in the correct directory that contains your Dockerfile 

Example:

/path/to/appName/Dockerfile


Build your image with 

`docker build --tag *appName*/*version*`

### Starting containers from images you built

1. Start a container based off your image:

`docker run --publish 8000:8080 --detach --name ** *appName*:*version*`

There are a couple of common flags here:

-    --publish asks Docker to forward traffic incoming on the host's port 8000, to the container's port 8080. Containers have their own private set of ports, so if you want to reach one from the network, you have to forward traffic to it in this way. Otherwise, firewall rules will prevent all network traffic from reaching your container, as a default security posture.
-    --detach asks Docker to run this container in the background.
-    --name specifies a name with which you can refer to your container in subsequent commands, in this case bb.

Also notice, you didn't specify what process you wanted your container to run. You didn't have to, as you've used the CMD directive when building your Dockerfile; thanks to this, Docker knows to automatically run the process npm start inside the container when it starts up.

2. Visit your application in a browser at localhost:8000.



3. Once you're satisfied that your bulletin board container works correctly, you can delete it:

`docker rm --force bb`

The --force option removes the running container. If you stop the container running with docker stop bb you do not need to use --force.

## UUUUGGH PUSH IT! - *Salt n Pepa*

>**"Are you guys silly? I'm just gonna send it!"** - *Larry Enticer*

### Pushing to your Docker repository

1. Now you are ready to share your image on Docker Hub, but there's one thing you must do first: images must be namespaced correctly to share on Docker Hub. Specifically, you must name images like `<Docker ID>/<Repository Name>:<tag>`. You can relabel your `baslineContainer:1.0` image like this (of course, please replace `<Docker ID>` with your Docker ID):

`docker tag baselineContainer:1.0 <Docker ID>/baselineContainer:1.0`

2. Finally, push your image to Docker Hub:

`docker push <Docker ID>/baselineContainer:1.0`

Visit your repository in Docker Hub, and you'll see your new image there. Remember, Docker Hub repositories are public by default.
