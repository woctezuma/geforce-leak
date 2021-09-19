import requests

from src.query_utils import get_query


def get_geforce_url(use_original_endpoint=True):
    if use_original_endpoint:
        geforce_url = get_geforce_original_url()
    else:
        geforce_url = get_geforce_backup_url()
    return geforce_url


def get_geforce_original_url():
    return "https://games.geforce.com/graphql"


def get_geforce_backup_url():
    # Caveat: data available via this url has been downloaded by the leaker at an **earlier** and **unspecified** date!
    # Reference: https://twitter.com/JulyIghor/status/1438152383461269512
    return "http://gfn.uax.co/graphql"


def fetch_page(cursor="", is_slim_query=True, use_original_endpoint=True, app_ids=None):
    geforce_url = get_geforce_url(use_original_endpoint=use_original_endpoint)

    print(f"Cursor: {cursor}")

    query = get_query(
        cursor,
        is_slim_query=is_slim_query,
        use_original_endpoint=use_original_endpoint,
        app_ids=app_ids,
    )

    r = requests.post(
        url=geforce_url,
        json={"query": query},
    )
    if r.ok:
        data = r.json()
        item_info = data["data"]["apps"]["items"]
        page_info = data["data"]["apps"]["pageInfo"]
    else:
        item_info = None
        page_info = None

    return item_info, page_info


def fetch_all_pages(is_slim_query=True, use_original_endpoint=True, app_ids=None):
    data = []

    has_next_page = True
    cursor = ""

    while has_next_page:
        item_info, page_info = fetch_page(
            cursor,
            is_slim_query=is_slim_query,
            use_original_endpoint=use_original_endpoint,
            app_ids=app_ids,
        )

        data += item_info

        has_next_page = page_info["hasNextPage"]
        cursor = page_info["endCursor"]

    return data
