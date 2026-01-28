# Anomaly Detection Benchmark (Lightweight)

🔹 Overview

Detect anomalous network flows using reconstruction error

Compare linear (PCA) vs non-linear (Autoencoder) methods

Evaluate thresholding strategies and their effect on sensitivity & false positives

Input: flow-level numeric features from the Network Traffic Feature Engineering pipeline

🛠️ Pipeline

Load flow-level features

Clean and standardize numeric columns

Train unsupervised models (PCA / Autoencoder)

Compute reconstruction errors → anomaly scores

Apply thresholds:

Mean + k·Std

Percentile-based

Aggregate and save results

Output: data/processed/anomaly_results.csv
Contains PCA & Autoencoder reconstruction errors and anomaly flags for both thresholds.

🔹 Models

PCA

Linear dimensionality reduction

Interpretable, fast

Reconstruction error → anomaly score

Autoencoder (TensorFlow)

Non-linear feature representations

Flexible but needs calibration

Reconstruction error → anomaly score

🔹 Thresholding

Mean + k·Std: Simple, interpretable

Percentile-based: Stable for skewed distributions

Threshold choice often matters more than model choice.

🔹 Key Takeaways

Thresholding impacts results more than model

Percentile thresholds are robust under skewed distributions

PCA is a strong baseline

Autoencoders provide flexibility


