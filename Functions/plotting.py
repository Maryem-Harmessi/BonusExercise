import matplotlib.pyplot as plt


## line plotting (tested)
def plot_series(x, y, title, xlabel, ylabel, color="blue", label=None, grid=True):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color=color, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if label:
        plt.legend()
    if grid:
        plt.grid(True)
    plt.tight_layout()
    plt.show()


