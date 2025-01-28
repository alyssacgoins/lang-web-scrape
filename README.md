# Lang-Web-Scrape
Welcome to Lang-Web-Scrape. This program scrapes the body text from the webpage at the input URL, 
and produces a CSV file containing the words, cleaned of all extraneous symbols. Program is used in
conjunction with Translate-German, which takes in a CSV file of German words and outputs 
an Excel doc containing the input words paired with their English translations. 

## Program input
### url
Required argument. URL of webpage to be scraped.
### source_lang
Optional argument. Language of input webpage. If not specified, default value is DE (German).
### target_lang
Optional argument. Language in which input webpage is to be later translated. If not specified, 
default value is EN (English).

## Program Output
Processed words retrieved from webpage are output into CSV file labeled "body-text.csv", located in 
root directory.