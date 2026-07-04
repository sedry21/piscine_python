def slice_me(family: list, start: int, end: int) -> list:
    # Vérifie que family est bien une liste non vide
    if not isinstance(family, list) or len(family) == 0:
        raise TypeError("family must be a non-empty list")

    # Vérifie que chaque élément est une liste
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")

    # Vérifie que toutes les lignes ont la même taille
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All rows must have the same size")

    # Shape originale
    original_shape = (len(family), row_length)
    print("My shape is :", original_shape)

    # Slicing
    new_family = family[start:end]

    # Shape après découpage
    new_shape = (len(new_family), row_length if len(new_family) > 0 else 0)
    print("My new shape is :", new_shape)

    return new_family