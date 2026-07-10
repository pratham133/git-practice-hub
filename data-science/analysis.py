"""Exploratory analysis helpers. Each challenge issue asks you to implement ONE function below."""

import pandas as pd

def load_data(path="dataset.csv"):
    return pd.read_csv(path)


def total_by_category(df):
    """TODO: return total `amount` grouped by `category` (see issue)."""
    raise NotImplementedError


def plot_by_region(df):
    """TODO: create a bar chart of total amount by region (see issue)."""
    raise NotImplementedError

def filter_by_region(df, region):
    return df[df["region"] == region]
