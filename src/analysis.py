import pandas as pd

def analyze_data(df):
    insights = {}

    # Average rating
    insights['avg_rating'] = df['rate'].mean()

    # Top cuisines
    insights['top_cuisines'] = df['cuisines'].value_counts().head(5)

    # Cost vs rating
    insights['cost_rating_corr'] = df['approx_cost(for two people)'].corr(df['rate'])

    # Location analysis
    insights['top_locations'] = df['location'].value_counts().head(10)

    return insights
