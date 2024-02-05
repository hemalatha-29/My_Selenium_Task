import pytest
from page_objects import IMDbSearchPage


@pytest.mark.usefixtures("browser")
class TestIMDbSearch:
    def test_search_actor(self, browser):
        imdb_search_page = IMDbSearchPage(browser)
        browser.get("https://www.imdb.com/search/name/")

        # Retry mechanism for the search action
        for _ in range(3):
            try:
                imdb_search_page.search_for_name("Tom Hanks")
                break
            except Exception as e:
                print(f"Failed to search. Retrying... {e}")


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])