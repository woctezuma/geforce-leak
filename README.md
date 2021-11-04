# GeForce Leak

This repository contains Python code to fetch data from [the GeForce leak][medium-post].

![Search results for Hollow][wiki-cover]

## Disclaimer

- The leak has been plugged, so the code cannot fetch data directly from Nvidia anymore.
- GeForce data can still be **partially** accessed via [a user-interface hosted][tweet-leaker-hosting-backup] by the leaker.
- As of September 23, partial data has been further constrained to ~ 1100 games, which removes much interest.
- If you want me to remove data from this project, please [create a Github issue][github-issues] to reach me.

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

- Run the following script to download GeForce data:

```bash
python download_geforce_data.py
```

Alternatively, you can find the data as `v0.1` in the ["Releases" section][github-releases] of this repository.

- Run the following script to filter GeForce data by stores, e.g. "Epic Games Store" or "Steam":

```bash
python filter_geforce_data.py
```

- Run the following script to query **partial** GeForce data via [an interface hosted][tweet-leaker-hosting-backup] by the leaker for known
  appIDs:

```bash
python query_geforce_backup.py
```

Alternatively, you can find the data as `v0.2` in the ["Releases" section][github-releases] of this repository.

## Results

Disclaimer: the results are purged of any entry about Ubisoft, to avoid [any possible DMCA issue][pcgamer-article-dmca].

Here is a list of games which have an id on [the Epic Games Store][epic-store]:
- [the whole list][gist-epic]

Here is a list of games which have an id on [the Steam Store][steam-store]:
- [the whole list][gist-steam-1], except for two entries which contain private information (email address, URL)

NB: if an id is empty in the results linked above, then it appeared in the leak as "TBD" for "To Be Decided".

Here is a list of games which do *not* have any id on the aforementioned stores:
- [the whole list][gist-no-id]

Here is a summary with a focus on documented releases dates:
- [a short list][gist-release-date] of future games.

## References

- A [Medium post by the original leaker][medium-post] revealing the method,
- A [tweet by the original leaker][tweet-leaker], which advertises the blog post above,
- A [tweet by the creator of SteamDB][tweet-steamdb], which helps spread the information.
- A [PC Gamer article][pcgamer-article-dmca], which mentions the takedown request issued by Ubisoft.
- A [status webpage for GeForce Now][status-geforce-now], which lists ids of **regional** "Virtual Private Cloud" (`vpcId`). 

<!-- Definitions -->

[wiki-cover]: <https://raw.githubusercontent.com/wiki/woctezuma/geforce-leak/img/cover.png>

[github-releases]: <https://github.com/woctezuma/geforce-leak/releases>
[github-issues]: <https://github.com/woctezuma/geforce-leak/issues>

[epic-store]: <https://www.epicgames.com/store/>
[steam-store]: <https://store.steampowered.com/>

[gist-epic]: <https://gist.github.com/woctezuma/9777501ed716008aa72542042a04f0e5>
[gist-steam-1]: <https://gist.github.com/woctezuma/c54c1af9287548ad4992a9fae34811c3>
[gist-no-id]: <https://gist.github.com/woctezuma/47376ccd6060ad6e850f24478e25c6fa>
[gist-release-date]: <https://gist.github.com/woctezuma/b2746c95b90c6076e1803b816f364a9a>

[medium-post]: <https://medium.com/@ighor/i-unlocked-nvidia-geforce-now-and-stumbled-upon-pirates-dc48a3f8ff7>
[tweet-leaker]: <https://twitter.com/JulyIghor/status/1437188494984720387>
[tweet-steamdb]: <https://twitter.com/thexpaw/status/1437362950885490692>
[tweet-leaker-hosting-backup]: <https://twitter.com/JulyIghor/status/1438152383461269512>
[pcgamer-article-dmca]: <https://www.pcgamer.com/uk/ubisoft-issues-takedown-request-of-speculative-nvidia-database-leak/>
[status-geforce-now]: <https://status.geforcenow.com/>
