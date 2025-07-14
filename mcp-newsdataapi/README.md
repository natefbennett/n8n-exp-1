# NewsDataAPI MCP Server

![Python](https://img.shields.io/badge/python-3.10%2B-blue)

Model Context Protocol server for real-time news search via [NewsData.io](https://newsdata.io/) API.

> **Note:** Uses NewsData.io free tier (200 requests/day, 10 articles per request)

## Setup

1. Get your [NewsData.io API key](https://newsdata.io/register)
2. Create `.env`: `NEWS_API_KEY=your_api_key_here`
3. Run with Docker: `docker compose up mcp-newsdataapi --build`

Server available at `http://localhost:8000`

## MCP Tools

- `get_latest_news()` - Latest headlines
- `search_news(query, max_pages=1)` - Search by keyword  
- `summarize_news(query)` - Generate summary prompt

## Local Development

Simply build the Docker image.

```shell
docker build -t mcp-newsdataapi .
```

It then can be run directly.

```shell
docker run --rm `
   --env-file .env `
   --port 8000:8000 `
   mcp-newsdataapi
```

Alternatively it can be run locally.

```shell
uv sync
uv run python main.py --port 8000
```
