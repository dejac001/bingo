import matplotlib.pyplot as plt
import random


def make_one_board(fig_name):
    bingo = 'BINGO'
    kwargs = dict(xycoords='axes fraction', ha='center', va='center',size=20)
    fig = plt.figure(1, (6.5, 5.0))
    vals = {
        0: list(range(1, 16)),
        1: list(range(16, 31)),
        2: list(range(31, 46)),
        3: list(range(46, 61)),
        4: list(range(61, 75))
    }
    for i in range(25):
        ax = fig.add_subplot(5, 5, i+1)
        col, row = i % 5, i // 5
        if row == 0:
            ax.annotate(bingo[col], xy=(0.5, 1.5), **kwargs)
        index = random.randint(0, len(vals[col])-1)
        val = vals[col].pop(index)
        if row == 2 and col == 2:
            ax.annotate('FREE', xy=(0.5, 0.5), **kwargs)
        else:
            ax.annotate('%i' % val, xy=(0.5, 0.5), **kwargs)


        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.tick_params(which='both', length=0.)
    plt.subplots_adjust(left=0.05, right=0.95,bottom=0.05)
    fig.savefig(fig_name)


if __name__ == '__main__':
    make_one_board('default')