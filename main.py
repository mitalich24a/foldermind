"""
FolderMind
Copyright (c) 2026 Mitali Choubisa. All rights reserved.

No part of this software may be copied, modified, distributed, or used
without prior written permission from the author.
"""

from fastapi import FastAPI

from app.api.sources import router as sources_router

from app.api.chat import router as chat_router

app = FastAPI(
    title="FolderMind",
    description="AI-powered knowledge platform.",
    version="1.0.0",
)

app.include_router(sources_router)
app.include_router(chat_router)

@app.get("/")
def health_check():
    return {
        "status": "FolderMind Running",
        "version": "1.0.0",
    }