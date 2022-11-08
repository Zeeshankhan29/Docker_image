# Docker_image
We have discussed about Docker image 


You must first create a virtual env
```
conda create -p dock python=3.10 -y

```

activate the Environment
```
conda activate dock

```

You must install all the requirements in your project

```
pip install -r requirements.txt

```

You must create a docker file and write the following code 

```

FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python app.py

```

You must follow the docker commands

```
docker build . -t <tag name>

```

To check the docker images we use

```
docker images

```

#To push your image to docker hub

we must login to docker hub
```
docker login
```

After login we follow

```
docker tag <repository_name>:<version> <username>/<repository_name> 
docker push <username>/<repository_name>
wait for the upload
```

To pull docker image we follow
```

docker pull <user_name>/<repository_name>

```
We must specify this details in app.py file
other docker container won't work 
```
app.run(host='0.0.0.0')

```

To Run docker image
Here 800 is the localhost portnumber and 5000 is the container port number 

```

docker run -p 5000:800 -e PORT=800 <docker image id>/<repository name>

```

To check running docker containers
```
docker ps
```

To stop docker container

```
docker stop <container_id>

```