import pytest
import pandas as pd
import numpy as np

def test_chronological_data_split():
    """Ensures training data strictly precedes testing data (No Leakage)."""
    # Create mock time-series data
    dates = pd.date_range(start="2026-01-01", periods=100, freq="h")
    df = pd.DataFrame({'value': np.random.randn(100)}, index=dates)
    
    # Simulate a chronological 80/20 split
    split_idx = int(len(df) * 0.8)
    train_data = df.iloc[:split_idx]
    test_data = df.iloc[split_idx:]
    
    # The absolute maximum date in train MUST be strictly less than the minimum date in test
    assert train_data.index.max() < test_data.index.min(), "CRITICAL: Data Leakage detected. Train data overlaps with future Test data!"
    assert len(train_data) + len(test_data) == len(df), "Data split dropped rows."
