# 📂 Python Job Market Analysis — Czech Republic 🇨🇿

**Project:** Data collection, analysis, and visualization of Python developer vacancies from [Jobs.cz](https://www.jobs.cz/).

---

## 📌 Project Description

This project focuses on collecting, processing, and visualizing Python job market data in the Czech Republic.  
It demonstrates skills in data scraping, data analysis, data visualization, and automation using Python.

---

## 🔧 Technologies Used

- **Python 3.11+**
- **Pandas** — for data manipulation
- **Matplotlib** — for data visualization
- **WordCloud** — for text data visualization
- **Selenium** — for browser automation
- **BeautifulSoup** — for HTML parsing
- **Regular Expressions (re)** — for extracting salary information

---

## 📊 Project Features

- Automatic scraping of job listings from Jobs.cz
- Data saving into an Excel file
- Extraction of salary information from job titles
- Identification of the most demanded specializations
- Geographic analysis of job opportunities across cities
- Generation of a WordCloud based on job title keywords
- Building and saving professional visualizations

---

## 📈 Analysis

- **Salary Analysis:** Extracted salary information where available, plotted salary distribution histograms and boxplots.
- **Specializations Analysis:** Identified and ranked popular Python specializations such as Data Science, Machine Learning, Web Development, etc.
- **Location Analysis:** Highlighted cities with the highest number of Python job offers.
- **Keyword Visualization:** Generated a WordCloud to show frequently mentioned skills and keywords in job titles.

---

## 📊 Results

- The majority of job offers did not explicitly state salary information.
- Data Science and Web Development were among the most frequently mentioned specializations.
- Prague was the dominant city for Python job opportunities, followed by Brno and Ostrava.
- Keywords like Python, Engineer, Developer, Data, and AI appeared most often in job titles.

---

## 🧠 Conclusion

This project demonstrates the ability to:

- Automatically collect and clean real-world data.
- Perform meaningful analysis on small datasets.
- Present findings clearly through professional visualizations.
- Handle inconsistencies in real data (e.g., missing salaries).

---

## 🚀 Future Work

- Expand scraping to other job platforms like Prace.cz or LinkedIn Jobs.
- Add salary extraction from detailed job descriptions.
- Implement sentiment analysis of job ads.
- Develop a Telegram bot for job notifications.
- Build an interactive dashboard with Plotly or Dash.

---

## 👩‍💻 About the Author

Author: **Mariia Biriulova**

**Python Skills:**
- Django/Flask web development (full websites and landing pages)
- Telegram bots development (with Google Sheets integration and admin panel)
- Excel and Google Sheets automation
- Web scraping (Selenium, BeautifulSoup)
- Data Analysis & Visualization (Pandas, Matplotlib, WordCloud)
- Data Science fundamentals (statistics, mathematics, regression models)
- SQL and database management
- HTML, CSS, JavaScript for responsive web development

**📬 Contacts:**
- [Telegram](https://t.me/s_masha_s)
- [LinkedIn](https://www.linkedin.com/in/mariia-biriulova-bb9aa3297)

---

# 📂 Project Structure

```bash
├── parser_jobs.py            # Scraping job data from jobs.cz
├── analyze_jobs.py           # Analyzing and visualizing collected data
├── jobs_filtered.xlsx        # Raw collected job data
├── salary_histogram.png      # Salary distribution histogram
├── salary_boxplot.png        # Salary boxplot
├── specializations_bar_chart.png # Specializations bar chart
├── top_cities_bar_chart.png  # City distribution bar chart
├── wordcloud.png             # WordCloud of job titles
├── README.md                 # Project description
├── requirements.txt          # List of required libraries
```