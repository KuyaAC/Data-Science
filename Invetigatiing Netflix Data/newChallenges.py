# ==========================================================
# Netflix EDA Challenges 1 to 5
# Fill in every ____ . Solutions are in netflix_eda_solutions_all.py
# ==========================================================
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")

# ----------------------------------------------------------
# CHALLENGE 1: Genre popularity
# ----------------------------------------------------------
#1.Genre popularity uses value_counts() and a bar chart to find the top 5 movie genres, then counts the movies in the most common one.
# My Solution:
no_per_genre = netflix_df["genre"].value_counts()
no_per_genre.head(5).plot(kind="bar")
plt.title("Top 5 most popular netflix genre")
plt.xlabel("Genre")
plt.ylabel("Count of Movies")
plt.show()


# ----------------------------------------------------------
# CHALLENGE 2: TV Shows and seasons
# ----------------------------------------------------------
# 2.TV shows and seasons plots the seasons histogram and uses a for loop to count shows with 3 or more seasons.
# No 2 solution:
type_of_show = netflix_df["type"].value_counts()
type_of_show
type_of_show.plot(kind="bar")
plt.title("Movies vs TV Shows by Volume")
plt.xlabel("Type of Series")
plt.ylabel("Number of movie")
plt.show()

tv_shows = netflix_df[netflix_df["type"]== "TV Show"]
tv_shows

plt.hist(tv_shows["duration"])
plt.title("Distribution of TV Show Seasons")
plt.xlabel("No of Season")
plt.xticks(range(1, 16))
plt.ylabel("No of Series")

no_tv_shows = tv_shows["duration"].value_counts()
no_tv_shows

more_season = 0

for label, row in tv_shows.iterrows():
    if row["duration"] > 3:
        more_season = more_season + 1
    else:
        more_season = more_season
print(more_season)

less_season = len(tv_shows) - more_season
plt.bar(
    ["Series Under 3 Season", "Series more than 3 season"],
    [less_season, more_season]
)
plt.title("Comparison of number of TV show under/over 3 season")
plt.ylabel("Number of season")
plt.show()


# ----------------------------------------------------------
# CHALLENGE 3: Movies from India
# ----------------------------------------------------------
# Keep only the movies where the country is "India"
indian_movies = netflix_df[netflix_df["country"] == "India"]

# Calculate the average duration of these movies
avg_duration_india = indian_movies["duration"].mean()
print(avg_duration_india)

# Use a for loop to find the title and duration of the longest Indian movie
# Hint: keep track of the longest duration seen so far, and update it when you find a longer one
longest_duration = 0
longest_title = ""
for labels, rows in indian_movies.iterrows():
    if rows["duration"] > longest_duration:
        longest_duration = rows["duration"]
        longest_title = rows["title"]

print(longest_title, longest_duration)

# Bonus: use .idxmax() to find the same movie without a loop

# ----------------------------------------------------------
# CHALLENGE 4: Releases over time
# ----------------------------------------------------------
# Count how many movies were released in each year, sorted by year
releases_per_year = netflix_df["release_year"].value_counts().sort_index()
desc = releases_per_year.sort_values(ascending=False)
desc

