from __future__ import annotations

from datetime import date
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import conint

from interface import Post, PostIndex, SimpleError
from sample_data import sample_posts

app = FastAPI(
    title="Headless Blog API",
    version="1.0.0",
    servers=[{"url": "/"}],
)


@app.get("/posts", response_model=List[PostIndex])
def get_posts(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    limit: Optional[conint(le=10)] = 10,
) -> List[PostIndex]:
    """
    Get blog posts
    """
    pass


@app.post("/posts", response_model=None)
def post_posts() -> None:
    """
    Create a new blog post
    """
    pass


BPNF = "Blog post not found"


@app.get(
    "/posts/{post_id}",
    response_model=Post,
    responses={404: {"model": SimpleError, "description": BPNF}},
)
def get_posts_post_id(post_id: int) -> Post:
    """
    Get a single blog post by ID
    """
    if post_id not in sample_posts:
        # raise HTTPException(status_code=404, detail=BPNF) # どっちでも同じ
        return JSONResponse(status_code=404, content={"detail": BPNF})
    return sample_posts[post_id]


@app.put("/posts/{post_id}", response_model=None)
def put_posts_post_id(post_id: int) -> None:
    """
    Update a blog post by ID
    """
    pass


@app.delete("/posts/{post_id}", response_model=None)
def delete_posts_post_id(post_id: int) -> None:
    """
    Delete a blog post by ID
    """
    pass
