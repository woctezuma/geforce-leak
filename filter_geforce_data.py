from src.disk_utils import load_from_disk
from src.duplicate_utils import deduplicate_data
from src.filter_utils import get_rival_stores, filter_in_by_store, filter_out_by_title
from src.parse_utils import parse_data
from src.print_utils import print_results


def run_workflow(
    data,
    target_store_name="Epic Games Store",
    excluded_store_name="Steam",
    trim_output=True,
    sort_output=True,
    verbose=False,
):
    print(f"\nResults with {target_store_name} and without {excluded_store_name}\n")

    apps = filter_in_by_store(data, target_store_name=target_store_name)
    apps = filter_out_by_title(apps, excluded_store_name=excluded_store_name)
    apps = parse_data(
        apps,
        target_store_name,
        trim_output=trim_output,
        sort_output=sort_output,
        verbose=verbose,
    )

    apps = deduplicate_data(apps, sort_output=sort_output)

    print_results(apps)

    return


def main():
    data = load_from_disk("data/data_slim.json", verbose=False)

    rival_stores = get_rival_stores()

    run_workflow(
        data, target_store_name=rival_stores[0], excluded_store_name=rival_stores[1]
    )

    run_workflow(
        data, target_store_name=rival_stores[1], excluded_store_name=rival_stores[0]
    )

    return


if __name__ == "__main__":
    main()
