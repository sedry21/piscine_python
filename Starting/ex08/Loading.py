from time import time

def ft_tqdm(iterable):
    """
    Crée une barre de chargement type tqdm.
    
    Affiche :
    - Pourcentage de progression
    - Barre visuelle
    - Nombre d'éléments traités / total
    - Temps écoulé
    - Temps estimé restant
    """
    start_time = time()
    total = len(iterable)
    
    for i, item in enumerate(iterable):
        yield item
        
        # Calcul de la progression
        current = i + 1
        percentage = (current / total) * 100
        elapsed = time() - start_time
        rate = current / elapsed if elapsed > 0 else 0
        remaining_time = (total - current) / rate if rate > 0 else 0
        
        # Formatage du temps
        def format_time(seconds):
            mins, secs = divmod(int(seconds), 60)
            return f"{mins:02d}:{secs:02d}"
        
        # Création de la barre (30 caractères de largeur)
        bar_width = 30
        filled = int(bar_width * current / total)
        bar = "█" * filled + "░" * (bar_width - filled)
        
        # Affichage de la progression
        progress = f"{percentage:6.2f}%|{bar}|{current}/{total} [{format_time(elapsed)}<{format_time(remaining_time)}]"
        print(f"\r{progress}", end="", flush=True)
    
    print()  # Nouvelle ligne à la fin
