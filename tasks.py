import os
import json

def run_task(task):
    if task.lower() == "format markdown":
        os.system("npx prettier --write data/format.md")
        return "Markdown formatted successfully."

    elif task.lower() == "sort contacts":
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

    elif task.lower() == "list logs":
        logs_folder = "data/logs"
        if not os.path.exists(logs_folder):
            return "Error: logs folder not found!"

        logs = os.listdir(logs_folder)
        return logs

    return "Invalid task."
