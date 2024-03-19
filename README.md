# Revolutionizing Real Estate: Introducing Dubai Land Law Chatbot

In today's fast-paced world, technology continues to reshape industries, making tasks more efficient and accessible than ever before. The real estate sector, known for its complexity and vast information landscape, is no exception to this digital transformation. With the aim of simplifying and enhancing user experiences, we are proud to introduce our cutting-edge chatbot developed. This chatbot will answer each question based on the context of Dubai Land Department's rules and regulation.

# What is the Dubai LandLawAIbot?
Our chatbot is an intelligent virtual assistant powered by state-of-the-art AI technology, including Promptflow and OpenAI models. It serves as a comprehensive resource for individuals and businesses seeking information related to land, properties, and their respective laws in Dubai.

# Chat with PDF

This is a simple flow that allow you to ask questions about the content of a PDF file and get answers.
You can run the flow with a path to a local PDF file and question as argument.
Once it's launched it will download the PDF and build an index of the content. 
Then when you ask a question, it will look up the index to retrieve relevant content and post the question with the relevant content to OpenAI chat model (gpt-3.5-turbo or gpt4) to get an answer.

Tools used in this flow：
- custom `python` Tool

## Prerequisites

Install promptflow sdk and other dependencies:
```bash
pip install -r requirements.txt
```
## How to run?
You should open the flow.dag.yaml file in Visual Studio Code.
Click on run button on the yaml file. This will invoke below command.

```bash

python -m promptflow._cli._pf.entry flow test --flow /LLM-main/core --interactive --user-agent "prompt-flow-extension/1.14.0 (darwin; x64) VSCode/1.86.0"
```

Then you can ask question as an user in the prompt.

## Comparing Actual answer with Bot response.
![image](https://github.com/Tariqueakhtar/LandLawAIBot/assets/44436572/08a9a833-56af-49d6-9eaf-c92f2211101f)

![image](https://github.com/Tariqueakhtar/LandLawAIBot/assets/44436572/2c178a5e-07b0-493a-bfd5-abed4d0b1fc2)

![image](https://github.com/Tariqueakhtar/LandLawAIBot/assets/44436572/4c3e4ab0-bb53-4b49-95db-947b42d5ed5d)

## How to Dockerize?
Exported Dockerfile & its dependencies are located in the 'dest' folder. The structure is as below:

- flow: the folder contains chat with pdf flow files

...
- connections: the folder contains yaml files to create all related connections
...

- runit: the folder contains all the runit scripts
...

- Dockerfile: the dockerfile to build the image

- start.sh: the script used in CMD of Dockerfile to start the service

- settings.json: a json file to store the settings of the docker image

- README.md: the readme file to describe how to use the dockerfile

Please refer to official doc for more details about how to use the exported dockerfile and scripts.

