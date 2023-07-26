from typing import Dict
from interface import Post

from datetime import datetime, timezone, timedelta

jst = timezone(timedelta(hours=9))

# サンプルのデータ（ダミーのブログエントリ）
sample_posts: Dict[int, Post] = {
    1: {
        "id": 1,
        "title": "Sample Post 1",
        "published_at": datetime(2023, 7, 26, 12, 30, 45, tzinfo=jst),
        "content": "This is the content of Sample Post 1.",
    },
    2: {
        "id": 2,
        "title": "Sample Post 2",
        "published_at": datetime(2023, 7, 27, 13, 45, 10, tzinfo=jst),
        "content": "This is the content of Sample Post 2.",
    },
    3: {
        "id": 3,
        "title": "Sample Post 3",
        "published_at": datetime(2023, 7, 28, 10, 15, 30, tzinfo=jst),
        "content": "This is the content of Sample Post 3.",
    },
    # 他のサンプルデータ...
}
