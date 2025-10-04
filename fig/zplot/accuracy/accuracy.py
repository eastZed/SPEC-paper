import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x_values = [60, 45, 30, 15, 0]
opt_67b_openbookqa = {
    'Full Cache': [44, 44, 44, 44, 44],
    'Quantization': [44, 42, 40, 36, 28],
    'H2O': [44, 42, 38, 36, 28],
    'InfiniGen': [44, 43, 42, 40, 39]
}

opt_67b_winogrande = {
    'Full Cache': [70, 70, 70, 70, 70],
    'Quantization': [70, 68, 66, 62, 55],
    'H2O': [70, 68, 66, 60, 55],
    'InfiniGen': [70, 69, 68, 65, 64]
}

opt_13b_openbookqa = {
    'Full Cache': [46, 46, 46, 46, 46],
    'Quantization': [46, 44, 40, 38, 32],
    'H2O': [46, 44, 38, 36, 32],
    'InfiniGen': [46, 44, 42, 41, 40]
}

opt_13b_winogrande = {
    'Full Cache': [75, 75, 75, 75, 75],
    'Quantization': [75, 73, 70, 65, 60],
    'H2O': [75, 73, 68, 63, 60],
    'InfiniGen': [75, 74, 73, 71, 70]
}

opt_30b_openbookqa = {
    'Full Cache': [50, 50, 50, 50, 50],
    'Quantization': [50, 48, 45, 42, 35],
    'H2O': [50, 48, 43, 40, 35],
    'InfiniGen': [50, 49, 46, 44, 42]
}

opt_30b_winogrande = {
    'Full Cache': [80, 80, 80, 80, 80],
    'Quantization': [80, 77, 75, 70, 62],
    'H2O': [80, 77, 72, 68, 62],
    'InfiniGen': [80, 78, 77, 75, 73]
}

# Colors and markers
colors = {'Full Cache': 'black', 'Quantization': 'grey', 'H2O': 'blue', 'InfiniGen': 'orange'}
markers = {'Full Cache': None, 'Quantization': '^', 'H2O': 's', 'InfiniGen': 'D'}
linestyles = {'Full Cache': '-', 'Quantization': '-', 'H2O': '-', 'InfiniGen': '-'}

# Create a figure and axis grid
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# List of all datasets
datasets = [
    (opt_67b_openbookqa, opt_67b_winogrande),
    (opt_13b_openbookqa, opt_13b_winogrande),
    (opt_30b_openbookqa, opt_30b_winogrande)
]

# Titles for the subplots
titles = ['OPT-6.7B', 'OPT-13B', 'OPT-30B']

# Plot each dataset in its respective subplot
for i, (openbookqa_data, winogrande_data) in enumerate(datasets):
    ax1 = axs[0, i]
    ax2 = axs[1, i]
    
    # Plot for OpenBookQA (Top row)
    for label, y_values in openbookqa_data.items():
        ax1.plot(x_values, y_values, color=colors[label], marker=markers[label], linestyle=linestyles[label], label=label)
    ax1.set_title(titles[i])
    ax1.set_ylim(20, 52)
    ax1.set_ylabel('OpenBookQA')
    ax1.set_xticks(x_values)

    # Plot for WinoGrande (Bottom row)
    for label, y_values in winogrande_data.items():
        ax2.plot(x_values, y_values, color=colors[label], marker=markers[label], linestyle=linestyles[label], label=label)
    ax2.set_ylim(45, 85)
    ax2.set_ylabel('WinoGrande')
    ax2.set_xticks(x_values)

# Add the legend in the first plot only
axs[0, 0].legend(loc='best')

# Show plot
plt.tight_layout()
plt.show()
