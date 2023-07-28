from datetime import datetime, timedelta, timezone
from typing import Dict

from interface import Post

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
    4: Post(
        id=4,
        title="Sample Post 4",
        published_at=datetime(2023, 7, 29, 10, 15, 30, tzinfo=jst),
        content="This is the content of Sample Post 4.",
    ),
    5: Post(
        **{
            "id": 5,
            "title": "Sample Post 5",
            "published_at": datetime(2023, 7, 30, 10, 15, 30, tzinfo=jst),
            "content": "This is the content of Sample Post 5.",
        }
    ),
    # 他のサンプルデータ...
}