# Visualize the trend with a line plot
plt.plot(releases_per_year.index, releases_per_year.values)
plt.title('Movies on Netflix by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.show()


# Find the release year with the most movies
peak_year = 2017
print(peak_year)

# Use a for loop over releases_per_year.items() to count movies released before 1980
old_movie_count = 0

for labels, row in releases_per_year.items():
    if labels < 1980:
        old_movie_count = old_movie_count + row

print("Number of old movies: ", old_movie_count)

# Bonus: get the same answer with a boolean condition and .sum()

# ----------------------------------------------------------
# CHALLENGE 5: When was content added?
# ----------------------------------------------------------
# The "date_added" column is text. Convert it to datetime (hint: pd.to_datetime, try format="mixed")
netflix_df["date_added"] = ____

# Create a new column "year_added" that holds only the year
netflix_df["year_added"] = ____

# Count how many titles were added each year, sorted by year, and plot it as a bar chart
added_per_year = ____
____
plt.title('Titles Added to Netflix per Year')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.show()

# Which year had the most titles added?
busiest_year = ____
print(busiest_year)

# Create a "gap" column: years between release and being added to Netflix
# Then print the average gap
netflix_df["gap"] = ____
print(____)































# -------------------------------------------SOLUTIONS-------------------------------------------
# ==========================================================
# SOLUTIONS - Netflix EDA Challenges 1 to 5
# (Try the challenges first before looking at this file!)
# ==========================================================
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")

# ----------------------------------------------------------
# CHALLENGE 1: Genre popularity
# ----------------------------------------------------------
netflix_movies = netflix_df[netflix_df["type"] == "Movie"]

genre_counts = netflix_movies["genre"].value_counts()
top_5_genres = genre_counts.head(5)

plt.bar(top_5_genres.index, top_5_genres.values)
plt.title('Top 5 Movie Genres on Netflix')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.show()

most_common_genre = "Dramas"

dramas = netflix_movies[netflix_movies["genre"] == "Dramas"]
dramas_count = len(dramas)
print(dramas_count)  # 1343

# ----------------------------------------------------------
# CHALLENGE 2: TV Shows and seasons
# ----------------------------------------------------------
tv_shows = netflix_df[netflix_df["type"] == "TV Show"]

# For TV shows, the "duration" column holds the number of seasons
plt.hist(tv_shows["duration"])
plt.title('Distribution of TV Show Seasons')
plt.xlabel('Number of Seasons')
plt.ylabel('Number of TV Shows')
plt.show()

# Most TV shows have only 1 season
typical_seasons = 1

multi_season_count = 0
for label, row in tv_shows.iterrows():
    if row["duration"] >= 3:
        multi_season_count = multi_season_count + 1
    else:
        multi_season_count = multi_season_count

print(multi_season_count)  # 23

# Quicker way
# (tv_shows["duration"] >= 3).sum()

# ----------------------------------------------------------
# CHALLENGE 3: Movies from India
# ----------------------------------------------------------
indian_movies = netflix_movies[netflix_movies["country"] == "India"]

avg_duration_india = indian_movies["duration"].mean()
print(avg_duration_india)  # about 128.1

# Find the longest Indian movie with a for loop
longest_duration = 0
longest_title = ""
for label, row in indian_movies.iterrows():
    if row["duration"] > longest_duration:
        longest_duration = row["duration"]
        longest_title = row["title"]

print(longest_title, longest_duration)  # Sangam 228

# Quicker way
# indian_movies.loc[indian_movies["duration"].idxmax(), "title"]

# ----------------------------------------------------------
# CHALLENGE 4: Releases over time
# ----------------------------------------------------------
releases_per_year = netflix_movies["release_year"].value_counts().sort_index()

plt.plot(releases_per_year.index, releases_per_year.values)
plt.title('Movies on Netflix by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.show()

peak_year = releases_per_year.idxmax()
print(peak_year)  # 2017

# Count movies released before 1980
old_movie_count = 0
for year, count in releases_per_year.items():
    if year < 1980:
        old_movie_count = old_movie_count + count

print(old_movie_count)  # 96

# Quicker way
# (netflix_movies["release_year"] < 1980).sum()

# ----------------------------------------------------------
# CHALLENGE 5: When was content added?
# ----------------------------------------------------------
netflix_df["date_added"] = pd.to_datetime(netflix_df["date_added"], format="mixed")
netflix_df["year_added"] = netflix_df["date_added"].dt.year

added_per_year = netflix_df["year_added"].value_counts().sort_index()

plt.bar(added_per_year.index, added_per_year.values)
plt.title('Titles Added to Netflix per Year')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles')
plt.show()

busiest_year = added_per_year.idxmax()
print(busiest_year)  # 2019

# Average gap (in years) between release and being added to Netflix
netflix_df["gap"] = netflix_df["year_added"] - netflix_df["release_year"]
print(netflix_df["gap"].mean())  # about 5.8