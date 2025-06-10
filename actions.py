
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHealthAdvice(Action):
    def name(self):
        return "action_health_advice"

    def run(self, dispatcher, tracker, domain):
        symptom = tracker.get_slot("symptom")
        advice = "Please consult a doctor." if symptom else "Tell me more about your symptoms."
        dispatcher.utter_message(text=advice)
        return []
