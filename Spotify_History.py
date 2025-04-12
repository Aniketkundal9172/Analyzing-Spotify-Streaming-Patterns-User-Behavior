import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("spotify_history.csv")

# Basic cleanup
df['ts'] = pd.to_datetime(df['ts'], errors='coerce')

# Top Tracks
top_tracks = df['track_name'].value_counts().head(10)
sns.barplot(y=top_tracks.index, x=top_tracks.values, palette="Blues_d")
plt.title("Top 10 Most Played Tracks")
plt.xlabel("Play Count")
plt.ylabel("Track")
plt.show()

# Top Artists
top_artists = df['artist_name'].value_counts().head(10)
sns.barplot(y=top_artists.index, x=top_artists.values, palette="Greens_d")
plt.title("Top 10 Artists")
plt.xlabel("Play Count")
plt.ylabel("Artist")
plt.show()

# Top Albums
top_albums = df['album_name'].value_counts().head(10)
sns.barplot(y=top_albums.index, x=top_albums.values, palette="Oranges_d")
plt.title("Top 10 Albums")
plt.xlabel("Play Count")
plt.ylabel("Album")
plt.show()

#Objective2

# Extract hour and weekday
df['hour'] = df['ts'].dt.hour
df['weekday'] = df['ts'].dt.day_name()

# Hourly Play Count
hourly = df['hour'].value_counts().sort_index()
sns.barplot(x=hourly.index, y=hourly.values, palette="coolwarm")
plt.title("Listening Patterns by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Plays")
plt.show()

# Weekday Play Count
weekday = df['weekday'].value_counts().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
sns.barplot(x=weekday.index, y=weekday.values, palette="Set2")
plt.title("Listening Patterns by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Plays")
plt.xticks(rotation=45)
plt.show()

#objective3

# Assume skip if song played less than 30 seconds
df['inferred_skipped'] = df['ms_played'] < 30000

# Skip rate overall
skip_rate = df['inferred_skipped'].value_counts(normalize=True)
skip_rate.plot(kind='bar', color=['green', 'red'])
plt.title("Skip vs Non-Skip Ratio")
plt.xticks([0, 1], ['Not Skipped', 'Skipped'], rotation=0)
plt.ylabel("Proportion")
plt.show()

# Skip vs duration
sns.histplot(data=df, x='ms_played', hue='inferred_skipped', bins=50, kde=True)
plt.title("Distribution of Play Duration with Skip Behavior")
plt.xlabel("Milliseconds Played")
plt.ylabel("Frequency")
plt.show()

#objective4

# Count shuffle usage
shuffle_counts = df['shuffle'].value_counts()
shuffle_counts.plot(kind='bar', color=['skyblue', 'orange'])
plt.title("Shuffle Mode Usage")
plt.xticks([0, 1], ['Off', 'On'], rotation=0)
plt.ylabel("Play Count")
plt.show()

# Skip rate in shuffle vs non-shuffle
shuffle_skip_rate = df.groupby('shuffle')['inferred_skipped'].mean()
shuffle_skip_rate.plot(kind='bar', color=['blue', 'red'])
plt.title("Skip Rate in Shuffle vs Non-Shuffle Mode")
plt.xticks([0, 1], ['Shuffle Off', 'Shuffle On'], rotation=0)
plt.ylabel("Skip Rate")
plt.show()

#Objective5

# Reason for starting session
start_reasons = df['reason_start'].value_counts().head(10)

sns.barplot(y=start_reasons.index, x=start_reasons.values, palette="Purples_d")
plt.title("Top 10 Music Discovery Methods")
plt.xlabel("Count")
plt.ylabel("Reason Start")
plt.show()
