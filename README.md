# InfluenceChecker
## Assess the Performance of 'Not Financial Advice' from Digital Asset Influencers on YouTube
#### Created: Jan. 6th 2025 by John Walsh

###
 Prototype
 ---
####
During the construction of the prototype, Python is the primarily language of developement, as progress occurs Scala and/or Java may likely be implemented to improve performance. Particularly during the API calls and initial text processing. 

Once the text is processed, it will need to be summarized. Open-Source pre-trained summarization models will likely be employed to ensure accurate and performant summarization occurs. 

After summarization, the performance of the respective assets will need to be assessed, this will likely happen through another API like Coin Metrics, Coin Market Cap, Moralis Money, etc. 

The initial asset performance will be fairly remedial and will need to be improved as time goes on. 

For now, the main post summarization questions are the following: 
 - "Did the asset's value increase?" 
 - "Over what time periods after release of the video did the asset perform the best?" 
####
---
###

### This project consists of three major components
#### Scrape, Summaraize, Analyze
 1) Youtube Transcript Scraper (InfluenceScrape)
 2) Transcript Summarization (TranscriptSummarize)
 3) Relative Asset Performance (InfluenceCheck)

### 1) InfluenceScraper
---
####
 - Uses Google's Youtube API to enable user to scrape transcripts for popular digital asset channels
 - This api call should be limited to respect rate limits and get transcipts in a reasonable amount of time
 - Methods should be explored for interacting with channels to filter by videos with keywords in titles or relevance to asset of interest
---
### 2) TranscriptSummarize
---
####
 - ...
 - ...
 - ...
---
### 3) InfluenceCheck
---
####
 - ...
 - ...
 - ...
---


### Configuring The Development Environment
#### Tools
---
 - Developing Requires Pipenv, PyTest, MyPy, and Ruff
---
