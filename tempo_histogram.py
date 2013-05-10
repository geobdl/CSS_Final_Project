#!/usr/bin/env python3
"""Make a histogram of tempoes with 20 bins."""

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt, rc
import pandas as pd
import numpy as np


# Pick out the tempo information.
SUMMARY = pd.read_hdf('data/msd_summary_file.h5', 'analysis/songs')
SUMMARY = SUMMARY['tempo']
SUMMARY = SUMMARY.map(float)


def main():
    """Bin the data and plot it."""
    rc('text', usetex=True)
    rc('font', family='serif')
    plt.hist(SUMMARY, bins=20)
    plt.title('Distribution of Tempo')
    plt.xlabel('Tempo (beats per minute)')
    plt.ylabel('Count')
    plt.savefig('data/graphs/graph_tempo_histogram.png')

    print('Statistics on the Distribution:')
    print('\tcount: {}'.format(len(SUMMARY)))
    print('\tmean: {}'.format(np.mean(SUMMARY)))
    print('\tstd: {}'.format(np.std(SUMMARY)))
    print('\tmin: {}'.format(np.min(SUMMARY)))
    print('\t25%: {}'.format(np.percentile(SUMMARY, 0.25)))
    print('\t50%: {}'.format(np.percentile(SUMMARY, 0.5)))
    print('\t75%: {}'.format(np.percentile(SUMMARY, 0.75)))
    print('\tmax: {}'.format(np.max(SUMMARY)))


if __name__ == '__main__':
    main()
