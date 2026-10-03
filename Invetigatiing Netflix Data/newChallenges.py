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
# Subset the DataFrame for type "Movie"
netflix_movies = ____

# Count how many movies there are in each genre, and keep only the 5 biggest genres
genre_counts = ____
top_5_genres = ____

# Visualize the top 5 genres with a bar chart
____
plt.title('Top 5 Movie Genres on Netflix')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.show()

# Save the name of the most common genre as a string
most_common_genre = ____

# Filter the movies to keep only that genre and save how many there are
dramas = ____
dramas_count = ____
print(dramas_count)

# ----------------------------------------------------------
# CHALLENGE 2: TV Shows and seasons
# ----------------------------------------------------------
# Subset the DataFrame for type "TV Show"
tv_shows = ____

# For TV shows, the "duration" column holds the number of seasons
# Visualize its distribution and save the most common number of seasons
____
plt.title('Distribution of TV Show Seasons')
plt.xlabel('Number of Seasons')
plt.ylabel('Number of TV Shows')
plt.show()

typical_seasons = ____

# Use a for loop and a counter to count how many TV shows have 3 or more seasons
multi_season_count = ____
for ____, ____ in tv_shows.iterrows():
    if ____:
        ____
    else:
        ____

print(multi_season_count)

# Bonus: get the same answer without a loop using .sum()

# ----------------------------------------------------------
# CHALLENGE 3: Movies from India
# ----------------------------------------------------------
# Keep only the movies where the country is "India"
indian_movies = ____

# Calculate the average duration of these movies
avg_duration_india = ____
print(avg_duration_india)

# Use a for loop to find the title and duration of the longest Indian movie
# Hint: keep track of the longest duration seen so far, and update it when you find a longer one
longest_duration = 0
longest_title = ""
for ____, ____ in indian_movies.iterrows():
    if ____:
        ____
        ____

print(longest_title, longest_duration)

# Bonus: use .idxmax() to find the same movie without a loop

# ----------------------------------------------------------
# CHALLENGE 4: Releases over time
# ----------------------------------------------------------
# Count how many movies were released in each year, sorted by year
releases_per_year = ____

# Visualize the trend with a line plot
____
plt.title('Movies on Netflix by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.show()

# Find the release year with the most movies
peak_year = ____
print(peak_year)

# Use a for loop over releases_per_year.items() to count movies released before 1980
old_movie_count = ____
for ____, ____ in releases_per_year.items():
    if ____:
        ____

print(old_movie_count)

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