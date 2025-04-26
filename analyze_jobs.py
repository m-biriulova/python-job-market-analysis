import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_excel('jobs_filtered.xlsx')

# -- ANALYSIS BY SALARY -- #
def extract_salary(title):
    title = title.lower()

    az_match = re.search(r"až\s*(\d{2,3}[\. ]?\d{3})", title)
    if az_match:
        salary = az_match.group(1)
        salary = salary.replace(".", "").replace(" ", "")
        return int(salary)

    range_match = re.search(r"\d{2,3}[ -]\d{2,3}[\. ]?\d{3}", title)
    if range_match:
        upper_salary = re.findall(r"\d{2,3}[\. ]?\d{3}", range_match.group(0))[-1]
        upper_salary = upper_salary.replace(".", "").replace(" ", "")
        return int(upper_salary)

    salary_match = re.search(r"(\d{2,3}[\. ]?\d{3}|\d{5,6}|\d{2,3}k)", title)
    if salary_match:
        salary = salary_match.group(0)
        salary = salary.replace(".", "").replace(" ", "").replace("k", "000")
        return int(salary)

    return None

df['Salary'] = df['Title'].apply(extract_salary)

salary_df = df[df['Salary'].notna()]

plt.figure(figsize=(10, 6))
plt.hist(salary_df['Salary'], bins=5, edgecolor='black')
plt.title('Distribution of Salaries')
plt.xlabel('Salary (CZK)')
plt.ylabel('Number of Vacancies')
plt.grid(True)
plt.savefig('salary_histogram.png')
plt.close()

plt.figure(figsize=(6, 8))
plt.boxplot(salary_df['Salary'], vert=True, patch_artist=True)
plt.title('Salary Distribution - Boxplot')
plt.ylabel('Salary (CZK)')
plt.grid(True)
plt.savefig('salary_boxplot.png')
plt.close()

print("The charts have been saved: salary_histogram.png и salary_boxplot.png")


# -- ANALYSIS BY SPECIALIZATIONS -- #
specializations = {
    "Data Science": ["data science", "data scientist"],
    "Machine Learning": ["machine learning", "ml engineer"],
    "Web Development": ["web developer", "django", "flask"],
    "DevOps": ["devops", "site reliability engineer", "sre"],
    "AI Engineer": ["ai engineer", "artificial intelligence"],
    "Automation": ["automation", "automation engineer"],
    "Analytics": ["analytics", "business intelligence", "bi"],
    "Backend Development": ["backend developer", "back-end developer"],
    "Data Engineer": ["data engineer"],
}

spec_counts = {spec: 0 for spec in specializations}

for title in df['Title']:
    title_lower = title.lower()
    for spec, keywords in specializations.items():
        for keyword in keywords:
            if keyword in title_lower:
                spec_counts[spec] += 1

spec_counts = {spec: count for spec, count in spec_counts.items() if count > 0}

plt.figure(figsize=(12, 6))
plt.bar(spec_counts.keys(), spec_counts.values(), color='skyblue', edgecolor='black')
plt.xticks(rotation=45, ha='right')
plt.title('Demand for Python Specializations')
plt.xlabel('Specialization')
plt.ylabel('Number of Vacancies')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('specializations_bar_chart.png')
plt.close()

print("The chart has been saved: specializations_bar_chart.png")

# WordCloud
text = " ".join(title for title in df['Title'].dropna())

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    max_words=100
).generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('WordCloud of Python Job Titles')
plt.savefig('wordcloud.png')
plt.close()

print("WordCloud has been saved: wordcloud.png")

# -- ANALYSIS BY CITIES -- #
city_counts = df['Location'].dropna().value_counts()

top_cities = city_counts.head(10)

plt.figure(figsize=(10, 6))
top_cities.plot(kind='barh', color='lightcoral', edgecolor='black')
plt.xlabel('Number of Vacancies')
plt.ylabel('City')
plt.title('Top Cities by Python Vacancies')
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.savefig('top_cities_bar_chart.png')
plt.close()

print("The chart has been saved: top_cities_bar_chart.png")