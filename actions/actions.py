from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConfirmBooking(Action):

    def name(self) -> Text:
        return "action_confirm_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date = tracker.get_slot('date')
        location = tracker.get_slot('location')

        if date and location:
            message = f"Vous souhaitez réserver un hôtel à {location} pour le {date}, c'est bien cela ?"
        else:
            message = "Je n'ai pas compris les détails de votre réservation. Pouvez-vous répéter ?"

        dispatcher.utter_message(text=message)

        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher