import matplotlib.pyplot as plt
import numpy as np

def main():
    # =========================
    # 1. 准备数据
    # =========================

    # x 轴刻度文本：不带百分号
    bins = ["0–20", "20–40", "40–60", "60–80", "80–100"]
    x = np.arange(len(bins))

    # PIQA
    piqa_opt_6_7b = [0.8691, 0.7048, 0.6116, 0.4791, 0.4757]
    piqa_opt_13b  = [0.8656, 0.6729, 0.5100, 0.4934, 0.4483]
    piqa_opt_30b  = [0.8697, 0.7011, 0.5995, 0.4926, 0.4909]

    # OpenBookQA
    obqa_opt_6_7b = [0.8459, 0.7358, 0.5912, 0.4991, 0.3936]
    obqa_opt_13b  = [0.8568, 0.7027, 0.5234, 0.4183, 0.4453]
    obqa_opt_30b  = [0.8402, 0.7045, 0.5935, 0.5215, 0.4623]

    # =========================
    # 2. 画两个子图并存成 PDF
    # =========================

    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0), sharey=True)
    ax1, ax2 = axes

    # ---- 左图：PIQA ----
    ax1.plot(x, piqa_opt_6_7b, marker="o", linestyle="-", label="OPT-6.7B")
    ax1.plot(x, piqa_opt_13b,  marker="s", linestyle="-", label="OPT-13B")
    ax1.plot(x, piqa_opt_30b,  marker="^", linestyle="-", label="OPT-30B")

    ax1.set_xticks(x)
    ax1.set_xticklabels(bins, rotation=0)
    ax1.set_xlabel("Importance percentile (%)")
    ax1.set_ylabel("Recall ratio (%)")
    ax1.set_ylim(0.0, 1.0)
    ax1.set_title("PIQA")
    ax1.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    # ---- 右图：OpenBookQA ----
    ax2.plot(x, obqa_opt_6_7b, marker="o", linestyle="-", label="OPT-6.7B")
    ax2.plot(x, obqa_opt_13b,  marker="s", linestyle="-", label="OPT-13B")
    ax2.plot(x, obqa_opt_30b,  marker="^", linestyle="-", label="OPT-30B")

    ax2.set_xticks(x)
    ax2.set_xticklabels(bins, rotation=0)
    ax2.set_xlabel("Importance percentile (%)")
    ax2.set_title("OpenBookQA")
    ax2.grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    # ===== 统一 y 轴范围和刻度，刻度显示为百分数整数 =====
    yticks = np.linspace(0.0, 1.0, 6)  # 0.0, 0.2, ..., 1.0
    yticklabels = [f"{int(v * 100)}" for v in yticks]  # "0","20",...,"100"

    for ax in axes:
        ax.set_ylim(0.0, 1.0)
        ax.set_yticks(yticks)
        ax.set_yticklabels(yticklabels)

    # ===== 轴线和刻度位置美化（保留四个边框）=====

    # 左图：左侧显示 y 刻度
    ax1.tick_params(axis="y", labelleft=True, labelright=False)
    # 右图：右侧显示 y 刻度
    ax2.tick_params(axis="y", labelleft=False, labelright=True)
    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")
    ax2.set_ylabel("Recall ratio (%)")

    # 不再关闭任何 spine，这样左右子图四条边框都在
    # ax1.spines["right"].set_visible(False)
    # ax2.spines["left"].set_visible(False)

    # 统一图例（放在顶部中间）
    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3, frameon=False)

    # 调整布局，给上方图例留空间
    plt.tight_layout(rect=[0, 0, 1, 0.90])

    # 保存为 PDF
    plt.savefig("importance_transition_two_datasets.pdf", bbox_inches="tight")

    plt.show()


if __name__ == "__main__":
    main()
