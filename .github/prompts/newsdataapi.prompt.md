# [Documentation](https://newsdata.io/blog/category/documentation/) How to use news API in Python: Newsdata.io

By[Prabhleen Kaur](https://newsdata.io/blog/author/prabhleen/ "Posts by Prabhleen Kaur")August 31, 2023 September 16th, 2024[No Comments](https://newsdata.io/blog/news-api-python-client/#respond)

[Blog](https://newsdata.io/blog/)\>**How to use news API in Python: Newsdata.io**

In this article, we’ll dive into the details of the “Python Client” integration guide.

## **Python Client**

With the “Client Python” section of the NewsData.io documentation, you can effortlessly integrate the API into your Python applications, whether you’re building news aggregators, data analysis tools, or research platforms.

### **Initial Steps of Integration news API in Python**

*   #### Obtain API Key
    

The first step is obtaining your unique API key by registering for an account. This serves as the authentication token for your requests.

*   #### Install newsdataapi
    

Start by installing the “newsdataapi” library using the given pip command:

`pip install newsdataapi`

*   #### Import the ‘NewsDataApiClient’ package to your program.
    

`from newsdataapi import NewsDataApiClient’`

Now, NewsData.io offers 4 endpoints i.e. **crypto news**, **latest news**, **news sources**, and **news archive\*\*\*\*API**. Let’s understand the different request parameters of each endpoint.

## **1\. ‘Latest’ News Endpoint**

‘**Latest**‘ News endpoint allows users to get the top live breaking news of the past 48 hours from all over the world. To fetch the Latest news follow the mentioned steps below.

After the initial integration, the latest news parameter would be:

*   ‘For API key authorization, Initialize the client with your API key

`api = NewsDataApiClient(apikey=’YOUR_API_KEY’)`

*   Data can now be fetched:

`response = api.news_api()``print(response) print data`

The ‘latest’ news endpoint accepts queries and other supported parameters in brackets (). Enter the information you want to retrieve data about within these brackets.

### **Let’s understand with the help of an example.**

If you want to fetch data on **Pizza**, then **q=pizza**. The request parameter of which will be:

`response = api.news_api(q=pizza)`

This will fetch all the articles related to pizza from **past 48 hours**. And to navigate to the next page you need to use the **[nextPage](https://newsdata.io/blog/newsdata-pagination/) parameter**.

To **scroll** through all the latest news extracted by news API:

`response = api.news_api(q='pizza',page='nextPage_value',scroll=True) print(response)`

The ‘**max\_result**’ parameter can be used if you don’t have enough API credits.

`response = api.news_api(q='pizza',page='nextPage_value',scroll=True,max_result=1000) print(response)`

This parameter will fetch you **1000 articles** from available articles.

## **2\. ‘Crypto’ News Endpoint**

‘**Crypto**‘ news endpoint allows users to fetch all the news articles related to cryptocurrency.

The query here is ‘**Bitcoin**‘ such that the request parameter for crypto news API is:

`api = NewsDataApiClient(apikey='YOUR_API_KEY')`

`response = api.crypto_api(q='bitcoin')`

`print(response)`

The ‘**crypto**‘ endpoint accepts queries and other supported parameters in brackets (). Enter the information you want to retrieve data about within these brackets.

The ‘**scroll=True**’ and ‘**max\_result**’ parameters can also be used to help fetch data.

## **3\. News ‘Archive’ Endpoint**

News ‘**Archive**‘ endpoint allows paid users to access **historical news** for **up to 2 years** as per the [subscription plan](https://newsdata.io/pricing). Access to older news can be further provided by contacting the website.

The query here is assumed to be pizza such that the request parameter is:

`api = NewsDataApiClient(apikey='YOUR_API_KEY')`

`response = api.archive_api(q='pizza',from_date='2021-01-01',to_date='2021-06-06')`

`print(response)`

The given query will fetch you all the articles on pizza from January 1st, 2021 to June 6th,2021.

The ‘**archive**‘ endpoint accepts queries and other supported parameters in brackets (). Enter the information you want to retrieve data about within these brackets.

The ‘**scroll=True**’ and ‘**max\_result**’ parameters can also be used to help fetch data.

You can add categories, languages, and countries as well. Check out [documentation](https://newsdata.io/documentation/#latest-news) to learn more about it.

## **4\. News ‘Sources’ Endpoint**

To get a list of **100 random sources** of Newsdata.io News API use:

`api = NewsDataApiClient(apikey="YOUR_API_KEY")`

`response = api.sources_api`

`print(response)`

The given request will fetch a list of 100 random news sources.

## **Frequently Asked Questions**

### **Q1. How to access news API in Python?**

To access news API in Python first you need to get an API key from your provider. Once done, you need to send HTTP requests to your API endpoints with the required parameters and headers to get the news data programmatically. For detailed information visit the [Python client library](https://newsdata.io/documentation/#client_py).

### **Q2. Can I filter news articles using the Python client?**

Yes, you can filter news articles using the Python client. You can filter the articles by either **filtering using a keyword** or by **filtering using tags**.