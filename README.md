# Spotify Vibe Visualizer 🎵📊

A Python-based data engineering and visualization pipeline that transforms raw Spotify streaming history into a chronological heatmap of weekly listening habits. 

## What It Does
This project takes a massive dataset of personal Spotify streams and processes it to find exactly when peak music listening happens. 

* **Data Cleaning:** Automatically filters out "skipped" tracks by dropping any streams with less than 30 seconds of play time.
* **Feature Engineering:** Extracts the exact hour of the day and day of the week from raw datetime stamps.
* **Data Aggregation:** Compresses thousands of individual streaming rows into a summarized 2D pivot matrix.
* **Visualization:** Renders a polished heatmap using Seaborn's `coolwarm` palette to visually separate high-activity hours (red) from low-activity hours (blue).

## Tech Stack
* Python
* Pandas
* Seaborn & Matplotlib