Introduction
            The Voice-Powered Calculator is a web application that allows users to perform arithmetic calculations either by typing expressions or by using voice commands. Built using Python (Flask framework) for the backend and HTML, CSS, and JavaScript for the frontend, this project integrates voice recognition technology, making it easier for users to calculate values by simply speaking their expressions.
By leveraging the power of speech recognition, the application listens to the user's voice input, interprets the spoken mathematical expression, and provides the result instantaneously. This project is not only a utility for quick calculations but also demonstrates the integration of voice-enabled features in web applications.

Technologies Used
   Languages:
            Python (Backend)
            HTML (Structure and content of web pages)
            CSS (Styling for an attractive UI)
            JavaScript (Client-side logic for interactivity and handling requests)
  Framework:
           Flask: Lightweight web framework for Python used to build the backend of the project.
 JavaScript Libraries:
           Fetch API: To handle asynchronous HTTP requests for calculations and voice input processing.

Python Libraries/Packages:

        SpeechRecognition: For capturing and processing the user's voice input.
        gunicorn: WSGI HTTP Server for running the Flask application in production.
        eval(): Built-in Python function to evaluate the mathematical expression provided by the user.

How the Project Works

        Users can either type a mathematical expression or use the voice command feature.
        The voice feature captures the user's speech, converts it into text, and then processes it as a mathematical expression.
        The backend evaluates the expression and returns the result, which is displayed on the screen.
        For convenience, both manual and voice inputs are supported, providing a flexible user experience.

Libraries/Packages Used
 
 Python:
    Flask: Provides the web framework for routing and handling requests.
    SpeechRecognition: Captures and processes voice inputs.
    gunicorn: Used for deploying the Flask app in production environments.

JavaScript:
    Fetch API: Used to send requests from the front-end to the Flask backend for processing the calculation (either voice or manual).

How to Run the Project
   Clone the repository.
   Install the required Python packages listed in requirements.txt using pip install -r requirements.txt.
   Run the application using python app.py.
   Access the application through the browser, where you can calculate expressions manually or by using voice commands.
