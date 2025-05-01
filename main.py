from news_retriever import fetch_news
from embedding_engine import store_embeddings
from summarizer import summarize_article
from user_manager import load_user_preferences, add_topic, add_search_history, get_search_history

def main():
    # Get user ID to load or create preferences
    user_id = input("Enter your user ID: ").strip()
    if not user_id:
        print("Error: User ID cannot be empty.")
        return

    preferences = load_user_preferences(user_id)

    while True:
        # Display menu options
        print("\n1. Search for news on a topic")
        print("2. Save a topic of interest")
        print("3. View customized summaries")
        print("4. View search history")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            topic = input("Enter a topic to search: ").strip()
            timeframe = input("Enter timeframe (e.g., '24 hours', '1 week'): ").strip()
            if not topic or not timeframe:
                print("Error: Topic and timeframe cannot be empty.")
                continue
            articles = fetch_news(topic, timeframe)
            if articles:
                store_embeddings(articles)
                add_search_history(user_id, topic, timeframe)
                print(f"Found {len(articles)} articles on '{topic}'.")
            else:
                print(f"No articles found on '{topic}' in the last {timeframe}. Try a different topic or timeframe.")

        elif choice == "2":
            topic = input("Enter a topic to save: ").strip()
            if not topic:
                print("Error: Topic cannot be empty.")
                continue
            add_topic(user_id, topic)
            print(f"Topic '{topic}' saved.")

        elif choice == "3":
            history = get_search_history(user_id)
            if not history:
                print("No search history found.")
                continue
            for i, entry in enumerate(history, 1):
                print(f"{i}. Topic: {entry['topic']}, Timeframe: {entry['timeframe']}")
            try:
                selection = int(input("Select a search entry to summarize: ")) - 1
                if 0 <= selection < len(history):
                    topic = history[selection]["topic"]
                    articles = fetch_news(topic, history[selection]["timeframe"])
                    if articles:
                        summary_type = input("Enter summary type (brief/detailed): ").strip().lower()
                        if summary_type not in ["brief", "detailed"]:
                            print("Invalid summary type. Defaulting to 'brief'.")
                            summary_type = "brief"
                        for article in articles:
                            title = article["title"]
                            content = article["content"] or article["description"]
                            if not content:
                                print(f"Skipping '{title}': No content available.")
                                continue
                            try:
                                summary = summarize_article(content, summary_type)
                                print(f"Title: {title}")
                                print(f"Summary: {summary}")
                                print("-" * 50)
                            except Exception as e:
                                print(f"Error summarizing '{title}': {e}")
                    else:
                        print("No articles found for this search.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            history = get_search_history(user_id)
            if not history:
                print("No search history found.")
            else:
                for entry in history:
                    print(f"Topic: {entry['topic']}, Timeframe: {entry['timeframe']}")

        elif choice == "5":
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()