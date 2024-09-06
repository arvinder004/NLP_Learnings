import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('stopwords')

# Preprocess the user input by tokenizing and removing stopwords
def preprocess(text):
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    stop_words = set(stopwords.words('english'))  # Get the set of stopwords
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]  # Remove stopwords
    return filtered_tokens

# Identify intent based on simple keyword matching
def recognize_intent(tokens):
    if 'ticket' in tokens or 'book' in tokens:
        return 'book_ticket'
    elif 'time' in tokens or 'hour' in tokens:
        return 'museum_hours'
    else:
        return 'unknown'

# Generate a response based on the identified intent
def generate_response(intent):
    if intent == 'book_ticket':
        return "How many tickets would you like to book, and for which date?"
    elif intent == 'museum_hours':
        return "The museum is open from 10 AM to 6 PM every day."
    else:
        return "I'm sorry, I didn't understand your request. Can you clarify?"

# Extract entities (like number of tickets and date) using regex
def extract_entities(text):
    number_of_tickets = re.findall(r'\d+', text)  # Extract numbers (for ticket count)
    date = re.findall(r'\d{1,2}[/-]\d{1,2}[/-]\d{4}', text)  # Simple date extraction (MM/DD/YYYY or similar)
    return {
        'tickets': number_of_tickets[0] if number_of_tickets else None,
        'date': date[0] if date else None
    }

# Main chatbot function to handle conversation flow
def book_museum_tickets():
    print("Welcome to the Museum Ticket Booking Chatbot!")
    while True:
        user_input = input("You: ")
        
        # Preprocess the user input
        tokens = preprocess(user_input)
        
        # Identify the intent
        intent = recognize_intent(tokens)
        
        # Generate and print the bot's response
        response = generate_response(intent)
        print("Bot:", response)
        
        if intent == 'book_ticket':
            # Ask for more details (number of tickets, date)
            user_input = input("You: ")
            entities = extract_entities(user_input)
            
            if entities['tickets'] and entities['date']:
                print(f"Bot: Great! You have booked {entities['tickets']} tickets for {entities['date']}. Enjoy your visit!")
                break
            else:
                print("Bot: I need to know both the number of tickets and the date to complete the booking.")
        elif intent == 'museum_hours':
            # If the user asks for museum hours, respond accordingly
            continue
        else:
            print("Bot: I can help you with booking tickets or checking museum hours.")

book_museum_tickets()