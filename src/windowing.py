import numpy as np

def create_windows(series, window_size=60, step=1):
    """
    Convert a 1D time series into sliding windows.
    """
    windows = []

    for i in range(0, len(series) - window_size, step):
        window = series[i : i + window_size]
        windows.append(window)

    return np.array(windows)


if __name__ == "__main__":
    # Quick test
    dummy_series = np.arange(100)
    windows = create_windows(dummy_series, window_size=10)

    print("Window shape:", windows.shape)
