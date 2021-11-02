import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def plot_polar(angles, ax, values, label):
    values = np.concatenate((values, [values[0]]))  # 閉じた多角形にする
    ax.plot(angles, values, 'o-', label=label)  # 外枠
    ax.fill(angles, values, alpha=0.25)  # 塗りつぶし

    return ax

def main():
    data = pd.read_csv("data/15819013_irisawa.csv", index_col=0, skiprows=[21, 22])
    data2 = pd.read_csv("data/15819013_irisawa.csv", index_col=0, skiprows=20)

    labels = data.columns

    fig = plt.figure(figsize=(8.5, 6.5))
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)

    gs = gridspec.GridSpec(nrows=1, ncols=2, figure=fig)

    for col,index in enumerate(data2.index.values):
        x1 = data.loc[index]
        x2 = data2.loc[index]

        ax = fig.add_subplot(gs[0, col], polar=True)
        ax.set_rgrids([-2.0, -1.0, 0, 1.0, 2.0])

        ax = plot_polar(angles, ax, x1, "1回目")
        ax = plot_polar(angles, ax, x2, "2回目")
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)  # 軸ラベル
        ax.set_rlim(-2.0, 2.0)
        ax.set_title(f'音源{index}')
    plt.legend(bbox_to_anchor=(0.1, 0.1))

    imgname = f'./output/rador_chart_stability.png'
    fig.savefig(imgname)
    plt.close(fig)


if __name__ == "__main__":
    main()