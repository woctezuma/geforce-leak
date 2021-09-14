def get_full_headers():
    full_headers = ["appID", "releaseDate", "title", "developerName", "publisherName"]
    return full_headers


def get_slim_headers():
    slim_headers = ["id", "date", "name", "dev", "pub"]
    return slim_headers


def standardize_str(text, sep=","):
    return text.replace(sep, "").replace('"', "")


def print_results(data, sep=","):
    full_headers = get_full_headers()
    slim_headers = get_slim_headers()

    print(sep.join(full_headers))
    for app in data:
        print(sep.join(standardize_str(app[s], sep=sep) for s in slim_headers))

    return
