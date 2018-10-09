import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

map = {
        'node': dict(
            node1=dict(name="Node A", hostname="node1.stalab.ciena.com", ip="10.10.10.1"),
            node2=dict(name="Node B", hostname="node2.stalab.ciena.com", ip="10.10.10.2"),
            node3=dict(name="Node C", hostname="node3.stalab.ciena.com", ip="10.10.10.3"),
            node4=dict(name="Node D", hostname="node4.stalab.ciena.com", ip="10.10.10.4")
        ),
        'edge': {
            'edge1': dict(srcNode="node1", dstNode="node2", srcNodePort="1", dstNodePort="2", speed="10gig"),
            'edge2': dict(srcNode="node1", dstNode="node2", srcNodePort="2", dstNodePort="1", speed="1gig",type="fiber"),
            'edge3': dict(srcNode="node2", dstNode="node3", srcNodePort="1", dstNodePort="2", speed="10gig"),
            'edge4': dict(srcNode="node3", dstNode="node4", srcNodePort="2", dstNodePort="1", speed="1gig",type="fiber"),
            'edge5': dict(srcNode="node4", dstNode="node1", srcNodePort="1", dstNodePort="2", speed="10gig"),
            'edge6': dict(srcNode="node1", dstNode="node2", srcNodePort="2", dstNodePort="1", speed="1gig",type="fiber"),
            'edge7': dict(srcNode="node2", dstNode="node3", srcNodePort="1", dstNodePort="2", speed="10gig"),
            'edge8': dict(srcNode="node3", dstNode="node4", srcNodePort="2", dstNodePort="1", speed="1gig",type="fiber"),
            'edge9': dict(srcNode="node4", dstNode="node2", srcNodePort="2", dstNodePort="1", speed="1gig",type="fiber")
        },
        'link' : {
                  'link1' : [["node1",0,3,"10gig"],["node2",0,3,"10gig"]]
                }
    }