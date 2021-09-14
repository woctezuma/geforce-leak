def sort_data(data):
    data.sort(key=lambda x: (x["name"], x["id"], x["date"]))
    return data


def deduplicate_data(data, sort_output=True):
    # Caveat: the order of the list is lost due to the process of de-duplication!
    # Reference: https://stackoverflow.com/a/38521207/
    data = [dict(s) for s in set(frozenset(d.items()) for d in data)]

    if sort_output:
        data = sort_data(data)

    return data
