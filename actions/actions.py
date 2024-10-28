from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class CheckAvailability(Action):
    def name(self) -> Text:
        return "check_availability"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        date = tracker.get_slot("date")
        people = tracker.get_slot("people")
        if date and people:
            dispatcher.utter_message(text=f"Table for {people} on {date} is available. Confirm?")
        else:
            dispatcher.utter_message(text="I need more information to check availability.")
        return []