import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, RepeatVector, TimeDistributed, Dense
from tensorflow.keras.optimizers import Adam


def build_lstm_autoencoder(window_size, n_features=1, latent_dim=32):
    """
    Build an LSTM Autoencoder model.
    """
    inputs = Input(shape=(window_size, n_features))

    # Encoder
    encoded = LSTM(latent_dim, activation="tanh", return_sequences=False)(inputs)

    # Bottleneck
    repeated = RepeatVector(window_size)(encoded)

    # Decoder
    decoded = LSTM(latent_dim, activation="tanh", return_sequences=True)(repeated)
    outputs = TimeDistributed(Dense(n_features))(decoded)

    model = Model(inputs, outputs)
    model.compile(optimizer=Adam(learning_rate=0.001), loss="mse")

    return model


if __name__ == "__main__":
    # Smoke test
    model = build_lstm_autoencoder(window_size=60)
    model.summary()
