from src.disk_utils import save_to_disk
from src.fetch_utils import fetch_all_pages


def main():
    data = fetch_all_pages(is_slim_query=False)
    save_to_disk(data, "data_slim.json", verbose=True)

    data = fetch_all_pages(is_slim_query=True)
    save_to_disk(data, "data_full.json", verbose=True)

    return


if __name__ == "__main__":
    main()
