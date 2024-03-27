import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Baseline', 'MAP']
on_chain_costs = [1240, 880]
off_chain_costs = [21, 15.7]
w = 0.1
y_pos = (w/4,w*1.7)
x = np.arange(len(labels))  # the label locations

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(8, 5))  # 1 row, 2 columns
# Bar chart for on-chain costs
axs[0].bar(y_pos, on_chain_costs, color=['tab:red', 'tab:blue'],width=w,align='center')
axs[0].set_xlabel('On-chain Costs', labelpad=15)  # title moved under the plot
axs[0].set_ylabel('Gas (k)')
axs[0].set_xticks(y_pos)
axs[0].set_xticklabels(labels)

# Bar chart for off-chain costs
axs[1].bar(y_pos, off_chain_costs, color=['tab:orange', 'tab:green'],width=w,align='center')
axs[1].set_xlabel('Off-chain costs', labelpad=15)  # title moved under the plot
axs[1].set_ylabel('Gates of Circuits (M)')
axs[1].set_xticks(y_pos)
axs[1].set_xticklabels(labels)


# Show the figure
plt.tight_layout()
plt.show()

# Save the figure as a PDF
plt.savefig('costs.pdf', format='pdf')