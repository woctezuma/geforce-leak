import json


def save_to_disk(data, fname, verbose=False):
    with open(fname, "w", encoding="utf8") as f:
        json.dump(data, f)

    if verbose:
        print(f"#entries = {len(data)}")

    return


def load_from_disk(fname, verbose=False):
    with open(fname, "r", encoding="utf8") as f:
        data = json.load(f)

    if verbose:
        print(f"#entries = {len(data)}")

    return data
