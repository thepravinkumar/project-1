import os
import json

def run_task(task):
    if "sort contacts" in task.lower():
        try:
            file_path = "data/contacts.json"
            if not os.path.exists(file_path):
                return "Error: contacts.json not found!"

            with open(file_path, "r") as f:
                contacts = json.load(f)

            if not isinstance(contacts, list):
                return "Error: Invalid JSON format in contacts.json!"

            sorted_contacts = sorted(contacts, key=lambda x: x.get("name", ""))
            with open("data/contacts_sorted.json", "w") as f:
                json.dump(sorted_contacts, f, indent=2)

            return "Contacts sorted successfully."

        except Exception as e:
            return f"Error: {str(e)}"

    return "Invalid task."
