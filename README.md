# reorderipy

A Python script to reorder the custom order of Spotify playlist items by date added, from newest to oldest instead of the opposite default. **It will reorder all playlists owned by the signed in user, both private, public and collaborative, unless modified to do otherwise.**

I made this because the AAOS Spotify app in my car at the time of writing is locked to the custom order which means new tracks are added to the end of the playlists. On top of this, the app only allows you to choose from the 100-or-so first (oldest) tracks - in other words not enough to reach the good stuff of my quickly growing 1000+ track playlist...

## Usage

1. Sign up for a [Spotify Developer](https://developer.spotify.com/) account.

2. Create a new app in the Spotify Developer dashboard. Enter a name and description and add a redirect URI. The redirect URI can simply be `https://localhost` and does not have to "do" anything - You will be redirected to this URL and copy the URL to paste it in the console when signing in the first time.

3. Create a `.env` file alongside the script, with the variables `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` and `SPOTIPY_REDIRECT_URI` set to the appropriate values for your newly created Spotify app.

4. Install dependencies with `pip install spotipy python-dotenv` (preferrably in a [Python venv](https://docs.python.org/3/library/venv.html)).

5. Run the script manually, as a cron job or however you like. The first time you run it, a Spotify sign-in URL will be printed. Open this URL in a browser and sign in to Spotify. Copy the URL you are redirected to and paste it back in the console. This will allow the script to extract the required access- and refresh tokens. These tokens will be cached in a file alongside the script. You can read more about the caching in the [spotipy docs](https://spotipy.readthedocs.io/#customized-token-caching).
