# NewsData API Bruno Collection

This Bruno collection provides comprehensive access to the NewsData.io API free tier endpoints.

## Setup

1. Update the `api_key` variable in `environments/Local.bru` with your actual NewsData.io API key
2. You can get a free API key by signing up at [newsdata.io](https://newsdata.io/)

## Available Endpoints

### 1. Get Latest News
- **File**: `Get Latest News.bru` 
- **Description**: Fetch the latest news articles
- **Parameters**: country, language, category, search query, timeframe, etc.

### 2. Get News Archive
- **File**: `Get News Archive.bru`
- **Description**: Search historical news articles with date range
- **Parameters**: query, country, language, category, from_date, to_date

### 3. Get News Sources
- **File**: `Get News Sources.bru`
- **Description**: Retrieve available news sources
- **Parameters**: country, language, category

### 4. Get Crypto News
- **File**: `Get Crypto News.bru`
- **Description**: Fetch cryptocurrency-related news
- **Parameters**: coin, country, language, timeframe

### 5. Search News by Query
- **File**: `Search News by Query.bru`
- **Description**: Search news articles by specific keywords
- **Parameters**: search query, country, language, category

### 6. Get News by Category
- **File**: `Get News by Category.bru`
- **Description**: Fetch news from specific categories
- **Categories**: business, entertainment, environment, food, health, politics, science, sports, technology, top, tourism, world

### 7. Get News by Country
- **File**: `Get News by Country.bru`
- **Description**: Fetch news from specific countries
- **Parameters**: country code (ISO 3166-1 alpha-2)

### 8. Get News by Domain
- **File**: `Get News by Domain.bru`
- **Description**: Fetch news from specific domains
- **Parameters**: domain name

### 9. Get News with Pagination
- **File**: `Get News with Pagination.bru`
- **Description**: Example of paginated results
- **Parameters**: size, page token

### 10. Get Full Text News
- **File**: `Get Full Text News.bru`
- **Description**: Fetch news with full article content (Premium feature in free trial)
- **Parameters**: full_content flag

## Common Parameters

- `apikey`: Your NewsData.io API key (required)
- `q`: Search query
- `qInTitle`: Search in title only
- `qInMeta`: Search in meta description
- `country`: Country code (us, gb, in, etc.)
- `language`: Language code (en, es, fr, etc.)
- `category`: News category
- `timeframe`: Time range in hours (24, 48, 72)
- `from_date` / `to_date`: Date range (YYYY-MM-DD format)
- `size`: Number of results (max 50 for free tier)
- `page`: Pagination token
- `domain`: Specific domain to search
- `domainurl`: Specific domain URL
- `excludedomain`: Domains to exclude
- `prioritydomain`: Priority domain ranking
- `removeduplicate`: Remove duplicate articles (1 or 0)

## Free Tier Limitations

- 200 requests per day
- Maximum 10 results per request for /news endpoint
- Maximum 50 results per request for /archive endpoint
- Historical data limited to last 30 days
- Some features require paid subscription

## Usage Notes

- Parameters prefixed with `~` in Bruno files are disabled by default
- Remove the `~` prefix to enable a parameter
- Update parameter values as needed for your use case
- The `full_content` parameter is available in premium plans

## Environment Variables

Set these in your Bruno environment:
- `base_url`: https://newsdata.io/api/1
- `api_key`: Your actual API key from newsdata.io
