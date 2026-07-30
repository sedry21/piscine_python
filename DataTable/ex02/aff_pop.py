import matplotlib.pyplot as plt
from load_csv import load


def display_population(dataset, countries: list):
    plt.figure(figsize=(8, 6))

    # on ne garde que les colonnes années entre 1800 et 2050
    all_years = [col for col in dataset.columns if col != "country"]
    years_to_show = [y for y in all_years if 1800 <= int(y) <= 2050]

    for country in countries:
        row = dataset[dataset["country"] == country]

        if row.empty:
            print(f"Error: country '{country}' not found in dataset")
            continue

        values = row[years_to_show].iloc[0].values
        plt.plot([int(y) for y in years_to_show], values, label=country)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()
    plt.savefig("plot.png")


if __name__ == "__main__":
    dataset = load("population_total.csv")
    if dataset is not None:
        display_population(dataset, ["Madagascar", "France"])