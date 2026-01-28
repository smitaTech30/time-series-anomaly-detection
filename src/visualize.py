import matplotlib.pyplot as plt
import numpy as np


def plot_anomalies(series, errors, threshold, window_size):
    """
    Plot time series with detected anomalies.
    """
    anomaly_indices = np.where(errors > threshold)[0] + window_size

    plt.figure(figsize=(14, 5))
    plt.plot(series, label="Signal")
    plt.scatter(
        anomaly_indices,
        series[anomaly_indices],
        color="red",
        label="Anomaly",
        s=15
    )

    plt.axhline(y=threshold, color="orange", linestyle="--", label="Threshold")
    plt.title("Time-Series Anomaly Detection (LSTM Autoencoder)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Dummy test
    x = np.sin(np.linspace(0, 50, 500))
    errors = np.random.rand(500)
    threshold = 0.95

    plot_anomalies(x, errors, threshold, window_size=10)
