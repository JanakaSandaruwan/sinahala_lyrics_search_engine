# Sinahala Lyrics Search Engine

![alt text](ui.png)

## Quick Start
To start the search engine follow the instructions given below.

- Start an solr on the port 8983
- Run the command ```ng serve```  inside search-ui directory
- Visit <a href="http://localhost:4200">http://localhost:4200</a>
- Enter the search query in the search box in the website

## Structure of the Data

Each song contains the following data fields. The data is scraped from <a href="https://sinhalasongbook.com/">sinhalasongbook.com</a><br>

```name```: name of the song <br>
```artist```: list containing artists <br>
```genre```: list containing genres<br>
```lyrics_by```: list containing lyric writers <br>
```music```: list containing music directors <br>
```key:``` key of the song<br>
```beat:``` beat of the song<br>
```visits:``` no of views for the song in original site<br>
```lyrics:``` lyric (each line seperated by a \n character)<br>

## Indexing and Querying Techniques Used


