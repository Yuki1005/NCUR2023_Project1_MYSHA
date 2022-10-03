from __future__ import annotations
from typing import Tuple, List, Optional, Dict
from heapq import heappush, heappop

VertexStr = str

cc = "A"
dd = "A"
aaa = input("スタート地点を入力")
bbb = input("行き先を入力")
aaa = str.upper(aaa)
bbb = str.upper(bbb)
if aaa == bbb:
    aaa = input("スタート地点を入力")
    bbb = input("スタート地点とは違う、行き先を入力")
    aaa = str.upper(aaa)
    bbb = str.upper(bbb)


class Vertex:
    A: VertexStr = 'A'
    B: VertexStr = 'B'
    C: VertexStr = 'C'
    D: VertexStr = 'D'
    E: VertexStr = 'E'
    F: VertexStr = 'F'
    G: VertexStr = 'G'
    H: VertexStr = 'H'
    I: VertexStr = 'I'
    J: VertexStr = 'J'
    K: VertexStr = 'K'
    L: VertexStr = 'L'
    M: VertexStr = 'M'
    N: VertexStr = 'N'
    O: VertexStr = 'O'
    P: VertexStr = 'P'
    Q: VertexStr = 'Q'
    R: VertexStr = 'R'
    S: VertexStr = 'S'
    T: VertexStr = 'T'
    U: VertexStr = 'U'
    V: VertexStr = 'V'
    W: VertexStr = 'W'
    X: VertexStr = 'X'
    Y: VertexStr = 'Y'
    Z: VertexStr = 'Z'
    AA: VertexStr = 'AA'
    AB: VertexStr = 'AB'
    AC: VertexStr = 'AC'
    AD: VertexStr = 'AD'
    AE: VertexStr = 'AE'
    AF: VertexStr = 'AF'
    AG: VertexStr = 'AG'
    AH: VertexStr = 'AH'
    AI: VertexStr = 'AI'
    AJ: VertexStr = 'AJ'
    AK: VertexStr = 'AK'
    AL: VertexStr = 'AL'
    AM: VertexStr = 'AM'
    AN: VertexStr = 'AN'
    AO: VertexStr = 'AO'
    AP: VertexStr = 'AP'
    D1: VertexStr = 'D1'
    D2: VertexStr = 'D2'
    D3: VertexStr = 'D3'
    D4: VertexStr = 'D4'
    D5: VertexStr = 'D5'
    D6L: VertexStr = 'D6L'
    D6: VertexStr = 'D6'
    D6R: VertexStr = 'D6R'
    D7: VertexStr = 'D7'
    D8: VertexStr = 'D8'
    D9: VertexStr = 'D9'
    D10: VertexStr = 'D10'
    D11L: VertexStr = 'D11L'
    D11: VertexStr = 'D11'
    D11R: VertexStr = 'D11R'
    D12L: VertexStr = 'D12L'
    D12: VertexStr = 'D12'
    D12R: VertexStr = 'D12R'
    I53: VertexStr = 'I53'
    I54: VertexStr = 'I54'
    I55: VertexStr = 'I55'
    I56: VertexStr = 'I56'
    I57: VertexStr = 'I57'
    I58: VertexStr = 'I58'


class Edge:
    def __init__(
            self, from_idx: int, to_idx: int,
            from_vertex: VertexStr, to_vertex: VertexStr,
            weight: float) -> None:
        self.from_idx: int = from_idx
        self.to_idx: int = to_idx
        self.from_vertex: VertexStr = from_vertex
        self.to_vertex: VertexStr = to_vertex
        self.weight: float = weight

    def reversed(self) -> Edge:
        reversed_edge = Edge(
            from_idx=self.to_idx,
            to_idx=self.from_idx,
            from_vertex=self.from_vertex,
            to_vertex=self.to_vertex,
            weight=self.weight)
        return reversed_edge

    def __str__(self) -> str:
        edge_info_str: str = (
            f'from: {self.from_vertex}'
            f'(weight: {self.weight})'
            f' -> to: {self.to_vertex}'
        )
        return edge_info_str


