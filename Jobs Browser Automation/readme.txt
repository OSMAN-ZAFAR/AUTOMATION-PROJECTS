=>Jobs Browser Automation

JobScraper Pro is a Python-based browser automation project built with "Selenium" and "Undetected ChromeDriver" to fetch real-time job listings from [Indeed Pakistan](https://pk.indeed.com/).  
It automatically searches for jobs based on user-defined "keywords" and "locations", extracts relevant details, and saves them into a structured CSV file for further analysis.  

=>Features
  -> Automated search by job title & location  
  -> Extracts job details: 
     ->Job Title  
     ->Company Name  
     ->Salary (if available)  
     ->Direct Apply Link  
  ->Handles multiple pages (pagination support)  
  -> Explicit waits for stable scraping  
  -> Export results into "CSV/Excel" using Pandas  
  -> Uses "undetected-chromedriver" to avoid blocking  

=>Tech Stack
  ->"Python 3.x"  
  ->"Selenium" (browser automation)  
  ->"Undetected ChromeDriver" (anti-bot detection)  
  ->"Pandas" (data saving & analysis)  

=>Installation & Setup
  ->Clone this repository:
   ```bash
   git clone https://github.com/OSMAN-ZAFAR/AUTOMATION-PROJECTS/tree/main/Jobs%20Browser%20Automation
   cd job-scraper-pro
