import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        dataset = pd.read_csv(path)
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    print(f"Loading dataset of dimensions {dataset.shape}")
    return dataset