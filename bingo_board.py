import matplotlib.pyplot as plt
import random


def make_one_board(fig_name, fig_num=1):
    bingo = 'BINGO'
    kwargs = dict(xycoords='axes fraction', ha='center', va='center',size=20)
    fig = plt.figure(fig_num, (6.5, 5.0))
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
            ax.annotate(bingo[col], color='C0', xy=(0.5, 1.5), **kwargs)
        index = random.randint(0, len(vals[col])-1)
        val = vals[col].pop(index)
        if row == 2 and col == 2:
            ax.annotate('FREE', color='C1', xy=(0.5, 0.5), **kwargs)
        else:
            ax.annotate('%i' % val, xy=(0.5, 0.5), **kwargs)

        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.tick_params(which='both', length=0.)
    plt.subplots_adjust(left=0.05, right=0.95,bottom=0.05)
    fig.savefig(fig_name)
    plt.close(fig)


if __name__ == '__main__':
    make_one_board('default')
    # for card in range(100):
    #     make_one_board('card_%i.pdf' % card, card+1)