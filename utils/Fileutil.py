import json


def load_expected_result(file_path):
    try:
        with open(file_path, encoding="utf8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("Expected JSON file not found.")
    except json.JSONDecodeError:
        raise FileNotFoundError("Error decoding expected JSON file.")