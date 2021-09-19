from src.disk_utils import save_to_disk
from src.fetch_utils import fetch_all_pages, get_geforce_url


def main():
    geforce_url = get_geforce_url()

    data = fetch_all_pages(is_slim_query=False, geforce_url=geforce_url)
    save_to_disk(data, "data_slim.json", verbose=True)

    data = fetch_all_pages(is_slim_query=True, geforce_url=geforce_url)
    save_to_disk(data, "data_full.json", verbose=True)

    return


if __name__ == "__main__":
    main()
