from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_paged_items(spotify, result):
    """Get the items from all pages of a paged spotipy-result"""
    items = result["items"]
    while result["next"]:
        result = spotify.next(result)
        items.extend(result["items"])
    return items


def reorder_playlist(spotify, playlist):
    """Reorder the items of a given playlist by date added in descending order"""
    playlist_id = playlist["id"]
    snapshot_id = playlist["snapshot_id"]
    items = list(map(
        lambda item: item["added_at"],
        get_paged_items(spotify, spotify.playlist_items(playlist_id)),
    ))
    for idx_1, item_1 in enumerate(items[1:], start=1):
        for idx_2, item_2 in reversed(list(enumerate(items[:idx_1]))):
            if item_1 > item_2 and (idx_2 <= 0 or item_1 <= items[idx_2 - 1]):
                snapshot_id = spotify.playlist_reorder_items(
                    playlist_id,
                    range_start=idx_1,
                    insert_before=idx_2,
                    snapshot_id=snapshot_id,
                )
                items.insert(idx_2, items.pop(idx_1))
                break


if __name__ == "__main__":
    load_dotenv()
    spotify = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=[
                "playlist-read-private",
                "playlist-read-collaborative",
                "playlist-modify-private",
                "playlist-modify-public",
            ],
            open_browser=False,
        )
    )
    playlists = get_paged_items(spotify, spotify.current_user_playlists())
    user_id = spotify.current_user()["id"]
    for playlist in playlists:
        if playlist["owner"]["id"] == user_id:
            reorder_playlist(spotify, playlist)
