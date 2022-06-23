
#  API Endpoint Generator, powered by GPT-3

This project leverages OpenAI's GPT-3 Machine Learning Model NLP capabilitiess to generate API endpoints from user defined server, database and endpoint parameters
=======
This project uses OpenAI's GPT-3 Machine Learning Model natural langauge processing capabilities to generate API endpoints semantically in your choice between Python(Flask), JavaScript(Node and Express), and Go in MySQL, Postgres and MongoDB. 

Backend built with Python & Flask deployed on docker container hosted on AWS Lightsail


## Deployment Instructions

 Duplicate the environment variable example file, and create an [API key](https://beta.openai.com/account/api-keys) and add it to the to the new .env file 
  
   ```bash
   $ cp .env.example .env
   ```


Run these commands to deploy containers for the web server, access on localhost:<your-port>/
 
 
 ```bash
 $ docker build -t <imageName> .
 ```
 
 M1/ARM64 reccomended build command for multi-arch support
 ```bash
 $ docker buildx build --platform=linux/amd64 -t <imageName> .
 ```
 
 ```bash
 $ docker run -p <your-port>:5000 <imageName>
 ```

