# Roundabout Analysis

Dataset used: [Roundabouts Across the World 27K](https://www.kaggle.com/datasets/ibrahimqasimi/roundabouts-across-the-world-27k)

## Problem
I want to find out whether countries differ in the how frequently they use non-standard roundabout designs, specifically for the following countries: United States, United Kingdom, Australia, Canada, and New Zealand.

## Approach
I started with a larger data set, and after some analysis, I figured that it is better to isolate the countries in accordance to their roundabout use as a lot of countries didnt have data on certain types of roundabouts. Initial exploration revealed significant geographic bias in the dataset, 15 of the top 15 countries by row count were high-income nations, with the US alone comprising 46% of all records. This reflects OpenStreetMap's mapping coverage rather than global roundabout distribution. The analysis was therefore scoped to five comparable high-income English-speaking countries to enable a fair comparison. 

The next issue was to prove my hypothesis, for which I chose to do a chi-squared test on the data set, but due to multiple types of "non-standard" roundabouts and them not being available in all the filtered countries all at once, I had to resort to classifying the roundabouts in 2 type:
1. Standard - Roundabouts
2. Non-Standard - Rotatry, Signalised roundabout/circle, Traffic Calming Circle, Other, Unknown.

## Findings
I found out that the percentage of non-standard roundabouts is the highest in America and a significantly lesser amount in both Australia and New Zealand, with Canada and the UK being the mid-runners. The second graph shows the disparity between the roundabout types per country, and we can see that Australia and New Zealand have really low non-standard roundabouts as compared to their standard roundabout, which can imply that a standard design might have been opted for across the mentioned countries.

A chi-square test of independence confirmed this association is statistically significant (χ²=1647.26, df=4, p<0.001), meaning the probability of observing this distribution by chance, if country had no effect on roundabout type, is essentially zero.

<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/51a99914-03e0-4775-80ac-50f3170a189c" />

<img width="640" height="480" alt="Figure_2" src="https://github.com/user-attachments/assets/5fff7d89-293b-4b69-a984-cf2d8bfcec83" />

## Reccomendations
For infrastructure consultants working across these five countries, these findings suggest that Australia and New Zealand have effectively standardised their roundabout design, procurement and construction planning in those markets can assume standard designs as the default. In the US and UK, where 26% and 11% of roundabouts respectively, are non-standard, budgets should account for higher design variability, the additional $150,000–$400,000 per non-standard installation is a material planning consideration at scale.

## Software and Libraries involved
```
SQLite, Python, Seaborn, Matplotlib
```
## Setup
```
1. Download the dataset from the link given and place it as 'data/roundabouts.csv'
2. Run init.py to set up the database and import the data from the dataset.
3. script.py contains the data handling.
4. visualisation.py is used to plot graphs.
```
