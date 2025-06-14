import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3

# Declare FilePaths
DATA_FILE_PATH = "../data/youtube.db"
IMAGE_FILE_PATH = "./visualisation/category_trends.png"

# Connect to database
conn = sqlite3.connect(DATA_FILE_PATH)

# Top 10 videos by engagement
print("=============== Top 10 By Engagement ===============")
top_engagement = pd.read_sql("""
    SELECT DISTINCT title, channel_title, MAX(view_count) as view_count, MAX(engagement_ratio) as engagement_ratio
    FROM trending_videos
    GROUP BY title
    ORDER BY engagement_ratio DESC
    LIMIT 10
""", conn)
print(top_engagement)

print()
# Top 10 videos by View Count
print("=============== Top 10 By View Count ===============")
top_view = pd.read_sql("""
    SELECT DISTINCT title, channel_title, MAX(view_count) as view_count, MAX(engagement_ratio) as engagement_ratio
    FROM trending_videos
    GROUP BY title
    ORDER BY view_count DESC
    LIMIT 10
""", conn)
print(top_view)

# Trending categories by region
category_trends = pd.read_sql("""
    SELECT region, category_id, COUNT(*) as video_count
    FROM trending_videos
    GROUP BY region, category_id
    ORDER BY video_count DESC
""", conn)

# Plot Graph with seaborn and matplotlib
plt.figure(figsize=(12, 6))
sns.barplot(data=category_trends, x='category_id', y='video_count', hue='region')
plt.title('Trending Video Categories by Region')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(IMAGE_FILE_PATH)
print(f"[INFO] Plot created at {IMAGE_FILE_PATH}")
