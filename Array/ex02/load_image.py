from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        # Vérification de l'extension
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise ValueError("Only JPG and JPEG formats are supported.")

        # Ouverture de l'image
        img = Image.open(path)

        # Conversion en RGB
        img = img.convert("RGB")

        # Conversion en tableau numpy
        img_array = np.array(img)

        # Affichage de la shape
        print("The shape of image is:", img_array.shape)

        return img_array

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' not found.")
    except Exception as e:
        raise Exception(f"Error loading image: {e}")