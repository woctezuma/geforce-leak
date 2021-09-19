from src.disk_utils import save_to_disk
from src.fetch_utils import fetch_all_pages


def main():
    use_gfn_endpoint = True

    data = fetch_all_pages(is_slim_query=True, use_original_endpoint=use_gfn_endpoint)
    save_to_disk(data, "data_slim.json", verbose=True)

    data = fetch_all_pages(is_slim_query=False, use_original_endpoint=use_gfn_endpoint)
    save_to_disk(data, "data_full.json", verbose=True)

    return


if __name__ == "__main__":
    main()
