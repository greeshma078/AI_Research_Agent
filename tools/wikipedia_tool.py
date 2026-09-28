import requests

from langchain_core.tools import tool


@tool
def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia and return a summary.

    Use this tool when the user asks for general factual
    information about a person, place, technology, concept,
    organization, or other topic.
    """

    try:

        url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + query.replace(" ", "_")
        )

        headers = {
            "User-Agent": (
                "AIResearchAgent/1.0 "
                "(Educational project; "
                "contact: greeshma@example.com)"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code == 404:

            return "Wikipedia page not found."

        if response.status_code != 200:

            return (
                "Unable to retrieve information from Wikipedia."
            )

        data = response.json()

        summary = data.get("extract")

        if not summary:

            return "No summary was found on Wikipedia."

        return summary

    except requests.exceptions.RequestException:

        return "Unable to connect to Wikipedia."

    except Exception:

        return (
            "Unable to retrieve information from Wikipedia."
        )


# --------------------------------------------------
# Test the Wikipedia tool
# --------------------------------------------------

if __name__ == "__main__":

    result = wikipedia_search.invoke(
        "Artificial intelligence"
    )

    print("Wikipedia Result:")
    print(result)