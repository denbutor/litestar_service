import asyncio
from app.main import app, create_tables
from app.config import settings
import os
import sys

async def main():
    await create_tables()
    # запустити через CLI:
    os.execvp(
        "granian",
        ["granian", "--interface", "asgi", "--host", settings.app_host, "--port", str(settings.app_port), "app.main:app"]
    )

if __name__ == "__main__":
    asyncio.run(main())
