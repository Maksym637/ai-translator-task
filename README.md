# ai-translator-task
An AI-powered translator app with BE and FE parts that provides real-time text translation through a clean user interface
- - -
### Task Objective
Your task is to build a prototype of an application that enables automated transaltions between the following languages: `["de", "en", "el", "es", "fr", "it", "pl", "pt", "ro", "nl"]`
- - -
### Task details and deliverables
1. Model Choice: Choose an appropriate machine learning model or API that can perform the translation task. You may use pre-trained models or APIs available in libraries or platforms of your choice.
2. Application Development: Develop a web application that allows users to input text in any of the given languages, select a target language, and see the translated text.
3. Backend and Frontend: Your application should have a backend that manages the translation process and a frontend that allows user interaction. You are free to choose the technologies and frameworks for this.
4. Running Locally: The application should be set up to run on a local machine. Provide clear instructions on how to set up and run the application.
5. Documentation: Prepare a short document detailing your approach to solving the business problem, the design and architecture of your application, and instructions on how to set it up and run it locally. Describe briefly potential risks, biases, and ethical implications of the model of your choice.
- - -
### Project description
The following application is a simplified version of a translator built on the Azure Translator API.

This application uses dependencies provided below:
- __BE:__
    - Python 3.11
    - Poetry 2.1.4
- __FE:__
    - Node.js v22 + npm v10
- Docker 28.3.2
- - -
### Project execution
Before executing the project, fill in the following files in the `env` folder:
- `.api.env`:
```ini
ENV=<env>
API_HOST=<api host>
API_PORT=<api port>
ORIGIN_PORT=<origin port>
AZURE_AI_KEY=<azure ai key>
AZURE_AI_REGION=<azure ai region>
```
- `.client.env`:
```ini
ENV=<env>
CLIENT_HOST=<client host>
CLIENT_PORT=<client port>
```
#### Local execution:
__BE execution__
1. Go to the `ai_translator_api` dir
2. Install all dependencies using the command below:
```bash
poetry install
```
3. Activate poetry using the command below:
```bash
poetry env list --full-path
```
```bash
source [poetry env path]/bin/activate
```
4. Launch the BE part using the command below:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

__FE execution__
1. Go to the `ai_translator_client` dir
2. Install all dependencies using the command below:
```bash
npm install
```
3. Launch the FE part using the command below:
```bash
npm run dev
```

#### Docker execution:
1. Install Docker into your system
2. Launch project via _docker-compose_ using the command below:
```bash
docker-compose \
  --env-file env/.api.env \
  --env-file env/.client.env \
  up --build
```
- - -
### Test execution
To execute tests, follow these steps:
1. Install all dependencies and activate poetry as described earlier in the local execution section
2. Execute tests using the command below:
```bash
PYTHONPATH=. pytest
```
- - -
### Demonstration
[Click here to see how application works](https://youtu.be/E-AGZXG_pc4?si=gd53tRXZvNu2HlL7)
- - -
