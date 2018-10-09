import networkx as nx


class NMLayer1():
  """
  Network Manager Layer 1 Class to track the Layer 1 provision information in graph format
  """
  "Graph Id Counter"
  graphID: int = 0
  "Node ID Counter"
  nodeID: int = 0

  def __init__(self, map):
    """
    Constructor when a hash map is given to initialize and create some default view.
    :param map: Dictionary for the graph contains elements.
    :type map: dict
    >> map = {
        'node': dict(
            node1=dict(name="Node A", hostname="node1.stalab.ciena.com", ip="10.10.10.1"),
            node2=dict(name="Node B", hostname="node2.stalab.ciena.com", ip="10.10.10.2")
        ),
        'edge': {
            'edge1': dict(srcNode="node1", dstNode="node2", srcNodePort="1", dstNodePort="2", speed="10gig"),
            'edge2': dict(srcNode="node1", dstNode="node2", srcNodePort="2", dstNodePort="1", speed="1gig",type="fiber")
        },
        'link' : {
                  'link1' : [["node1",0,3,"10gig"],["node2",0,3,"10gig"]]
        }
    }
    """
    self.graphID = self.graph_id_get()
    self.graph = nx.Graph()
    if map is None or len(map) == 0:
      return
    def_map = dict(
      node = "add_node",
      edge = "add_edge",
      link = "add_link"
    )
    for key in map.keys():
      if key.lower() in def_map.keys():
        self.__getattribute__(def_map[key.lower()])(map[key])
      else:
        print("Wrong key: Current implemented are : {}",def_map.keys())
    return

  @classmethod
  def create_blank_graph(cls):
    return cls(map=None)

  @staticmethod
  def graph_id_get():
    """
    Returns the currently available Graph ID
    :return: Graph ID
    :type return: int
    """
    NMLayer1.graphID += 1
    return NMLayer1.graphID

  @staticmethod
  def node_id_get():
    """
    Returns the currently available Node ID
    :return: Node ID
    :type return: int
    """
    NMLayer1.nodeID += 1
    return NMLayer1.nodeID

  def add_node(self,node_map):
    """
    Add node and its data into the graph
    :param node_map:
    :type node_map: dict
    :return: None
    >> node_map = dict(
            node1=dict(name="Node A", hostname="node1.stalab.ciena.com", ip="10.10.10.1"),
            node2=dict(name="Node B", hostname="node2.stalab.ciena.com", ip="10.10.10.2")
        )
    """
    for node in node_map.keys():
      self.graph.add_node(node)
      self.graph.node[node]["id"] = self.node_id_get()
      for attr in node_map[node].keys():
        self.graph.node[node][attr] = node_map[node][attr]

  def add_edge(self,edge_map):
    """

    :param edge_map:
    :type edge_map: dict
    :return: None
    >> edge_map = {
            'edge1': dict(srcNode="node1", dstNode="node2", srcNodePort="1", dstNodePort="2", speed="10gig"),
            'edge2': dict(srcNode="node1", dstNode="node2", srcNodePort="2", dstNodePort="1", speed="1gig",type="fiber")
        }
    """
    for edge in edge_map.keys():
      self.graph.add_edge(edge_map[edge]["srcNode"],edge_map[edge]["dstNode"])
      self.graph[edge_map[edge]["srcNode"]][edge_map[edge]["dstNode"]]['weight'] = 1
      for attr in edge_map[edge].keys():
        self.graph[edge_map[edge]["srcNode"]][edge_map[edge]["dstNode"]][attr] = edge_map[edge][attr]

  def add_link(self,link_map):
    """
    Add the given link into map
    :param link_map:
    :type link_map: dict
    :return:
    >> link_map : {
                  'link1' : [["node1",0,3,"10gig"],["node2",0,3,"10gig"]]
                }
    """
    edge_map = {}
    for link in link_map.keys():
      if len(link_map[link]) != 2:
        continue
      src_port = link_map[link][0]
      dst_port = link_map[link][1]

      map = dict(
          srcNode = src_port[0],
          dstNode = dst_port[0],
          srcBlade = src_port[1],
          dstBlade = dst_port[1],
          srcPort = src_port[2],
          dstPort = dst_port[2],
          speed = src_port[3] if src_port[3] == dst_port[3] else ""
      )
      edge_map[link] = map
    self.add_edge(edge_map)
