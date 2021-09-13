import requests

from src.query_utils import get_query


def get_geforce_url():
    return "https://games.geforce.com/graphql"


def fetch_page(cursor="", is_slim_query=True):
    print(f"Cursor: {cursor}")

    r = requests.post(
        url=get_geforce_url(),
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


def fetch_all_pages(is_slim_query=True):
    data = []

    has_next_page = True
    cursor = ""

    while has_next_page:
        item_info, page_info = fetch_page(cursor, is_slim_query=is_slim_query)

        data += item_info

        has_next_page = page_info["hasNextPage"]
        cursor = page_info["endCursor"]

    return data
