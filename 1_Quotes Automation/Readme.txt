->Selenium Quotes Automation

A simple yet effective web scraping project built with **Python, Selenium, and Pandas**.  
This scraper extracts **quotes and their authors** from the website [Quotes to Scrape](https://quotes.toscrape.com/) and stores the data into a CSV file.

->Features:
 .>Scrapes quotes from multiple pages.
 .>Collects both "quote text" and "author name".
 .>Exports the data into a structured "CSV file".
 .>Demonstrates the use of "Selenium automation" with Python.

->Tech Stack
 .>Python 3.8+
 .>Seleniu
 .>Pandas
 .>ChromeDriver

-> Project Structure
 .> scraper.py          => Main scraping script
 .> requirements.txt    => Dependencies file
 .> Automation.csv      => Output file (auto-generated after run)
 .> README.md           => Documentation file

-> Installation & Setup
1. Clone the repository:
   git clone https://github.com/OSMAN-ZAFAR/selenium-quotes-scraper.git
   cd selenium-quotes-scraper

2. Install dependencies:
   pip install -r requirements.txt

3. Download ChromeDriver and update its path inside "scraper.py":
   s = Service("C:/Users/MIAUZ/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")

-> Usage
Run the scraper with:
   python scraper.py

The scraped quotes will be saved in a file named:
   Output.csv

-> Sample Output
| Quotions | Author Name |
|----------|-------------|
| "The world as we have created it is a process of our thinking." | Albert Einstein |
| "It is our choices, Harry, that show what we truly are, far more than our abilities." | J.K. Rowling |

-> Contributing
Contributions, issues, and suggestions are always welcome!  
Feel free to fork the repo, open an issue, or submit a pull request.

-> License
This project is licensed under the MIT License – you are free to use, modify, and distribute it.

-> Author
Developed by "OSMAN ZAFAR"  
GitHub: [OSMAN-ZAFAR](https://github.com/OSMAN-ZAFAR)


