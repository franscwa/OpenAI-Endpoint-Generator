
#  API Endpoint Generator, powered by GPT-3


This project leverages the OpenAI GPT-3 Machine Learning Model's NLP capabilities to generate API endpoints from user defined server, database and endpoint parameters

Backend built with Python & Flask deployed on a docker container hosted on AWS Lightsail


## Deployment Instructions

 Duplicate the environment variable example file, and create an API Key [free from OpenAI](https://beta.openai.com/account/api-keys) and add it to the to the new .env file 
  
   ```bash
   $ cp .env.example .env
   ```


Run these commands to deploy containers for the web server, runs on https://[host-ip]:[your-port]/
 
 
 ```bash
 $ docker build -t [imageName] .
 
 OR, For M1/ARM64 devices use this build command for multi-arch support 
 
 $ docker buildx build --platform=linux/amd64 -t [imageName] .
 ```
 
 ```bash
 $ docker run -p [your-port]:5000 [imageName]
 ```

