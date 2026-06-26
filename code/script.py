import pandas as pd
import sqlite3 as db
from init import df
from scipy.stats import chi2_contingency

conn = db.connect("mydatabase.db")

#To get all the field names and their respective types given in the dataset 
result1 = pd.read_sql_query(
    "PRAGMA table_info(Roundabouts)",
    conn
)


#To get the count of all the types of rounabouts present in the dataset
result2 = pd.read_sql_query(
    "select type, count(*) typecount from Roundabouts group by type order by typecount desc",
    conn
)


#To get the top 15 countries and the count of all the types of roundabouts present in them
result3 = pd.read_sql_query(
    "select country, count(*) as countrycount from Roundabouts group by country order by countrycount desc LIMIT 15",
    conn
)

#Identifying the target countries i.e. top 5 high-income english speaking countries.
target_countries = ['United States', 'United Kingdom', 'Australia', 'Canada', 'New Zealand']

#To get the type of roundabouts and their respective counts for top 5 high-income english speaking countries.
result4 = pd.read_sql_query(
    "SELECT country, type, COUNT(*) as count FROM roundabouts WHERE country IN ('United States', 'United Kingdom', 'Australia', 'Canada', 'New Zealand') GROUP BY country, type ORDER BY country, type",
    conn
)

#To get the percentage of the roundabouts for each country
result5 = pd.read_sql_query(
    "SELECT country, type, COUNT(*) as count, ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY country), 2) as pct FROM roundabouts WHERE country IN ('United States', 'United Kingdom', 'Australia', 'Canada', 'New Zealand') GROUP BY country, type ORDER BY country, type",
    conn
)

#To add a 'percentage' column in order to use chi-square test on the data.
df_filtered = df[df['country'].isin(target_countries)].copy()

# Reclassify i.e. anything which is not a simple roundabout gets classified into a 'Non-Standard' roundabout.
df_filtered['type_grouped'] = df_filtered['type'].apply(
    lambda x: 'Standard' if x == 'Roundabout' else 'Non-Standard'
)

# Build contingency table from raw rows
contingency = pd.crosstab(df_filtered['country'], df_filtered['type_grouped'])
contingency['total'] = contingency.sum(axis=1)
contingency['pct_nonstandard'] = (contingency['Non-Standard'] / contingency['total'] * 100).round(2)

# Drop the calculated columns, keep only the 2 type columns
chi2_table = contingency[['Non-Standard', 'Standard']]
chi2, p, dof, expected = chi2_contingency(chi2_table)

# Printing the results of the chi-squar 
print(f"Chi-square statistic: {chi2:.4f}")
print(f"P-value: {p:.6f}")
print(f"Degrees of freedom: {dof}")
print(f"\nExpected counts:\n{pd.DataFrame(expected, index=chi2_table.index, columns=chi2_table.columns).round(1)}")

conn.close()

