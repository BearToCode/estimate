import matplotlib.pyplot as plt
import numpy as np

labels = ["R RMS", "S RMS", "W RMS", "Position RMS"]
standard = [148.844, 357.233, 14.838, 387.285]
no_bad = [33.516, 108.945, 11.978, 114.612]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 4))
bars1 = ax.bar(
    x - width / 2, standard, width, label="Standard (all passes)", color="steelblue"
)
bars2 = ax.bar(x + width / 2, no_bad, width, label="No bad passes", color="coral")

ax.set_ylabel("RMS [km]")
ax.set_title("RSW Orbit Difference RMS: Estimated vs TLE (per pass arcs)")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.7)

for bar in bars1:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 5,
        f"{bar.get_height():.1f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )
for bar in bars2:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 5,
        f"{bar.get_height():.1f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )

fig.tight_layout()
fig.savefig(f"./output/residuals_comparison_per_pass.png", dpi=300)

standard = [22.791, 115.084, 25.988, 120.163]
no_bad = [23.652, 124.987, 13.401, 127.909]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 4))
bars1 = ax.bar(
    x - width / 2, standard, width, label="Standard (all passes)", color="steelblue"
)
bars2 = ax.bar(x + width / 2, no_bad, width, label="No bad passes", color="coral")

ax.set_ylabel("RMS [km]")
ax.set_title("RSW Orbit Difference RMS: Estimated vs TLE (per day arcs)")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.7)

for bar in bars1:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{bar.get_height():.1f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )
for bar in bars2:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{bar.get_height():.1f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )

fig.tight_layout()
fig.savefig(f"./output/residuals_comparison_per_day.png", dpi=300)

plt.show()
