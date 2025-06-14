### Objective of analysis ###
# Sample 80% of data to plot a linear regression model of
# engagement_ratio = view_count + likes + comment_count + category_id
# Use remaining 20% of the data to test the accuracy of the model
### End ###

import pandas as pd
import sqlite3
import statsmodels.api as sm

# Declare FilePaths
DATA_FILE_PATH = "../data/youtube.db"
IMAGE_FILE_PATH = "./visualisation/category_trends.png"

# Connect to database
conn = sqlite3.connect(DATA_FILE_PATH)

# Import Data
data_df = pd.read_sql("""
    SELECT DISTINCT view_count, engagement_ratio, likes, comment_count
    FROM trending_videos
""", conn)
# print(data_df)
print("[INFO] Loaded data_df")

# Sample 80% of data
train_df = data_df.sample(frac=0.8,random_state=10)
test_df = data_df.drop(train_df.index)

# Build Model on training data
# Note: No use in splitting train and test data for numerical response variables, doing this for practice with pandas and statsmodels.api
X = sm.add_constant(train_df[["view_count","likes","comment_count"]])
Y = train_df["engagement_ratio"]

model = sm.OLS(Y,X).fit()
print("[INFO] Model built successfully")
print(model.summary())

# Test model on 20% of data with metrics
pass

