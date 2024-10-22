from flask import Flask, request, render_template, jsonify, redirect, url_for
import stripe

app = Flask(__name__)


# Define the list of states and cities
states_and_cities = {
    'Madhya Pradesh': ['Jabalpur', 'Bhopal', 'Indore']
}

museums_in_jabalpur = [
    {'name': 'Rani Durgavati Museum', 'price_per_ticket': 150}
]


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle chatbot conversation
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response, buttons, show_input_box = generate_response(user_input)
    return jsonify(response=response, buttons=buttons, showInputBox=show_input_box)


def generate_response(user_input):
    global total_price  # Ensure you use a global variable if necessary
    buttons = []
    show_input_box = False

    if user_input.lower() == 'book ticket':
        return "Please select your state:", list(states_and_cities.keys()), False

    elif user_input in states_and_cities:
        return f"Please select your city in {user_input}:", states_and_cities[user_input], False

    elif user_input in ['Jabalpur', 'Bhopal', 'Indore']:
        if user_input == 'Jabalpur':
            museums = [museum['name'] for museum in museums_in_jabalpur]
            return "Available museums in Jabalpur:", museums, False
        else:
            return f"No museums available in {user_input} yet.", [], False

    elif user_input == 'Rani Durgavati Museum':
        return "Ticket price: 150 INR per person. How many tickets would you like?", [], True  # Show input box

    elif user_input.isdigit():
        ticket_count = int(user_input)
        total_price = ticket_count * 150  # Update total price of tickets
        return f"The total price is {total_price} INR. How would you like to pay?", ['Card', 'UPI', 'Netbanking'], False

    elif user_input.lower() in ['card', 'upi', 'netbanking']:
        method = user_input.lower()
        response = pay(total_price, method)
        return response['message'], [], False

    elif user_input.lower():
        return "Rasa Activating"

    else:
        return "Thank you for using our chatbot! Happy visit to the museum!", [], False


@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json
    price = data.get('price')
    method = data.get('method')
    return pay(price, method)


def pay(price, method):
    # Simulate payment processing
    if price and method:
        response = {
            'status': 'success',
            'message': 'Payment processed successfully.',
            'transaction_id': 'txn_dummy_123456',
            'amount': price,
            'payment_method': method
        }
        return response  # Return response as dict
    else:
        response = {
            'status': 'failure',
            'message': 'Invalid payment details.'
        }
        return response  # Return response as dict



if __name__ == '__main__':
    app.run(debug=True)
