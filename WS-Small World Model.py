import networkx as ne   #导入建网络模型包，命名ne
import matplotlib.pyplot as mp      #导入科学绘图包，命名mp

#WS network graphy
#watts_strogatz_graph(n, k, p)方法生成一个含有n个节点、每个节点有k个邻居、以概率p随机化重连边的WS小世界网络。
#在本程序中用该方法生成了一个含有34个节点，每个节点有5个邻居节点，以概率0.5随机化重连边的WS小世界网路。
ws = ne.watts_strogatz_graph(34,5,0.5)
ps = ne.circular_layout(ws)     #布置框架
ne.draw(ws,ps,with_labels = False,node_size = 30)
mp.show()