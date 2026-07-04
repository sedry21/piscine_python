from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    try:
        img = ft_load("test.jpg")
        print(img)

        # Découpe d'une zone 400x400
        zoom = img[100:500, 450:850]

        # Conversion en niveaux de gris
        gray = zoom.mean(axis=2).astype(np.uint8)

        print("New shape after slicing:", gray.shape)
        print(gray)

        # Affichage
        plt.imshow(gray, cmap="gray")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()