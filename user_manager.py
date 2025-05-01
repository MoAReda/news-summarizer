import json

def load_user_preferences(user_id):
    """
    Load user preferences from a JSON file.
    """
    try:
        with open(f"{user_id}_preferences.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"topics": [], "history": []}

def save_user_preferences(user_id, preferences):
    """
    Save user preferences to a JSON file.
    """
    with open(f"{user_id}_preferences.json", "w") as f:
        json.dump(preferences, f)

def add_topic(user_id, topic):
    """
    Add a topic to the user's preferences.
    """
    preferences = load_user_preferences(user_id)
    if topic not in preferences["topics"]:
        preferences["topics"].append(topic)
        save_user_preferences(user_id, preferences)

def add_search_history(user_id, topic, timeframe):
    """
    Add a search entry to the user's history.
    """
    preferences = load_user_preferences(user_id)
    preferences["history"].append({"topic": topic, "timeframe": timeframe})
    save_user_preferences(user_id, preferences)

def get_search_history(user_id):
    """
    Retrieve the user's search history.
    """
    preferences = load_user_preferences(user_id)
    return preferences["history"]