# simple_plot.py　　装飾のない一番シンプルな時系列グラフ
# matplotlibがインストールされていないときは、pip install matplotlib をターミナルで実行する。
# mu-editorで動かすときは、右下の歯車／Third Party Packagesで、matplotlibと入力、エンター。



import datetime as dt
import matplotlib.pyplot as plt

date_values = (
    ("2012-2-29", 0),
    ("2013-1-31", 20000),
    ("2014-6-11", 30000),
    ("2015-2-18", 50000),
    ("2015-10-13", 70000),
    ("2016-2-29", 80000),
    ("2016-9-8", 100000),
    ("2016-11-25", 130000),
    ("2017-3-14", 150000),
    ("2019-11-14", 170000),
    ("2020-1-21", 200000),
    ("2021-5-12", 230000),
    )

dates, values = zip(*date_values)

x = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]
y = [int(v/10) for v in values]

plt.plot(x, y)
plt.show()







