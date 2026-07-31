from get_data_selection import get_filepath_list
import json
from collections import Counter

filepaths = get_filepath_list('../data/json_per_doc_class_IO')
#print(filepaths)

all_labels = []
for filepath in filepaths:
    #print(filepath)
    with open(filepath, 'r') as f:
        for line in f:
            doc = json.loads(line)
            labels = doc['events']

            for label in labels:
                if label != 'None':
                    all_labels.append(label)




counted = Counter(all_labels)
print(counted)
print()
print(len(list(counted.keys())))
print()

frequencies = list(counted.values())[1:] # take out None class
frequencies.sort()
print(frequencies)

import matplotlib.pyplot as plt
import numpy as np

def plot_label_distribution(label_counts: dict,
                             outfile: str,
                             title: str = "Label Distribution",
                             figsize: tuple = (14, 8),
                             exclude_labels: list = None,
                             log_scale: bool = True,
                             annotate_top: int = 5,
                             annotate_bottom: int = 10):
    if exclude_labels:
        label_counts = {k: v for k, v in label_counts.items() if k not in exclude_labels}

    sorted_items = sorted(label_counts.items(), key=lambda x: x[1], reverse=True)
    labels, counts = zip(*sorted_items)
    n = len(labels)

    fig, ax = plt.subplots(figsize=figsize)
    colors = plt.cm.viridis(np.linspace(0.1, 0.9, n))
    bars = ax.bar(range(n), counts, color=colors, edgecolor='white', linewidth=0.5)

    ax.set_xticks(range(n))
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)

    if log_scale:
        ax.set_yscale('log')
        ax.set_ylabel("Count (log scale)", fontsize=11)
    else:
        ax.set_ylabel("Count", fontsize=11)

    ax.set_title(title, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel("Label", fontsize=11)

    # Annotate top N and bottom N bars
    annotate_indices = set(range(annotate_top)) | set(range(n - annotate_bottom, n))
    for i, (bar, count) in enumerate(zip(bars, counts)):
        if i in annotate_indices:
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + max(counts) * 0.005,
                    str(count),
                    ha='center', va='bottom', fontsize=7.5, fontweight='bold')

    ax.yaxis.grid(True, linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)
    plt.tight_layout()
    plt.savefig(outfile, dpi=1000)
    plt.show()

# --- Usage ---
label_counts = dict(counted)
# With the dominant 'O' class
plot_label_distribution(label_counts, title="Full Label Distribution", outfile='label_distr_fig1.png')

# Without 'O' to better see the minority classes
plot_label_distribution(label_counts, title="Label Distribution (excluding 'O')", exclude_labels=['O'], log_scale=False, outfile='label_distr_fig2.png')