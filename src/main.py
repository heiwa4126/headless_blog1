from __future__ import annotations

from datetime import date
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status, Response
from fastapi.responses import JSONResponse
from pydantic import conint

from interface import Post, PostIndex, SimpleError
from sample_data import sample_posts as post_data

import os

PROD_OPT = (
    {"docs_url": None, "redoc_url": None, "openapi_url": None}
    if (os.getenv("FASTAPI_ENV", "") == "production")
    else {}
)

app = FastAPI(
    title="Headless Blog API", version="1.0.0", servers=[{"url": "/"}], **PROD_OPT
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
    responses={status.HTTP_404_NOT_FOUND: {"description": BPNF, "model": SimpleError}},
)
def get_posts_post_id(post_id: int) -> Post:
    """
    Get a single blog post by ID
    """
    if post_id not in post_data:
        # raise HTTPException(status_code=404, detail=BPNF) # オリジナル
        # return JSONResponse(status_code=404, content={"detail": BPNF})  # これでもOK
        # return JSONResponse({"detail": BPNF}, status.HTTP_404_NOT_FOUND)  # これでもOK
        return JSONResponse(
            SimpleError(detail=BPNF).model_dump(), status.HTTP_404_NOT_FOUND
        )  # これでもOK
    return post_data[post_id]


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
