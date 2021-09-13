import json


def save_to_disk(data, fname, verbose=False):
    with open(fname, "w", encoding="utf8") as f:
        json.dump(data, f)

    if verbose:
        print(f"#entries = {len(data)}")

    return