class Graph:

    def __init__(self, vertices: List[VertexStr]) -> None:
        self._vertices: List[VertexStr] = vertices
        self._edges: List[List[Edge]] = []
        for _ in vertices:
            self._edges.append([])

    def vertex_at(self, index: int) -> VertexStr:
        return self._vertices[index]

    def index_of(self, vertex: VertexStr) -> int:
        return self._vertices.index(vertex)

    @property
    def vertex_count(self):
        return len(self._vertices)

    def edges_at(self, vertex_index: int) -> List[Edge]:
        return self._edges[vertex_index]

    def get_neighbor_vertices_and_weights_by_index(
            self, vertex_index: int) -> List[Tuple[VertexStr, float]]:
        neighbor_vertices_and_weights: List[Tuple[VertexStr, float]] = []
        for edge in self.edges_at(vertex_index=vertex_index):
            tuple_val = (
                self.vertex_at(index=edge.to_idx),
                edge.weight,
            )
            neighbor_vertices_and_weights.append(tuple_val)
        return neighbor_vertices_and_weights

    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.from_idx].append(edge)
        self._edges[edge.to_idx].append(edge.reversed())

    def add_edge_by_vertices(
            self, from_vertex: VertexStr,
            to_vertex: VertexStr,
            weight: float) -> None:
        from_idx = self._vertices.index(from_vertex)
        to_idx = self._vertices.index(to_vertex)
        edge = Edge(
            from_idx=from_idx,
            to_idx=to_idx,
            from_vertex=from_vertex,
            to_vertex=to_vertex,
            weight=weight)
        self.add_edge(edge=edge)

    def __str__(self) -> str:
        graph_info: str = ''
        for index in range(self.vertex_count):
            neighbors_data = self.get_neighbor_vertices_and_weights_by_index(
                vertex_index=index)
            graph_info += (
                f'対象の頂点 : {self.vertex_at(index=index)}'
                f' -> 隣接頂点データ : {neighbors_data}\n'
            )
        return graph_info


class DijkstraDistanceVertex:

    def __init__(self, vertex_idx: int, distance: float) -> None:
        self.vertex_idx = vertex_idx
        self.distance = distance

    def __lt__(self, other: DijkstraDistanceVertex) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DijkstraDistanceVertex) -> bool:
        return self.distance == other.distance


class PriorityQueue:

    def __init__(self) -> None:
        self._container: List[DijkstraDistanceVertex] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: DijkstraDistanceVertex) -> None:
        heappush(self._container, item)

    def pop(self) -> DijkstraDistanceVertex:
        return heappop(self._container)


def dijkstra(
        graph: Graph,
        root_vertex: VertexStr
        ) -> tuple[List[Optional[float]], Dict[int, Edge]]:
    first_idx: int = graph.index_of(vertex=root_vertex)
    distances: List[Optional[float]] = [
        None for _ in range(graph.vertex_count)]
    distances[first_idx] = 0

    path_dict: Dict[int, Edge] = {}
    priority_queue: PriorityQueue = PriorityQueue()
    priority_queue.push(
        item=DijkstraDistanceVertex(
            vertex_idx=first_idx,
            distance=0))

    while not priority_queue.empty:
        from_idx:int = priority_queue.pop().vertex_idx
        from_vertex_distance: float = distances[from_idx]
        for edge in graph.edges_at(vertex_index = from_idx):
            to_distance: Optional[float] = distances[edge.to_idx]
            current_route_distance: float = edge.weight + from_vertex_distance
            if (to_distance is not None
                    and to_distance <= current_route_distance):
                continue

            distances[edge.to_idx] = current_route_distance
            path_dict[edge.to_idx] = edge
            priority_queue.push(
                item=DijkstraDistanceVertex(
                    vertex_idx=edge.to_idx,
                    distance=current_route_distance))

    return distances, path_dict


