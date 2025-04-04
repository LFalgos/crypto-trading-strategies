"""
Sample Crypto Trading Strategy using pandas and technical indicators
"""
import pandas as pd
import numpy as np

def bollinger_bands(data, window=20):
    sma = data['close'].rolling(window).mean()
    std = data['close'].rolling(window).std()
    data['upper'] = sma + (2 * std)
    data['lower'] = sma - (2 * std)
    return data

# Example usage with sample DataFrame
# df = pd.read_csv("your_data.csv")
# df = bollinger_bands(df)
