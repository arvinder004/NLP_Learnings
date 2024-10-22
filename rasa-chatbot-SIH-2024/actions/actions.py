# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionBookTicket(Action):
    def name(self):
        return "action_book_ticket"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Great! Let me book your museum ticket. Can you provide the date?")
        return []


class ActionCheckHours(Action):
    def name(self):
        return "action_check_hours"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="The museum is open from 9 AM to 5 PM every day except Mondays.")
        return []


class ActionGetDirections(Action):
    def name(self):
        return "action_get_directions"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Here’s the Google Maps link to the museum: [Museum Directions](https://maps.google.com)")
        return []
