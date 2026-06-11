import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_locations(df):
    top_locations = df['location'].value_counts().head(10)

    plt.figure()
    sns.barplot(x=top_locations.values, y=top_locations.index)
    plt.title("Top Restaurant Locations")
    plt.xlabel("Number of Restaurants")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.savefig("outputs/charts/top_locations.png")

def plot_rating_distribution(df):
    plt.figure()
    sns.histplot(df['rate'], bins=20, kde=True)
    plt.title("Rating Distribution")
    plt.savefig("outputs/charts/rating_distribution.png")
