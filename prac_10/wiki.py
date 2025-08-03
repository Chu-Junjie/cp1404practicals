import wikipedia

def search_wikipedia():
    """Simple tool to search Wikipedia titles and display page info."""
    print("Wikipedia Search Tool (press Enter to quit)\n")
    for _ in range(10):  # Allow up to 10 searches
        title = input("Enter page title: ").strip()

        if title != "":
            try:
                page = wikipedia.page(title, auto_suggest=False)
                print(page.title)
                print(page.summary)
                print(page.url + "\n")

            except wikipedia.DisambiguationError as e:
                print("We need a more specific title. Try one of the following:")
                print("(BeautifulSoup warning)")
                print(e.options[:5], "...")

            except wikipedia.PageError:
                print(f'Page "{title}" does not match any pages. Try another title!')

            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")
        else:
            print("Thank you.")
            return

if __name__ == "__main__":
    search_wikipedia()