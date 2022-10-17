# Wewy Chatbot
This chatbot project is to **support** people with psychosocial disabilities and to prevent suicide. 

## Getting Started
These are the instructions to be able to start the bot api, which has a Dockerfile

### Prerequisites

Step-by-step installation of everything needed to start the chatbot
``` bash
pip install fastapi
pip install uvicorn
pip install pydantic
```

### Installation with docker

If you want to avoid the hassle of installing everything locally, you can use docker, with its Dockerfile building the following image like this: 
``` docker
docker build -t wewy-chatbot .                   
```

## Usage
To run the chatbot with uvicorn locally, you can do so with the following command 
``` shell
 uvicorn api.main:api --host localhost --port 8080
```

If you used the Dockerfile to run the chatbot use the following command
``` docker
docker run  --name wewy -p 8080:8080 wewy
```

## Deployment
For development we will use Trunkbased, which means that we will add specific branches for functionality, including repairs and so on, only accepting the master branch with a PR.
 
### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Documentation link:
* etc...
