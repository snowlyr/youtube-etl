import pandas as pd
import json
from datetime import datetime

def transform_data(raw_path):
    with open(raw_path) as f:
        raw_data = json.load(f)

    processed_records = []

    for region_data in raw_data:
        for item in region_data['items']:
            video = item['snippet']
            stats = item['statistics']

            record = {
                'video_id': item['id'],
                'title': video['title'],
                'channel_title': video['channelTitle'],
                'published_at': video['publishedAt'],
                'trending_date': datetime.now().strftime('%Y-%m-%d'),
                'region': region_data['region'],
                'view_count': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'dislikes': int(stats.get('dislikeCount', 0)),
                'comment_count': int(stats.get('commentCount', 0)),
                'category_id': video['categoryId'],
                'tags': '|'.join(video.get('tags', [])),
                'extracted_at': region_data['extracted_at']
            }
            processed_records.append(record)

    df = pd.DataFrame(processed_records)

    # Calculate derived metrics
    df['engagement_ratio'] = (df['likes'] + df['comment_count']) / df['view_count']
    df['sentiment_score'] = df['likes'] / (df['likes'] + df['dislikes'])

    return df
