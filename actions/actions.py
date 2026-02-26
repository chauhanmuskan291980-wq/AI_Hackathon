from rasa_sdk import Action

class ActionCheckESICEligibility(Action):

    def name(self):
        return "action_check_esic_eligibility"

    def run(self, dispatcher, tracker, domain):

        salary = tracker.get_slot("salary")
        employer_registered = tracker.get_slot("employer_registered")

        # 🔥 CONVERT SALARY TO FLOAT
        if salary:
            salary = float(salary)

        if salary <= 21000 and employer_registered:
            dispatcher.utter_message(text="🎉 You are eligible for ESIC benefits.")
        else:
            dispatcher.utter_message(text="❌ You are not eligible for ESIC benefits.")

        return []