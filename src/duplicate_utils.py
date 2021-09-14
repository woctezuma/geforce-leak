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


def cluster_data(data):
    clusters = dict()

    for app in data:
        name = app["name"]

        if name not in clusters:
            clusters[name] = []

        clusters[name].append(app)

    return clusters


def identify_issues(clusters):
    # An "issue" means here that there are several apps with the same name.
    issues = [name for name in clusters if len(clusters[name]) > 1]

    # Arbitrary sort, in order to easily focus on the largest cluster in debug mode
    issues.sort(key=lambda x: len(clusters[x]), reverse=True)

    return issues


def merge_data(data, sort_output=True, verbose=False):
    clusters = cluster_data(data)
    issues = identify_issues(clusters)

    merged_data = list()
    merged_data = merge_apps_without_issue(data, issues, merged_data)
    merged_data = merge_apps_with_issues(clusters, issues, merged_data, verbose=verbose)

    if sort_output:
        merged_data = sort_data(merged_data)

    return merged_data


def merge_apps_without_issue(data, issues, merged_data=None):
    if merged_data is None:
        merged_data = list()

    for app in data:
        name = app["name"]

        if name not in issues:
            merged_data.append(app)

    return merged_data


def merge_apps_with_issues(clusters, issues, merged_data=None, verbose=False):
    if merged_data is None:
        merged_data = list()

    for name in issues:
        partial_apps, complete_apps = split_problematic_apps(clusters[name])

        # Caveat: this is important for merging in the right order! We want to process apps with the fewer issues first!
        partial_apps.sort(key=lambda x: sum(s == "" for s in x.values()))

        complete_apps = add_some_partial_apps(partial_apps, complete_apps, verbose)
        merged_data += complete_apps

    return merged_data


def split_problematic_apps(cluster_content):
    partial_apps = []
    complete_apps = []

    for app in cluster_content:
        if any(s == "" for s in app.values()):
            # There is at least one empty field, so we will check whether we can merge this entry with another one.
            partial_apps.append(app)
        else:
            # Every field is filled.
            complete_apps.append(app)

    return partial_apps, complete_apps


def add_some_partial_apps(partial_apps, complete_apps, verbose=False):
    for app in partial_apps:
        to_remove = False

        for ref in complete_apps:
            if all(v in ref[k] for k, v in app.items()):
                # This happens if a partial app does not bring any new information compared to the complete app "ref".
                # An empty field will always verify this property, so only non-empty fields can make a difference here.
                to_remove = True
                break

        if to_remove:
            if verbose:
                print(f"Remove {app}")
        else:
            complete_apps.append(app)
            if verbose:
                print(f"Add {app}")

    return complete_apps
