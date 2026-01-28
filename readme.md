# Anomaly Detection Benchmark (Lightweight)

This project implements a simple, reproducible benchmark for  
**unsupervised anomaly detection on network traffic features**.

The focus is on **engineering clarity and fair comparison**, not state-of-the-art research.

---

## Overview

The pipeline detects anomalous network flows using **reconstruction error–based methods**
and compares how different **unsupervised models and thresholding strategies**
affect sensitivity and false positives.

Key questions addressed:
- How do unsupervised models assign anomaly scores?
- How does threshold selection affect sensitivity and false positives?
- How do linear (PCA) and non-linear (Autoencoder) methods compare?
- How interpretable are simple reconstruction-based approaches?

---

## Feature Source

Input features are **flow-level network traffic statistics**, generated using a separate  
**Network Traffic Feature Engineering** pipeline.

Only **numeric features** are used for modeling.

---

## Pipeline

1. Load flow-level features  
2. Select numeric columns and clean missing values  
3. Standardize features (`StandardScaler`)  
4. Train unsupervised models  
5. Compute reconstruction error as anomaly score  
6. Apply thresholding methods  
7. Aggregate and compare results  
8. Save anomaly scores and flags  

---

## Models

- **PCA (Baseline)**
  - Linear dimensionality reduction
  - Reconstruction error used as anomaly score
  - Highly interpretable and computationally efficient

- **Autoencoder (TensorFlow)**
  - Fully connected neural network
  - Learns non-linear feature representations
  - Reconstruction error used as anomaly score

Both models produce **comparable anomaly scores**, enabling a fair benchmark.

---

## Thresholding Methods

- **Mean + k·Std**
  - Simple and interpretable
  - Sensitive to distribution shape and outliers

- **Percentile-based**
  - Predictable anomaly rate
  - No distributional assumptions
  - Often more stable for skewed scores

The **same thresholding logic** is applied to all models.

---

## Outputs

The final output is a single CSV file containing **side-by-side results**:

- PCA reconstruction error
- PCA anomaly flags (mean+std, percentile)
- Autoencoder reconstruction error
- Autoencoder anomaly flags (mean+std, percentile)

Saved at:data/processed/anomaly_results.csv


---

## PCA vs Autoencoder Comparison

Both models use **reconstruction error** as the anomaly score, but differ in behavior:

- PCA produces smoother, more stable error distributions
- Autoencoders capture non-linear structure but may flag more anomalies
- Threshold choice often impacts results more than model choice itself

This benchmark highlights how **engineering decisions**
(thresholding, scaling, aggregation) can dominate outcomes.

---

## Key Takeaways

- Threshold choice often has a **larger impact than the model itself**
- Percentile thresholds are more robust under skewed distributions
- Simple baselines like PCA remain strong references
- Autoencoders provide flexibility but require careful calibration

---

## How to Run

From project root:

```bash
# Train PCA and save reconstruction error
python -m src.pca_model

# Train Autoencoder and save reconstruction error
python -m src.autoencoder_model

# Aggregate results and apply thresholds
python -m src.save_results


---

## Notes

This project is intentionally lightweight and modular, designed as a foundation
for extending to:

Isolation Forest

Time-windowed analysis

Time-series anomaly detection

Streaming or online detection pipelines


