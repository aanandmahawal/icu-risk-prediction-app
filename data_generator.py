import pandas as pd
import numpy as np

def generate_synthetic_data(n_samples=1000):
    np.random.seed(42)
    X = pd.DataFrame({
        'HR': np.random.normal(80, 10, n_samples),
        'BP': np.random.normal(120, 15, n_samples),
        'Temp': np.random.normal(98.6, 1.0, n_samples),
        'RespRate': np.random.normal(18, 2, n_samples),
        'ComorbidityIndex': np.random.randint(0, 5, n_samples)
    })

    risk_score = (
        (X['HR'] > 90).astype(int) +
        (X['BP'] < 110).astype(int) +
        (X['RespRate'] > 20).astype(int) +
        (X['ComorbidityIndex'] > 2).astype(int)
    )

    y = (risk_score >= 2).astype(int)
    return X, y
