#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import pandas as pd
import matplotlib.style
import matplotlib.pyplot as plt


def draw(data):
    ts = pd.Series(data)
    ax = ts.plot()
    ax.set_xlabel('Time')
    ax.set_ylabel('Power/Temperature')
    plt.gcf().autofmt_xdate()


def render_image(name, s, u, t):
    draw(s)
    draw(u)
    draw(t)
    plt.savefig(name+'.png', dpi=200, bbox_inches='tight')
    plt.clf()


if __name__ == '__main__':
    matplotlib.style.use('ggplot')
    plt.clf()
    ns, nu, nt, cs, cu, ct, ss, su, st, es, eu, et = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
    with open('p2Aans.tsv') as fp:
        header = True
        for line in fp:
            if header:
                header = False
                continue
            cols = line.split('\t')
            d = datetime.datetime.strptime(cols[0], '%Y-%m-%d').date()
            ns[d] = float(cols[1])
            nu[d] = float(cols[2])
            cs[d] = float(cols[3])
            cu[d] = float(cols[4])
            ss[d] = float(cols[5])
            su[d] = float(cols[6])
            es[d] = float(cols[7])
            eu[d] = float(cols[8])
    with open('p2Cans.tsv') as fp:
        header = True
        for line in fp:
            if header:
                header = False
                continue
            cols = line.split('\t')
            d = datetime.datetime.strptime(cols[0], '%Y-%m-%d').date()
            nt[d] = float(cols[1])
            ct[d] = float(cols[2])
            st[d] = float(cols[3])
            et[d] = float(cols[4])
    render_image('p3north', ns, nu, nt)
    render_image('p3center', cs, cu, ct)
    render_image('p3south', ss, su, st)
    render_image('p3east', es, eu, et)
