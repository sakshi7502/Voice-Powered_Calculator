from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

# Function to perform the calculation
def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error"

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle voice input
@app.route('/voice-calculate', methods=['POST'])
def voice_calculate():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for the expression...")
        audio = recognizer.listen(source)

        try:
            # Recognize the spoken expression
            expression = recognizer.recognize_google(audio)
            print(f"Expression: {expression}")

            # Calculate the result
            result = calculate(expression)
            print(f"Result: {result}")

            # Return the result
            return result

        except Exception as e:
            return str(e)

# Route to handle typed input calculation
@app.route('/calculate', methods=['POST'])
def calculate_expression():
    data = request.get_json()
    expression = data['expression']
    result = calculate(expression)
    return result

if __name__ == "__main__":
    app.run(debug=True)
