"""
CP1404/CP5632 Practical
Wikipedia API & Python Library
"""

import wikipedia

while True:
    page_title = input("Page title or search phrase: ")
    if page_title != "":
        try:
            page = wikipedia.page(page_title, auto_suggest=False)

            print("Page Title:", page.title)
            print("Summary:", page.summary)
        except wikipedia.exceptions.DisambiguationError as error:
            print('Disambiguation Error:', error.options)
        except wikipedia.exceptions.PageError as page_not_found:
            print("Page Error:", page_not_found)
    else:
        break
