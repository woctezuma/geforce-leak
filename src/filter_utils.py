def get_rival_stores():
    rival_stores = ["Epic Games Store", "Steam"]
    return rival_stores


def get_store_id(store_name):
    first_word = store_name.split(" ")[0]
    first_word_in_upper_case = first_word.upper()
    return first_word_in_upper_case


def filter_in_by_store(data, target_store_name="Epic Games Store"):
    target_store_id = get_store_id(target_store_name)

    apps = list()

    for app in data:
        store_names = [s["store"] for s in app["storeIds"]]

        if target_store_id in store_names:
            apps.append(app)

    return apps


def get_store_suffixe(store_name):
    store_suffixe = f"- {store_name}"
    return store_suffixe


def filter_out_by_title(data, excluded_store_name="Steam"):
    excluded_store_suffixe = get_store_suffixe(excluded_store_name)

    apps = list()

    for app in data:
        game_name = app["title"]

        if excluded_store_suffixe not in game_name:
            apps.append(app)

    return apps


def sort_data(data):
    data.sort(key=lambda x: (x["name"], x["id"], x["date"]))
    return data
