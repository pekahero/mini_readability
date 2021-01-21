## Idea behind the code.
The goal is to format article given by URL by throwing away everything except pure text and links in this text.
I assume all content of an article is placed inside single tag. One of these: div, article, section, main.
Basically, task is to find tag with the greatest number of sentences. Sentences can be found with regular expressions.

## Algorithm.
1) Download page by URL from args.
2) Create BeautifulSoup object.
3) Clean it up of unwanted tags.
4)  Recursive tree search for tags from mentioned above group that have no children from that group. 
    Count sentences and delete this tag. Go to extracted node's parent and repeat.
5) Format found text.
6) Save file or create a folder first if needed.

## Files:
- main.py - main executable file.
- data_from_url.py - file for downloading article.
- page_scrapper.py - file for soup and searching for biggest tag.
- convert_to_text.py - converting to text file.
- tag_format_rules.py - format rules file for tags.
- configs.py - program's configurations/options file.
- all_urls.cmd - run program for all test articles.

## External libraries:
- lxml.
- bs4.
- requests.

## What can be set in configs:
- Maximum width of text.
- Where to save file in a current directory or set another directory.
- Name a folder where articles are saved.
- Set unwanted/wanted tags.
- Set if write information about running and result into the console.
- Possibility to set tag format rules.

## Things to add:
- Creating directories based on URL.
- Saving as pdf or other document formats. Allows adding pictures and tables, text sizes and styles.
- Add various formatting styles. 
- Add tables to txt format by "|,-,+" symbols.
- Improvements to current algorithms.

## Tests.
 All test URLs are written in "all_urls.cmd". Results are saved to the folder "articles".
