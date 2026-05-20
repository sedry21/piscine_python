import time
from datetime import datetime

# Obtenir le timestamp actuel en secondes depuis le 1er janvier 1970
seconds = time.time()

# Formater les secondes avec virgules comme séparateur de milliers
formatted_seconds = f"{seconds:,.4f}"

# Notation scientifique
scientific_notation = f"{seconds:.2e}"

# Obtenir la date actuelle
now = datetime.now()
date_str = now.strftime("%b %d %Y").lstrip("0").replace(" 0", " ")

# Afficher le résultat
print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation$")
print(f"{date_str} \"")

