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
    mydata = pd.read_csv("data/15819013_irisawa.csv", index_col=0, skiprows=[21, 22])
    avedata = pd.read_csv("data/average.csv", index_col=0)

    labels = mydata.columns

    fig = plt.figure(figsize=(35, 30))
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)

    rows = 5
    cols = 4
    gs = gridspec.GridSpec(nrows=rows, ncols=cols, figure=fig)

    for index in mydata.index.values:
        mydata_row = mydata.loc[index]
        avedata_row = avedata.loc[index]

        row = (index-1) // cols
        col = (index-1) % cols

        ax = fig.add_subplot(gs[row, col], polar=True)
        ax.set_rgrids([-2.0, -1.0, 0, 1.0, 2.0])

        ax = plot_polar(angles, ax, mydata_row, "自分のデータ")
        ax = plot_polar(angles, ax, avedata_row, "平均のデータ")
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)  # 軸ラベル
        ax.set_rlim(-2.0, 2.0)
        ax.set_title(f'音源{index}')
    plt.legend(bbox_to_anchor=(0.1, 0.1))

    imgname = f'./output/rador_chart.png'
    fig.savefig(imgname)
    plt.close(fig)

if __name__ == "__main__":
    main()