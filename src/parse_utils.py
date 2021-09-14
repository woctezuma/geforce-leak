from src.duplicate_utils import sort_data
from src.filter_utils import get_store_suffixe, get_store_id


def parse_data(
    data,
    target_store_name="Epic Games Store",
    trim_output=True,
    sort_output=True,
    verbose=False,
):
    apps = list()

    for app in data:
        slim_app = dict()

        slim_app["name"] = parse_title(
            app, target_store_name=target_store_name, trim_output=trim_output
        )
        slim_app["dev"] = parse_developer(app)
        slim_app["pub"] = parse_publisher(app)
        slim_app["id"] = parse_app_id(
            app,
            target_store_name=target_store_name,
            trim_output=trim_output,
            verbose=verbose,
        )
        slim_app["date"] = parse_release_date(
            app, trim_output=trim_output, verbose=verbose
        )

        apps.append(slim_app)

    if sort_output:
        apps = sort_data(apps)

    return apps


def parse_title(app, target_store_name="Epic Games Store", trim_output=True):
    title = app["title"]

    if trim_output:
        target_store_suffixe = get_store_suffixe(target_store_name)
        title = title.replace(target_store_suffixe, "")

    title = title.strip()

    return title


def parse_developer(app):
    return app["developerName"]


def parse_publisher(app):
    return app["publisherName"]


def parse_app_id(
    app, target_store_name="Epic Games Store", trim_output=True, verbose=False
):
    target_store_id = get_store_id(target_store_name)

    all_app_ids = []
    for store_element in app["storeIds"]:
        if store_element["store"] == target_store_id:
            current_app_id = store_element["id"]
            all_app_ids.append(current_app_id)
    all_app_ids.sort()

    if verbose and len(all_app_ids) > 1:
        print(f"[several appIDs detected] {app}")

    if len(all_app_ids) > 0:
        # Arbitrarily pick the last appID
        app_id = all_app_ids[-1]
    else:
        app_id = ""

    if trim_output and app_id == "TBD":
        app_id = ""

    return app_id


def parse_release_date(app, trim_output=True, verbose=False):
    all_release_dates = []
    for date_element in app["computedValues"].values():
        if date_element is not None:
            all_release_dates.append(date_element)
    all_release_dates.sort()

    if verbose and len(all_release_dates) > 1:
        print(f"[several release dates detected] {app}")

    if len(all_release_dates) > 0:
        # Pick the latest date
        release_date = all_release_dates[-1]
    else:
        release_date = ""

    if trim_output and release_date == "TBD":
        release_date = ""

    # Ensure that the granularity stops at the day, i.e. "YYYY-MM-DD"
    release_date = release_date[:10]

    return release_date
