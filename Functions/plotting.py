import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

## line plotting (tested)
def plot_series(x, y, title, xlabel, ylabel, color="blue", label=None, grid=True):
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, color=color, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if label:
        plt.legend()
    if grid:
        plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_scatter(
    x, y,
    title, xlabel, ylabel,
    color="blue", label=None,
    grid=True, size=50,
    show_regression=False, reg_color="red", reg_label="Regression Line"
):
    """
    Plots a scatter plot from two datasets, with an optional regression line.

    Parameters:
    - x, y: Lists, arrays, or pandas Series of the same length.
    - title: Plot title.
    - xlabel, ylabel: Axis labels.
    - color: Color of scatter points.
    - label: Label for scatter points (optional).
    - grid: Show grid (default True).
    - size: Marker size (default 50).
    - show_regression: If True, plots a linear regression line.
    - reg_color: Color of regression line.
    - reg_label: Label for regression line.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, color=color, label=label, s=size)

    if show_regression:
        # Convert to NumPy arrays
        x_np = np.array(x)
        y_np = np.array(y)

        # Calculate linear regression coefficients
        m, b = np.polyfit(x_np, y_np, 1)
        y_pred = m * x_np + b

        # Plot regression line
        plt.plot(x_np, y_pred, color=reg_color, label=reg_label)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if label or show_regression:
        plt.legend()
    if grid:
        plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_skewness(data, title="Skewness Plot", color="skyblue", bins=30, show_kde=True):
    """
    Plots a histogram with optional KDE line and displays skewness value.

    Parameters:
    - data: list, array, or pandas Series
    - title: plot title
    - color: color of histogram bars
    - bins: number of bins in histogram
    - show_kde: whether to overlay KDE line
    """
    plt.figure(figsize=(10, 5))
    
    sns.histplot(data, bins=bins, kde=show_kde, color=color, edgecolor="black")

    skew_val = stats.skew(data)
    skew_text = f"Skewness = {skew_val:.2f}"

    plt.title(f"{title}\n{skew_text}")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_boxplot(data, title="Box Plot", ylabel="Values", showfliers=True, color="lightblue"):
    """
    Plots a boxplot to visualize the IQR and detect outliers.

    Parameters:
    - data: list, array, or pandas Series
    - title: plot title
    - ylabel: label for the y-axis
    - showfliers: show outliers as points (default True)
    - color: box color
    """
    plt.figure(figsize=(6, 4))
    
    # Create the boxplot
    box = plt.boxplot(data, patch_artist=True, showfliers=showfliers, vert=True)
    
    # Style the box
    for patch in box['boxes']:
        patch.set(facecolor=color)

    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
from scipy.stats import norm

def plot_skewness1(data_list, labels=None, bins=50):
    """
    Plot skewness for multiple datasets with histogram, KDE, normal curve, and boxplot.

    Parameters:
    - data_list: list of arrays/lists (each is a dataset to plot)
    - labels: list of titles/labels for each subplot
    - bins: number of histogram bins
    """
    num_datasets = len(data_list)
    fig, axes = plt.subplots(1, num_datasets, figsize=(6 * num_datasets, 5))

    # If only one dataset, wrap axis in a list
    if num_datasets == 1:
        axes = [axes]

    for i, data in enumerate(data_list):
        ax = axes[i]

        # Plot histogram + KDE
        sns.histplot(data, bins=bins, kde=True, stat='density', ax=ax, color='navy')

        # Overlay normal distribution curve
        mu, sigma = np.mean(data), np.std(data)
        x = np.linspace(min(data), max(data), 1000)
        p = norm.pdf(x, mu, sigma)
        ax.plot(x, p, 'r', linewidth=2)

        # Add boxplot below
        ax_box = ax.inset_axes([0, -0.25, 1, 0.15])  # x, y, width, height
        sns.boxplot(data=data, orient='h', ax=ax_box, color='lightgray')
        ax_box.set_xticks([])
        ax_box.set_yticks([])
        ax_box.axis('off')

        # Title with skewness
        skew_val = skew(data)
        title = labels[i] if labels else f"Dataset {i+1}"
        ax.set_title(f"{title}\nSkewness = {skew_val:.2f}", fontsize=14)
        ax.set_xlabel('')
        ax.set_ylabel('')

    plt.tight_layout()
    plt.show()
