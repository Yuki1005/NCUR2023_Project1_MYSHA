import networkx as nx
from networkx.readwrite import json_graph
import json
import pylab
import matplotlib.pyplot as plt

#　辺を設定する．
G = nx.read_weighted_edgelist("dijkstra.txt",create_using=nx.DiGraph)     #有向グラフ
G1 = nx.read_weighted_edgelist("dijkstra.txt",create_using=nx.Graph)      #無向グラフ


#　座標を設定する．indexがid，代入している値が座標．
pos={}
pos["A"]=(0,0)
pos["B"]=(210,0)
pos["C"]=(630,0)
pos["D"]=(910,0)
pos["E"]=(1075,0)
pos["F"]=(1385,0)
pos["G"]=(1465,0)
pos["H"]=(1615,0)
pos["I"]=(1605,-184)
pos["J"]=(1465,-184)
pos["K"]=(1385,-184)
pos["L"]=(1075,-184)
pos["M"]=(615,-184)
pos["N"]=(335,-184)
pos["O"]=(-365,0)
pos["P"]=(-705,0)
pos["Q"]=(-1185,0)
pos["R"]=(-1665,0)
pos["S"]=(-1185,-184)
pos["T"]=(-765,-184)
pos["U"]=(-705,-184)
pos["V"]=(-190,-184)
pos["W"]=(110,-184)
pos["X"]=(-1185,-394)
pos["Y"]=(-1185,-503)
pos["Z"]=(-945,-394)
pos["AA"]=(-945,-503)
pos["AB"]=(-705,-394)
pos["AC"]=(-705,-503)
pos["AD"]=(-535,-394)
pos["AE"]=(-535,-503)
pos["AF"]=(-365,-394)
pos["AG"]=(-365,-503)
pos["AH"]=(210,-503)
pos["AI"]=(560,-503)
pos["AJ"]=(910,-503)
pos["AK"]=(910,-394)
pos["AL"]=(1075,-394)
pos["AM"]=(1075,-503)
pos["AN"]=(1315,-394)
pos["AO"]=(1315,-503)
pos["AP"]=(1615,-503)
pos["AQ"]=(560,-394)
pos["D1"]=(-1480,197)
pos["D2"]=(-1200,197)
pos["D3"]=(-920,197)
pos["D4"]=(-640,197)
pos["D5"]=(-360,197)
pos["D6"]=(-80,197)
pos["D7"]=(200,197)
pos["D8"]=(480,197)
pos["D9"]=(760,197)
pos["D10"]=(1040,197)
pos["D11"]=(1320,197)
pos["D12"]=(1600,197)
pos["I53"]=(-1600,-700)
pos["I54"]=(-960,-700)
pos["I55"]=(-320,-700)
pos["I56"]=(320,-700)
pos["I57"]=(960,-700)
pos["I58"]=(1600,-700)


#　行先指定
aaa = input("スタート地点を入力")
bbb = input("行き先を入力")
aaa = str.upper(aaa)
bbb = str.upper(bbb)
if aaa == bbb:
    bbb = input("スタート地点とは違う、行き先を入力")
    bbb = str.upper(bbb)

##　重み表示    
#edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
#print(nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels))

##　グラフオブジェクト（点と辺）に座標を関連付けて描画
a = nx.dijkstra_path(G,aaa,bbb)
print(f'スタート地点({aaa})から目的地({bbb})までの最短経路:\n',nx.dijkstra_path(G,aaa,bbb))
print(f'スタート地点({aaa})から目的地({bbb})までの最短距離(m):\n', nx.dijkstra_path_length(G,aaa,bbb),"m [メートル]")

##　重みの色を変更
sp_edges = [(a[i],a[i+1]) for i in range(len(a)-1)]
edge_color_list = ["grey"]*len(G.edges)
#replace the color in edge_color_list with red if the edge belongs to the shortest path:
for i, edge in enumerate(G.edges()):
    if edge in sp_edges or (edge[1],edge[0]) in sp_edges:
        edge_color_list[i] = 'crimson'

##　ノードの色を変更
color_map = []
for i in G:
    if i == nx.dijkstra_path(G,aaa,bbb)[len(nx.dijkstra_path(G,aaa,bbb))-1]:
        color_map.append('crimson')
    elif i == nx.dijkstra_path(G,aaa,bbb)[0]:
        color_map.append('crimson')
    else: color_map.append('skyblue')   

nx.draw_networkx(G,pos,edge_color=edge_color_list,node_color= color_map)     #座標あり
#nx.draw_networkx(G)        #座標なし
plt.show()

# 平均kts(knot)を測る。1kts = 0.51477m/s
# 距離データをもう一度見直し
# 待ち行列プログラム
# #1をもとに各ゲートから離陸地点までの平均到達時間を予想、算出