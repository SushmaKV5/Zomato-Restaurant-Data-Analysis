from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import plot_top_locations, plot_rating_distribution

def main():
    df = clean_data("data/raw/zomato.csv")

    insights = analyze_data(df)
    print("Key Insights:", insights)

    plot_top_locations(df)
    plot_rating_distribution(df)

if __name__ == "__main__":
    main()