RoutePath = List[Edge]


def to_route_path_from_path_dict(
        start_vertex_idx: int,
        last_vertex_idx: int,
        path_dict: Dict[int, Edge]) -> RoutePath:
    route_path: RoutePath = []
    current_edge: Edge = path_dict[last_vertex_idx]
    route_path.append(current_edge)
    while current_edge.from_idx != start_vertex_idx:
        current_edge = path_dict[current_edge.from_idx]
        route_path.append(current_edge)
    route_path.reverse()
    return route_path

if __name__ == '__main__':
    graph = Graph(
        vertices=[
            Vertex.A,
            Vertex.B,
            Vertex.C,
            Vertex.D,
            Vertex.E,
            Vertex.F,
            Vertex.G,
            Vertex.H,
            Vertex.I,
            Vertex.J,
            Vertex.K,
            Vertex.L,
            Vertex.M,
            Vertex.N,
            Vertex.O,
            Vertex.P,
            Vertex.Q,
            Vertex.R,
            Vertex.S,
            Vertex.T,
            Vertex.U,
            Vertex.V,
            Vertex.W,
            Vertex.X,
            Vertex.Y,
            Vertex.Z,
            Vertex.AA,
            Vertex.AB,
            Vertex.AC,
            Vertex.AD,
            Vertex.AE,
            Vertex.AF,
            Vertex.AG,
            Vertex.AH,
            Vertex.AI,
            Vertex.AJ,
            Vertex.AK,
            Vertex.AL,
            Vertex.AM,
            Vertex.AN,
            Vertex.AO,
            Vertex.AP,
            Vertex.D1,
            Vertex.D2,
            Vertex.D3,
            Vertex.D4,
            Vertex.D5,
            Vertex.D6,
            Vertex.D7,
            Vertex.D8,
            Vertex.D9,
            Vertex.D10,
            Vertex.D11,
            Vertex.D12,
            Vertex.I53,
            Vertex.I54,
            Vertex.I55,
            Vertex.I56,
            Vertex.I57,
            Vertex.I58
        ])
    
    
    
    graph.add_edge_by_vertices(
        from_vertex=Vertex.P,
        to_vertex=Vertex.U,
        weight=184)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AC,
        to_vertex=Vertex.AB,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.P,
        to_vertex=Vertex.AC,
        weight=503)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.Q,
        to_vertex=Vertex.S,
        weight=184)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.R,
        to_vertex=Vertex.S,
        weight=250)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.R,
        to_vertex=Vertex.Q,
        weight=148)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.Q,
        to_vertex=Vertex.T,
        weight=502)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.Q,
        to_vertex=Vertex.P,
        weight=480)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.Y,
        to_vertex=Vertex.X,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AA,
        to_vertex=Vertex.Y,
        weight=240)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AC,
        to_vertex=Vertex.AA,
        weight=240)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AA,
        to_vertex=Vertex.Z,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.B,
        to_vertex=Vertex.AH,
        weight=503)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.E,
        to_vertex=Vertex.AM,
        weight=503)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.E,
        to_vertex=Vertex.L,
        weight=184)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AM,
        to_vertex=Vertex.AL,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.P,
        to_vertex=Vertex.V,
        weight=550)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AB,
        to_vertex=Vertex.V,
        weight=570)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.P,
        to_vertex=Vertex.O,
        weight=340)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.O,
        to_vertex=Vertex.W,
        weight=515)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AF,
        to_vertex=Vertex.W,
        weight=515)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AE,
        to_vertex=Vertex.AD,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AE,
        to_vertex=Vertex.AC,
        weight=170)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AG,
        to_vertex=Vertex.AE,
        weight=170)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AG,
        to_vertex=Vertex.AF,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AG,
        to_vertex=Vertex.AH,
        weight=575)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.O,
        to_vertex=Vertex.A,
        weight=365)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.A,
        to_vertex=Vertex.B,
        weight=210)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.B,
        to_vertex=Vertex.C,
        weight=420)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.C,
        to_vertex=Vertex.D,
        weight=280)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.C,
        to_vertex=Vertex.N,
        weight=440)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D,
        to_vertex=Vertex.M,
        weight=440)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D,
        to_vertex=Vertex.E,
        weight=165)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.E,
        to_vertex=Vertex.F,
        weight=310)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.F,
        to_vertex=Vertex.K,
        weight=235)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.G,
        to_vertex=Vertex.J,
        weight=235)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.F,
        to_vertex=Vertex.G,
        weight=80)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.H,
        to_vertex=Vertex.I,
        weight=184)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.G,
        to_vertex=Vertex.H,
        weight=150)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AP,
        to_vertex=Vertex.I,
        weight=319)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AL,
        to_vertex=Vertex.M,
        weight=580)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AO,
        to_vertex=Vertex.AN,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AO,
        to_vertex=Vertex.AP,
        weight=300)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AM,
        to_vertex=Vertex.AO,
        weight=240)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AJ,
        to_vertex=Vertex.AM,
        weight=165)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AJ,
        to_vertex=Vertex.AK,
        weight=109)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AK,
        to_vertex=Vertex.N,
        weight=630)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AH,
        to_vertex=Vertex.AI,
        weight=350)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.AI,
        to_vertex=Vertex.AJ,
        weight=350)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D1,
        to_vertex=Vertex.A,
        weight=1620)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D1,
        to_vertex=Vertex.R,
        weight=347)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D2,
        to_vertex=Vertex.A,
        weight=1560)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D2,
        to_vertex=Vertex.R,
        weight=279)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D3,
        to_vertex=Vertex.A,
        weight=1515)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D3,
        to_vertex=Vertex.R,
        weight=235)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D4,
        to_vertex=Vertex.A,
        weight=1472)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D4,
        to_vertex=Vertex.R,
        weight=192)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D5,
        to_vertex=Vertex.A,
        weight=1429)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D5,
        to_vertex=Vertex.R,
        weight=235)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D6,
        to_vertex=Vertex.A,
        weight=1386)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D6,
        to_vertex=Vertex.R,
        weight=246)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D7,
        to_vertex=Vertex.A,
        weight=1314)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D7,
        to_vertex=Vertex.R,
        weight=320)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D8,
        to_vertex=Vertex.A,
        weight=1242)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D8,
        to_vertex=Vertex.R,
        weight=392)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D9,
        to_vertex=Vertex.A,
        weight=1059)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D9,
        to_vertex=Vertex.R,
        weight=578)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D10,
        to_vertex=Vertex.A,
        weight=986)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D10,
        to_vertex=Vertex.R,
        weight=650)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D11,
        to_vertex=Vertex.A,
        weight=902)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D11,
        to_vertex=Vertex.R,
        weight=733)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D12,
        to_vertex=Vertex.A,
        weight=816)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.D12,
        to_vertex=Vertex.R,
        weight=818)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I58,
        to_vertex=Vertex.AG,
        weight=890)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I57,
        to_vertex=Vertex.AG,
        weight=815)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I56,
        to_vertex=Vertex.AG,
        weight=740)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I55,
        to_vertex=Vertex.AG,
        weight=646)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I54,
        to_vertex=Vertex.AG,
        weight=570)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I53,
        to_vertex=Vertex.AG,
        weight=495)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I58,
        to_vertex=Vertex.AJ,
        weight=995)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I57,
        to_vertex=Vertex.AJ,
        weight=915)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I56,
        to_vertex=Vertex.AJ,
        weight=991)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I55,
        to_vertex=Vertex.AJ,
        weight=1095)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I54,
        to_vertex=Vertex.AJ,
        weight=1170)
    graph.add_edge_by_vertices(
        from_vertex=Vertex.I53,
        to_vertex=Vertex.AJ,
        weight=1245)
    
    if(aaa == ("A" or "a")):
        cc = Vertex.A
    elif(aaa == ("B" or "b")):
        cc = Vertex.B
    elif(aaa == ("C" or "c")):
        cc = Vertex.C
    elif(aaa == ("D" or "d")):
        cc = Vertex.D
    elif(aaa == ("E" or "e")):
        cc = Vertex.E
    elif(aaa == ("F" or "f")):
        cc = Vertex.F
    elif(aaa == ("G" or "g")):
        cc = Vertex.G
    elif(aaa == ("H" or "h")):
        cc = Vertex.H
    elif(aaa == ("I" or "i")):
        cc = Vertex.I
    elif(aaa == ("J" or "j")):
        cc = Vertex.J
    elif(aaa == ("K" or "k")):
        cc = Vertex.K
    elif(aaa == ("L" or "l")):
        cc = Vertex.L
    elif(aaa == ("M" or "m")):
        cc = Vertex.M
    elif(aaa == ("N" or "n")):
        cc = Vertex.N
    elif(aaa == ("O" or "o")):
        cc = Vertex.O
    elif(aaa == ("P" or "p")):
        cc = Vertex.P
    elif(aaa == ("Q" or "q")):
        cc = Vertex.Q
    elif(aaa == ("R" or "r")):
        cc = Vertex.R
    elif(aaa == ("S" or "s")):
        cc = Vertex.S
    elif(aaa == ("T" or "t")):
        cc = Vertex.T
    elif(aaa == ("U" or "u")):
        cc = Vertex.U
    elif(aaa == ("V" or "v")):
        cc = Vertex.V
    elif(aaa == ("W" or "w")):
        cc = Vertex.W
    elif(aaa == ("X" or "x")):
        cc = Vertex.X
    elif(aaa == ("Y" or "y")):
        cc = Vertex.Y
    elif(aaa == ("Z" or "z")):
        cc = Vertex.Z
    elif(aaa == ("AA" or "aa")):
        cc = Vertex.AA
    elif(aaa == ("AB" or "ab")):
        cc = Vertex.AB
    elif(aaa == ("AC" or "ac")):
        cc = Vertex.AC
    elif(aaa == ("AD" or "ad")):
        cc = Vertex.AD
    elif(aaa == ("AE" or "ae")):
        cc = Vertex.AE
    elif(aaa == ("AF" or "af")):
        cc = Vertex.AF
    elif(aaa == ("AG" or "ag")):
        cc = Vertex.AG
    elif(aaa == ("AH" or "ah")):
        cc = Vertex.AH
    elif(aaa == ("AI" or "ai")):
        cc = Vertex.AI
    elif(aaa == ("AJ" or "aj")):
        cc = Vertex.AJ
    elif(aaa == ("AK" or "ak")):
        cc = Vertex.AK
    elif(aaa == ("AL" or "al")):
        cc = Vertex.AL
    elif(aaa == ("AM" or "am")):
        cc = Vertex.AM
    elif(aaa == ("AN" or "an")):
        cc = Vertex.AN
    elif(aaa == ("AO" or "ao")):
        cc = Vertex.AO
    elif(aaa == ("AP" or "ap")):
        cc = Vertex.AP
    elif(aaa == ("D1" or "d1")):
        cc = Vertex.D1
    elif(aaa == ("D2" or "d2")):
        cc = Vertex.D2
    elif(aaa == ("D3" or "d3")):
        cc = Vertex.D3
    elif(aaa == ("D4" or "d4")):
        cc = Vertex.D4
    elif(aaa == ("D5" or "d5")):
        cc = Vertex.D5
    elif(aaa == ("D6L" or "d6l")):
        cc = Vertex.D6L
    elif(aaa == ("D6" or "d6")):
        cc = Vertex.D6
    elif(aaa == ("D6R" or "d6r")):
        cc = Vertex.D6R
    elif(aaa == ("D7" or "d7")):
        cc = Vertex.D7
    elif(aaa == ("D8" or "d8")):
        cc = Vertex.D8
    elif(aaa == ("D9" or "d9")):
        cc = Vertex.D9
    elif(aaa == ("D10" or "d10")):
        cc = Vertex.D10
    elif(aaa == ("D11L" or "d11l")):
        cc = Vertex.D11L
    elif(aaa == ("D11" or "d11")):
        cc = Vertex.D11
    elif(aaa == ("D11R" or "d11r")):
        cc = Vertex.D11R
    elif(aaa == ("D12L" or "d12l")):
        cc = Vertex.D12L
    elif(aaa == ("D12" or "d12")):
        cc = Vertex.D12
    elif(aaa == ("D12R" or "d12r")):
        cc = Vertex.D12R
    elif(aaa == ("I53" or "i53")):
        cc = Vertex.I53
    elif(aaa == ("I54" or "i54")):
        cc = Vertex.I54
    elif(aaa == ("I55" or "i55")):
        cc = Vertex.I55
    elif(aaa == ("I56" or "i56")):
        cc = Vertex.I56
    elif(aaa == ("I57" or "i57")):
        cc = Vertex.I57
    elif(aaa == ("I58" or "i58")):
        cc = Vertex.I58
    if(bbb== ("A" or "a")):
        dd = Vertex.A
    elif(bbb == ("B" or "b")):
        dd = Vertex.B
    elif(bbb == ("C" or "c")):
        dd = Vertex.C
    elif(bbb == ("D" or "d")):
        dd = Vertex.D
    elif(bbb == ("E" or "e")):
        dd = Vertex.E
    elif(bbb == ("F" or "f")):
        dd = Vertex.F
    elif(bbb == ("G" or "g")):
        dd = Vertex.G
    elif(bbb == ("H" or "h")):
        dd = Vertex.H
    elif(bbb == ("I" or "i")):
        dd = Vertex.I
    elif(bbb == ("J" or "j")):
        dd = Vertex.J
    elif(bbb == ("K" or "k")):
        dd = Vertex.K
    elif(bbb == ("L" or "l")):
        dd = Vertex.L
    elif(bbb == ("M" or "m")):
        dd = Vertex.M
    elif(bbb == ("N" or "n")):
        dd = Vertex.N
    elif(bbb == ("O" or "o")):
        dd = Vertex.O
    elif(bbb == ("P" or "p")):
        dd = Vertex.P
    elif(bbb == ("Q" or "q")):
        dd = Vertex.Q
    elif(bbb == ("R" or "r")):
        dd = Vertex.R
    elif(bbb == ("S" or "s")):
        dd = Vertex.S
    elif(bbb == ("T" or "t")):
        dd = Vertex.T
    elif(bbb == ("U" or "u")):
        dd = Vertex.U
    elif(bbb == ("V" or "v")):
        dd = Vertex.V
    elif(bbb == ("W" or "w")):
        dd = Vertex.W
    elif(bbb == ("X" or "x")):
        dd = Vertex.X
    elif(bbb == ("Y" or "y")):
        dd = Vertex.Y
    elif(bbb == ("Z" or "z")):
        dd = Vertex.Z
    elif(bbb == ("AA" or "aa")):
        dd = Vertex.AA
    elif(bbb == ("AB" or "ab")):
        dd = Vertex.AB
    elif(bbb == ("AC" or "ac")):
        dd = Vertex.AC
    elif(bbb == ("AD" or "ad")):
        dd = Vertex.AD
    elif(bbb == ("AE" or "ae")):
        dd = Vertex.AE
    elif(bbb == ("AF" or "af")):
        dd = Vertex.AF
    elif(bbb == ("AG" or "ag")):
        dd = Vertex.AG
    elif(bbb == ("AH" or "ah")):
        dd = Vertex.AH
    elif(bbb == ("AI" or "ai")):
        dd = Vertex.AI
    elif(bbb == ("AJ" or "aj")):
        dd = Vertex.AJ
    elif(bbb == ("AK" or "ak")):
        dd = Vertex.AK
    elif(bbb == ("AL" or "al")):
        dd = Vertex.AL
    elif(bbb == ("AM" or "am")):
        dd = Vertex.AM
    elif(bbb == ("AN" or "an")):
        dd = Vertex.AN
    elif(bbb == ("AO" or "ao")):
        dd = Vertex.AO
    elif(bbb == ("AP" or "ap")):
        dd = Vertex.AP
    elif(bbb == ("D1" or "d1")):
        dd = Vertex.D1
    elif(bbb == ("D2" or "d2")):
        dd = Vertex.D2
    elif(bbb == ("D3" or "d3")):
        dd = Vertex.D3
    elif(bbb == ("D4" or "d4")):
        dd = Vertex.D4
    elif(bbb == ("D5" or "d5")):
        dd = Vertex.D5
    elif(bbb == ("D6L" or "d6l")):
        dd = Vertex.D6L
    elif(bbb == ("D6" or "d6")):
        dd = Vertex.D6
    elif(bbb == ("D6R" or "d6r")):
        dd = Vertex.D6R
    elif(bbb == ("D7" or "d7")):
        dd = Vertex.D7
    elif(bbb == ("D8" or "d8")):
        dd = Vertex.D8
    elif(bbb == ("D9" or "d9")):
        dd = Vertex.D9
    elif(bbb == ("D10" or "d10")):
        dd = Vertex.D10
    elif(bbb == ("D11L" or "d11l")):
        dd = Vertex.D11L
    elif(bbb == ("D11" or "d11")):
        dd = Vertex.D11
    elif(bbb == ("D11R" or "d11r")):
        dd = Vertex.D11R
    elif(bbb == ("D12L" or "d12l")):
        dd = Vertex.D12L
    elif(bbb == ("D12" or "d12")):
        dd = Vertex.D12
    elif(bbb == ("D12R" or "d12r")):
        dd = Vertex.D12R
    elif(bbb == ("I53" or "i53")):
        dd = Vertex.I53
    elif(bbb == ("I54" or "i54")):
        dd = Vertex.I54
    elif(bbb == ("I55" or "i55")):
        dd = Vertex.I55
    elif(bbb == ("56" or "i56")):
        dd = Vertex.I56
    elif(bbb == ("I57" or "i57")):
        dd = Vertex.I57
    elif(bbb == ("I58" or "i58")):
        dd = Vertex.I58
    
    print('-' * 20)
    print('グラフ情報:')
    print(graph)
    print('-' * 20)
    distances, path_dict = dijkstra(
        graph=graph,
        root_vertex = cc)###変える箇所(先頭)
    print(f'算出されたスタート地点({cc})から各頂点への最短距離情報:')
    for index, distance in enumerate(distances):
        vertex: VertexStr = graph.vertex_at(index=index)
        print('頂点 :', vertex, '距離 :', distance)
    print('-' * 20)

    start_vertex_idx = graph.index_of(vertex = cc)###変える箇所(先頭)
    last_vertex_idx = graph.index_of(vertex = dd)###変える箇所(目的地)
    route_path: RoutePath = to_route_path_from_path_dict(
        start_vertex_idx=start_vertex_idx,
        last_vertex_idx=last_vertex_idx,
        path_dict=path_dict)
    print(f'スタート地点({cc})から目的地({dd})までの最短経路:')
    for edge in route_path:
        print(edge)

#タキシング　直線４５km/h、旋回２７km/h