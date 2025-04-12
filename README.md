
# Analyzing Spotify Streaming Patterns & User Behavior

## Overview

This project aims to analyze a user's Spotify streaming history to uncover meaningful insights into music listening behavior. By using Python and its powerful data analysis libraries, the project explores trends, preferences, and patterns across various dimensions such as playtime, skips, shuffle usage, and more.

The core objective is to demonstrate how real-world streaming data can be utilized to better understand user engagement, support personalization strategies, and enhance music recommendation systems.

## Objectives

- Understand overall listening trends and preferences.
- Identify the most played tracks, artists, and albums.
- Analyze user behavior based on time of day and day of the week.
- Examine skip behavior and what leads to content rejection.
- Investigate the role of shuffle mode in user satisfaction.
- Explore how users discover music (autoplay, search, playlist, etc.).

## Dataset

The dataset used is a personal Spotify streaming history file, which contains:
- 149,860 records
- 11 attributes, including:
  - `ts`: Timestamp of when the track was played
  - `track_name`, `artist_name`, `album_name`
  - `ms_played`: Duration (in milliseconds) the track was played
  - `reason_start`, `reason_end`: How and why a track started or ended
  - `shuffle`, `skipped`: Boolean flags for shuffle mode and skipping behavior
  - `platform`: Device/platform used for streaming

## Tools & Technologies

- Python
- Pandas for data wrangling and analysis
- Seaborn and Matplotlib for visualization
- Jupyter Notebook for interactive exploration

## Key Analyses Performed

### 1. Top Content
- Identified top 10 most played tracks, artists, and albums.
- Visualized with bar charts to highlight frequency of plays.

### 2. Time-Based Listening Behavior
- Extracted features like hour of day and day of week from timestamps.
- Analyzed peak listening times (e.g., evenings and weekends).
- Visualized with count plots and line graphs.

### 3. Skip Behavior
- Defined skip threshold (tracks played under 30 seconds).
- Compared skipped vs. fully played tracks.
- Created box plots to show distribution of play duration.

### 4. Shuffle Mode Analysis
- Analyzed user engagement when shuffle mode was on vs. off.
- Measured how randomness affects satisfaction and skip rates.

### 5. Music Discovery Methods
- Explored how users start playing music (click, autoplay, etc.).
- Analyzed most common reasons for track starts.
- Visualized with bar and pie charts.

## Conclusion

The project provides a thorough exploration of user behavior based on Spotify streaming data. It reveals strong patterns in how, when, and what users prefer to listen to. These insights are essential for building smarter recommendation systems, optimizing user interfaces, and tailoring content strategies in music streaming platforms.

## Future Scope

- Integrate machine learning models to predict skips or recommend songs.
- Perform sentiment analysis using lyrics or mood detection.
- Segment users into behavioral clusters.
- Explore geographic trends if location data is available.
- Use real-time streaming tools like Apache Kafka for live analysis.

## References

- [Spotify Developer Documentation](https://developer.spotify.com/documentation/web-api/)
- [Pandas Library](https://pandas.pydata.org)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org)
- Research papers and articles on user behavior in music streaming
