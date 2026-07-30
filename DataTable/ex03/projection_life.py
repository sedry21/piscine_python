import matplotlib.pyplot as plt
from load_csv import load


def display_projection(gdp_dataset, life_dataset, year: str):
    if year not in gdp_dataset.columns or year not in life_dataset.columns:
        print(f"Error: year '{year}' not found in dataset")
        return

    # on fusionne les deux datasets sur la colonne "country"
    merged = gdp_dataset[["country", year]].merge(
        life_dataset[["country", year]],
        on="country",
        suffixes=("_gdp", "_life")
    )

    merged = merged.dropna()

    x = merged[f"{year}_gdp"]
    y = merged[f"{year}_life"]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.7)
    plt.title(f"Life expectancy VS GDP in {year}")
    plt.xlabel("GDP per capita")
    plt.ylabel("Life expectancy")
    plt.savefig("plot.png")


if __name__ == "__main__":
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    if gdp is not None and life is not None:
        display_projection(gdp, life, "1900")