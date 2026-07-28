import matplotlib.pyplot as plt
from load_csv import load


def display_country(dataset, country: str):
    # on récupère la ligne correspondant au pays
    row = dataset[dataset["country"] == country]

    if row.empty:
        print(f"Error: country '{country}' not found in dataset")
        return

    # on retire la colonne "country" pour ne garder que les années/valeurs
    years = row.columns[1:].astype(int)
    values = row.iloc[0, 1:].values

    plt.figure(figsize=(8, 6))
    plt.plot(years, values)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    dataset = load("life_expectancy_years.csv")
    if dataset is not None:
        display_country(dataset, "France")