# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"


# Filter to keep only movies released in the 2000s (2000 up to and including 2009)
# Start by filtering out movies that were released before 2000

# And then do the same to filter out movies released in or after 2010
movies2000s = netflix_df[
    (netflix_df["release_year"] >= 2000) &
    (netflix_df["release_year"] <= 2009)
]
from IPython.display import display, HTML

display(HTML(
    f'<div style="height:400px; overflow:auto;">'
    f'{movies2000s.to_html()}'
    f'</div>'
))


# Hint: you can also do this in one step using the & operator

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!
plt.hist(movies2000s["duration"], bins=30)
plt.title('Distribution of Movie Durations in the 2000s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

# Filter the data again to keep only the Comedies
# Filtering data for the genre
comedies_2000s = movies2000s[movies2000s["genre"]== "Comedies"]

# Use a for loop and a counter to count how many LONG comedies (more than 120 minutes) there were in the 2000s

# Start the counter
long_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is greater than 120
# If it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in comedies_2000s.iterrows():
    if row["duration"] > 90:
        long_movie_count = long_movie_count + 1
    else:
        long_movie_count = long_movie_count

print(long_movie_count)

# Creating data visualization in comparison
short_movie_count = len(comedies_2000s) - long_movie_count
plt.bar(
    ["Under 90 minutes", "90 minutes or longer"],
    [short_movie_count, long_movie_count]
)

plt.title("2000s Comedy Movies by Duration")
plt.ylabel("Number of Movies")
plt.show()

# Bonus: a quicker way of counting values in a column is to use .sum() on a boolean condition
# Can you get the same answer without a for loop?