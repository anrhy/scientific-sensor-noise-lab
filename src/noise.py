import numpy as np

def generate_signal(
        n_points: int = 1000,
        frequency: float = 1.0
)-> np.ndarray:
    x = np.linspace(0,10,n_points)
    signal = np.sin(frequency * x)
    return signal

def add_gaussian_noise(
        signal: np.ndarray,
        sigma: float = 0.2
)-> np.ndarray:
    noise = np.random.normal(0,sigma,size=signal.shape)
    return signal + noise
