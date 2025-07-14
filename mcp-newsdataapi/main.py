#!/usr/bin/env python3
"""
HTTP MCP Server for News Search
This runs the MCP server over HTTP transport instead of stdio.
Provides general news search functionality using NewsData.io API.
"""

from mcp.server.fastmcp import FastMCP, Context
from newsdataapi import NewsDataApiClient
from typing import List, Dict, Any
from dotenv import load_dotenv
import os
import argparse

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("NEWS_API_KEY")
if not API_KEY:
    raise ValueError("NEWS_API_KEY not found in .env file")

# Initialize the NewsData API client
news_client = NewsDataApiClient(apikey=API_KEY)


parser = argparse.ArgumentParser(description="News Search MCP HTTP Server")
parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
args = parser.parse_args()

print(f"Starting MCP HTTP server on {args.host}:{args.port}")

# Initialize the MCP server with stateless HTTP for better n8n compatibility
mcp = FastMCP(
    "NewsSearchServer",
    stateless_http=True,
    host=args.host,
    port=args.port
)

# Helper function to fetch news from the API with pagination using NewsDataApiClient
def fetch_news(query: str = None, max_pages: int = 1) -> List[Dict[str, Any]]:
    all_articles = []
    next_page = None  # Start with no page token for the first request

    # Fetch up to max_pages
    for page_num in range(max_pages):
        try:
            # Use news_api for all news queries (free tier)
            if next_page:
                if query:
                    response = news_client.news_api(q=query, page=next_page, language="en")
                else:
                    response = news_client.news_api(page=next_page, language="en")
            else:
                if query:
                    response = news_client.news_api(q=query, language="en")
                else:
                    response = news_client.news_api(language="en")

            # Extract articles from response
            articles = response.get("results", [])
            all_articles.extend(articles)

            # Get the nextPage token from the response
            next_page = response.get("nextPage")

            # Stop if there's no nextPage or no more articles
            if not next_page or not articles:
                break

        except Exception as e:
            print(f"Error fetching news: {e}")
            break

    return all_articles

# Tool: Fetch the latest news headlines
@mcp.tool()
def get_latest_news(ctx: Context) -> str:
    """
    Fetch the latest news headlines.

    Returns:
        str: A formatted string of the latest news headlines with publication dates.
    """
    ctx.info("Fetching latest news headlines")
    articles = fetch_news()
    headlines = "\n".join(
        f"Title: {article['title']}\n"
        f"Published: {article['pubDate']}\n"
        f"Description: {article['description'] or 'No description available'}\n"
        for article in articles
    )
    return headlines if headlines else "No recent news available."

# Tool: Search for news articles by keyword with pagination
@mcp.tool()
def search_news(query: str, max_pages: int = 1, ctx: Context = None) -> str:
    """
    Search for news articles by keyword or topic with pagination support.

    Parameters:
        query (str): The keyword or topic to search for (e.g., 'bitcoin', 'ethereum', 'technology').
        max_pages (int, optional): Maximum number of pages to fetch (default: 1). Each page typically contains up to 10 articles.

    Returns:
        str: A formatted string containing news article titles, dates, and descriptions.
    """
    ctx.info(f"Searching news for query: {query} with max_pages: {max_pages}")
    articles = fetch_news(query=query, max_pages=max_pages)

    print(articles)

    if not articles:
        return f"No news found for query '{query}'."

    result = "\n\n".join(
        f"Title: {article['title']}\n"
        f"Published: {article['pubDate']}\n"
        f"Description: {article['description'] or 'No description available'}"
        for article in articles
    )
    return result

# Prompt: Summarize news
@mcp.prompt()
def summarize_news(query: str) -> str:
    """Generate a prompt to summarize news for a specific topic or keyword"""
    return (
        f"Please summarize the latest news about {query} based on the following data:\n\n"
        f"{{{{ search_news(\"{query}\") }}}}"
    )

# Run FastMCP instance
mcp.run("sse")
