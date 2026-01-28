import numpy as np


def reconstruction_error(original, reconstructed):
    """
    Compute reconstruction error (MSE per window).
    """
    return np.mean(np.square(original - reconstructed), axis=(1, 2))


def select_threshold(errors, factor=3.0):
    """
    Threshold = mean + factor * std
    """
    mean = np.mean(errors)
    std = np.std(errors)
    return mean + factor * std


def detect_anomalies(errors, threshold):
    """
    Return binary anomaly labels.
    """
    return (errors > threshold).astype(int)


if __name__ == "__main__":
    # Smoke test
    dummy_errors = np.random.normal(0, 1, 1000)
    threshold = select_threshold(dummy_errors)

    labels = detect_anomalies(dummy_errors, threshold)

    print("Threshold:", threshold)
    print("Anomalies detected:", labels.sum())
