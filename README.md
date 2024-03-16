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
python -m promptflow._cli._pf.entry flow test --flow /LLM-main/core --interactive --user-agent "prompt-flow-extension/1.14.0 (darwin; x64) VSCode/1.86.0"

Then you can ask question as an user in the prompt.

