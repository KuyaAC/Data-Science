
# ============================================================
# PYTHON DATA SCIENCE NOTES: APPLICATIONS OF STATISTICS
# ============================================================

# Statistics helps data scientists understand data, identify
# patterns, measure relationships, and make informed decisions.


# 1. DESCRIPTIVE STATISTICS
# ------------------------------------------------------------
# Purpose: Summarize and describe the characteristics of data.
#
# Mean: Calculate the average value.
# Median: Identify the middle value.
# Mode: Identify the most frequent value.
# Standard Deviation: Measure how spread out the data is.
# Variance: Measure the variability of data.
# Min/Max: Identify the lowest and highest values.
#
# Applications:
# - Calculate average monthly sales.
# - Analyze employee salaries.
# - Understand product price distributions.
#
# Python:
df.describe()
df['sales'].mean()
df['sales'].median()
df['sales'].mode()
df['sales'].std()
df['sales'].var()


# 2. INFERENTIAL STATISTICS
# ------------------------------------------------------------
# Purpose: Use sample data to make conclusions about a larger
# population.
#
# Population: The entire group being studied.
# Sample: A smaller group selected from the population.
# Sampling: Selecting observations for analysis.
# Confidence Interval: Estimate a population value within a range.
#
# Applications:
# - Estimate customer satisfaction using survey samples.
# - Analyze customer behavior.
# - Evaluate business performance using sample data.


# 3. CORRELATION ANALYSIS
# ------------------------------------------------------------
# Purpose: Identify the strength and direction of relationships
# between two variables.
#
# +1: Perfect positive correlation.
#  0: No linear correlation.
# -1: Perfect negative correlation.
#
# Applications:
# - Determine the relationship between advertising and sales.
# - Analyze employee experience and salary.
# - Investigate product prices and customer demand.
#
# Python:
df['advertising'].corr(df['sales'])
df.corr(numeric_only=True)

# Visualization:
df.plot(kind='scatter', x='advertising', y='sales')


# 4. PROBABILITY DISTRIBUTION
# ------------------------------------------------------------
# Purpose: Understand how data is distributed and calculate
# the likelihood of certain events.
#
# Normal Distribution: Data follows a bell-shaped distribution.
# Binomial Distribution: Models success or failure outcomes.
# Poisson Distribution: Models the frequency of events.
# Uniform Distribution: All outcomes have equal probability.
#
# Applications:
# - Analyze examination scores.
# - Predict customer calls per hour.
# - Estimate the probability of purchasing a product.


# 5. OUTLIER DETECTION
# ------------------------------------------------------------
# Purpose: Identify unusually high or low values in a dataset.
#
# IQR (Interquartile Range):
# Measures the spread of the middle 50% of the data.
#
# Applications:
# - Detect unusual financial transactions.
# - Identify incorrect data entries.
# - Investigate unusual business performance.
#
# Python:
Q1 = df['sales'].quantile(0.25)
Q3 = df['sales'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df['sales'] < lower) |
    (df['sales'] > upper)
]


# 6. HYPOTHESIS TESTING
# ------------------------------------------------------------
# Purpose: Test an assumption using statistical evidence.
#
# Null Hypothesis (H0):
# Assumes there is no significant difference or effect.
#
# Alternative Hypothesis (H1):
# Assumes there is a significant difference or effect.
#
# P-value:
# Measures how compatible the observed results are with
# the null hypothesis.
#
# Common significance level: 0.05
#
# P-value < 0.05:
# Reject the null hypothesis.
#
# P-value >= 0.05:
# Fail to reject the null hypothesis.
#
# Applications:
# - Compare two marketing campaigns.
# - Test website conversion improvements.
# - Evaluate new business processes.
#
# Python:
from scipy import stats

t_stat, p_value = stats.ttest_ind(group_a, group_b)


# 7. REGRESSION ANALYSIS
# ------------------------------------------------------------
# Purpose: Understand relationships between variables and
# estimate or predict numerical outcomes.
#
# Linear Regression:
# Models the relationship between independent and dependent
# variables using a straight line.
#
# Independent Variable (X):
# The variable used to explain or predict another variable.
#
# Dependent Variable (Y):
# The variable being predicted or explained.
#
# Applications:
# - Predict future sales.
# - Estimate house prices.
# - Analyze the effect of advertising expenses on revenue.


# 8. COMMON PYTHON STATISTICS LIBRARIES
# ------------------------------------------------------------
#
# NumPy:
# Numerical operations and statistical calculations.
#
# Pandas:
# Data manipulation and statistical summaries.
#
# SciPy:
# Statistical tests and probability distributions.
#
# Matplotlib:
# Data visualization and statistical charts.
#
# Seaborn:
# Statistical visualization and relationship analysis.
#
# Statsmodels:
# Statistical modeling and regression analysis.
#
# Scikit-learn:
# Machine learning and predictive modeling.


# ============================================================
# KEY TAKEAWAY
# ============================================================
# Statistics is essential in Data Science because it helps us:
#
# 1. Understand and summarize datasets.
# 2. Identify patterns and relationships.
# 3. Detect unusual observations.
# 4. Test assumptions using evidence.
# 5. Make predictions and informed decisions.
#
# Goal:
# Understand what the data tells you and use statistical
# evidence to support your conclusions.
# ============================================================
