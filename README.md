# TAMU-Degree-Planner

The TAMU-Degree-Planner is a tool designed to help Texas A&M University students generate a comprehensive degree plan. By utilizing data scraped from the Texas A&M UCC Requirements website and the base degree plan provided by the university, this tool helps students map out their courses based on their major and AP credits.

## About

This project was created for TidalHack at Texas A&M University by a rookie team. Our goal is to provide an easy-to-use degree planning tool for students to navigate their course requirements more effectively.

## Features

* **Links and Majors Handling**: Retrieves and displays available majors from provided URLs.
* **User Input Handling**: Prompts the user to select a major and input their AP exam scores.
* **Web Scraping**: Uses BeautifulSoup to scrape the degree requirements from the selected major's webpage.
* **AP Exam Credits Processing**: Matches user's AP credits against degree requirements.
* **UCC Credit Calculation**: Calculates remaining UCC credits needed and suggests courses to fulfill them.

## Usage Instructions

1. **Select Your Major:**
   The program will display a list of available majors. Enter the number corresponding to your major.

2. **Input AP Exam Scores:**
   Follow the prompts to input your AP exam scores. Enter 'quit' when you have finished entering your scores.

3. **Receive Degree Plan:**
   The program will output a suggested degree plan based on your input.

## OpenAI Implementation

*Placeholder for how OpenAI environment will be integrated into the project.*

## Example Output

```plaintext
You selected #12 which is Computer Science - BS

Thank you for entering your AP tests. You have credit for:
MATH 151 | CHEM 119 | ENGL 104

You need:
3 more credit hours for Communication,
4 more credit hours for American History,
...

For your degree plan, we recommend you take the following courses:
For the Communication category, we recommend ENGL 203, 3 credit hours
For the American History category, we recommend HIST 105, 4 credit hours
...
