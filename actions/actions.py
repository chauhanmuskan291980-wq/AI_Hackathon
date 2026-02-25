from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckEsic(Action):
    def name(self) -> Text:
        return "action_check_esic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        salary = tracker.get_slot("salary_amount")

        if salary is None:
            dispatcher.utter_message(text="I didn't get your salary. Can you tell me again?")
            return []

        if salary <= 21000:
            dispatcher.utter_message(text="You are eligible for ESIC.")
        else:
            dispatcher.utter_message(text="You are not eligible for ESIC.")

        return []