from news_retriever import fetch_news
from embedding_engine import store_embeddings
from summarizer import summarize_article
from user_manager import load_user_preferences, save_user_preferences, add_topic, add_search_history, get_search_history

def main():
    user_id = input("Enter your user ID: ")
    preferences = load_user_preferences(user_id)

    while True:
        print("\n1. Search for news on a topic")
        print("2. Save a topic of interest")
        print("3. View customized summaries")
        print("4. View search history")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            topic = input("Enter a topic to search: ")
            timeframe = input("Enter timeframe (e.g., '24 hours', '1 week'): ")
            articles = fetch_news(topic, timeframe)
            if articles:
                store_embeddings(articles)
                add_search_history(user_id, topic, timeframe)
                print(f"Found {len(articles)} articles on '{topic}'.")
            else:
                print(f"No articles found on '{topic}' in the last {timeframe}. Try a different topic or timeframe.")

        elif choice == "2":
            topic = input("Enter a topic to save: ")
            add_topic(user_id, topic)
            print(f"Topic '{topic}' saved.")

        elif choice == "3":
            history = get_search_history(user_id)
            if not history:
                print("No search history found.")
                continue
            for i, entry in enumerate(history):
                print(f"{i + 1}. Topic: {entry['topic']}, Timeframe: {entry['timeframe']}")
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
                            try:
                                summary = summarize_article(content, summary_type)
                                print(f"Title: {title}")
                                print(f"Summary: {summary}")
                                print("-" * 50)
                            except Exception as e:
                                print(f"Error generating summary: {e}")
                    else:
                        print("No articles found.")
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
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()