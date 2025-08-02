import wikipedia

title = input("Enter page title: ").strip()

try:
    page = wikipedia.page(title, autosuggest=False)
    print(page.title)
    print(page.summary)
    print(page.url)

except wikipedia.DisambiguationError as e:
    print("We need a more specific title. Try one of the following:")
    print(e.options)

except wikipedia.PageError:
    print(f'Page "{title}" does not match any pages. Try another title!')

except Exception as e:
    print(f"An error occurred: {e}")