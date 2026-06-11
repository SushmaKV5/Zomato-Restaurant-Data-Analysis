import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.dropna(subset=['rate', 'approx_cost(for two people)'], inplace=True)

    # Clean rating column
    df['rate'] = df['rate'].str.replace('/5', '')
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

    # Clean cost column
    df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.replace(',', '')
    df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')

    return df

if __name__ == "__main__":
    df = clean_data("data/raw/zomato.csv")
    df.to_csv("data/processed/cleaned_zomato.csv", index=False)
