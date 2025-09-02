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
TODO
- - -
### Project execution
To run project via __docker-compose__ use the following command:
```bash
docker-compose \
  --env-file env/.api.env \
  --env-file env/.common.env \
  up --build
```
- - -
### Test execution
TODO
- - -
