import matplotlib.pyplot as plt
import numpy as np

labels = ["Baseline", "1", "2", "3", "6"]
errors = [
    28.324269061254807,
    11.736425999696008,
    19.40157399074767,
    13.685401765218774,
    23.05944581360584,
]
correls = [
    43.3310515983105,
    31.837598299090153,
    13.136981288100296,
    9.11159442742151,
    8.121017428582753,
]

x = np.arange(len(labels))
width = 0.35

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

colors_e = ["#d9534f" if l == "Baseline" else "#5b9bd5" for l in labels]
colors_c = ["#d9534f" if l == "Baseline" else "#70ad47" for l in labels]

# --- Errors ---
bars1 = axes[0].bar(x, errors, color=colors_e, edgecolor="white", linewidth=0.8)
axes[0].set_title(r"$\Lambda$ Score")
axes[0].set_xticks(x)
axes[0].set_xticklabels(labels)
axes[0].set_xlabel("# of fake stations")
axes[0].set_ylabel("Score")
axes[0].bar_label(bars1, fmt="%.1f", padding=3, fontsize=9)
axes[0].set_ylim(0, max(errors) * 1.18)
axes[0].axhline(
    errors[0], color="#d9534f", linestyle="--", linewidth=1, alpha=0.5, label="Baseline"
)
axes[0].legend(fontsize=8)
axes[0].spines[["top", "right"]].set_visible(False)

# --- Correlations ---
bars2 = axes[1].bar(x, correls, color=colors_c, edgecolor="white", linewidth=0.8)
axes[1].set_title(r"$\Gamma$ Score")
axes[1].set_xticks(x)
axes[1].set_xticklabels(labels)
axes[1].set_xlabel("# of fake stations")
axes[1].set_ylabel("Score")
axes[1].bar_label(bars2, fmt="%.1f", padding=3, fontsize=9)
axes[1].set_ylim(0, max(correls) * 1.18)
axes[1].axhline(
    correls[0],
    color="#d9534f",
    linestyle="--",
    linewidth=1,
    alpha=0.5,
    label="Baseline",
)
axes[1].legend(fontsize=8)
axes[1].spines[["top", "right"]].set_visible(False)

plt.tight_layout()

plt.savefig("./output/assignment3/10_results.png", dpi=300)
