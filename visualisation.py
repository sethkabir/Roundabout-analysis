from script import df_filtered, contingency
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting a bar graph to show the percentage of Non-Standard roundabouts for the 5 targeted countries.
contingency['pct_nonstandard'].sort_values(ascending=False).plot(
    kind='bar', 
    color='steelblue'
)
plt.ylabel('% Non-Standard Roundabouts')
plt.xlabel('Country')
plt.title('Non-Standard Roundabout Usage by Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting a bar graph to show the percentage of Standard and Non-Standard roundabouts for the 5 targeted countries.
contingency[['Standard', 'Non-Standard']].plot(
    kind='bar', 
    stacked=True,
    color=['lightgray', 'crimson']
)
plt.ylabel('Number of Roundabouts')
plt.title('Roundabout Types by Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()