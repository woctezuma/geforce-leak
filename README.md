# GeForce Leak

This repository contains Python code to fetch data from [the GeForce leak][medium-post].

## Disclaimer

- The leak has been plugged, so the code cannot fetch data anymore.
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

Alternatively, you can find the data in the ["Releases" section][github-releases] of this repository.

- Run the following script to filter GeForce data by stores, e.g. "Epic Games Store" or "Steam":

```bash
python filter_geforce_data.py
```

## Results

Here is a list of games which have an id on [the Epic Games Store][epic-store]:
- [the whole list][gist-epic]

Here is a list of games which have an id on [the Steam Store][steam-store]:
- [the whole list][gist-steam-1], except for two entries which contain private information (email address, URL)

NB: if an id is empty in the results linked above, then it appeared in the leak as "TBD" for "To Be Decided".

## References

- A [Medium post by the original leaker][medium-post] revealing the method,
- A [tweet by the original leaker][tweet-leaker], which advertises the blog post above,
- A [tweet by the creator of SteamDB][tweet-steamdb], which helps spread the information.

<!-- Definitions -->

[github-releases]: <https://github.com/woctezuma/geforce-leak/releases>
[github-issues]: <https://github.com/woctezuma/geforce-leak/issues>

[epic-store]: <https://www.epicgames.com/store/>
[steam-store]: <https://store.steampowered.com/>

[gist-epic]: <https://gist.github.com/woctezuma/64949a67eedfc96a063d3510d7b8d0bb>
[gist-steam-1]: <https://gist.github.com/woctezuma/bd75692055c5d341d9989b9ec5396421>

[medium-post]: <https://medium.com/@ighor/i-unlocked-nvidia-geforce-now-and-stumbled-upon-pirates-dc48a3f8ff7>
[tweet-leaker]: <https://twitter.com/JulyIghor/status/1437188494984720387>
[tweet-steamdb]: <https://twitter.com/thexpaw/status/1437362950885490692>
