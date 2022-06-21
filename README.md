
#  API Endpoint Generator, powered by GPT-3
This project uses OpenAI's GPT-3 Machine Learning Model natural langauge processing capabilities to generate API endpoints semantically in your choice between Python(Flask), JavaScript(Node and Express), and Go in MySQL, Postgres and MongoDB. 

Backend built with Python & Flask with [Zappa](https://github.com/zappa/Zappa) to connect with AWS lambda

## Setup

 Clone this repository

 Navigate into the project directory

   ```bash
   $ cd /path/to/repo
   ```

 Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

 Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

 Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Create an [API key](https://beta.openai.com/account/api-keys) and add it to the to the .env file 
 Run 

 ```bash
 $ flask run
 ```

