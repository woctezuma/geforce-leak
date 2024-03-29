import glob

from more_itertools import chunked

from src.disk_utils import save_to_disk, load_from_disk
from src.fetch_utils import fetch_all_pages


def main():
    use_gfn_endpoint = False

    # This file contains all of the known appIDs, as they were downloaded from the original GeForce end-point.
    all_app_ids = load_from_disk("data/app_ids.json", verbose=True)

    # This is the largest number of appIDs which can be listed in a single query for the GraphQL end-points.
    chunk_size = 1200

    # Download data by querying apps in chunks
    for chunk_no, app_ids in enumerate(chunked(all_app_ids, chunk_size), start=1):
        data = fetch_all_pages(
            is_slim_query=True, use_original_endpoint=use_gfn_endpoint, app_ids=app_ids
        )
        save_to_disk(data, f"data/backup_slim_chunk_{chunk_no}.json", verbose=True)

        data = fetch_all_pages(
            is_slim_query=False, use_original_endpoint=use_gfn_endpoint, app_ids=app_ids
        )
        save_to_disk(data, f"data/backup_full_chunk_{chunk_no}.json", verbose=True)

    # Export to disk
    for keyword in ["slim", "full"]:
        data = list()
        for fname in glob.glob(f"data/backup_{keyword}_chunk_*.json"):
            data += load_from_disk(fname)
        save_to_disk(data, f"backup_{keyword}.json", verbose=True)

    return


if __name__ == "__main__":
    main()
