import requests

from src.query_utils import get_query


def get_geforce_url():
    return "https://games.geforce.com/graphql"


def get_geforce_backup_url():
    # Caveat: data available via this url has been downloaded by the leaker at an **earlier** and **unspecified** date!
    # Reference: https://twitter.com/JulyIghor/status/1438152383461269512
    return "http://gfn.uax.co/graphql"


def fetch_page(cursor="", is_slim_query=True, geforce_url=None):
    if geforce_url is None:
        geforce_url = get_geforce_url()

    print(f"Cursor: {cursor}")

    r = requests.post(
        url=geforce_url,
        json={"query": get_query(cursor, is_slim_query=is_slim_query)},
    )
    if r.ok:
        data = r.json()
        item_info = data["data"]["apps"]["items"]
        page_info = data["data"]["apps"]["pageInfo"]
    else:
        item_info = None
        page_info = None

    return item_info, page_info


def fetch_all_pages(is_slim_query=True, geforce_url=None):
    data = []

    has_next_page = True
    cursor = ""

    while has_next_page:
        item_info, page_info = fetch_page(
            cursor, is_slim_query=is_slim_query, geforce_url=geforce_url
        )

        data += item_info

        has_next_page = page_info["hasNextPage"]
        cursor = page_info["endCursor"]

    return data
