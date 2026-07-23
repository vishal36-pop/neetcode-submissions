"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        hashmap = collections.defaultdict(Node)
        source = [node]

        hashmap[1] = Node(1)
        visited = set()
        visited.add(node)
        queue = collections.deque(source)


        while queue:

            u = queue.popleft()
            for v in u.neighbors:
                if v not in visited:
                    visited.add(v)
                    hashmap[v.val] = Node(v.val)
                    queue.append(v)
                hashmap[u.val].neighbors.append(hashmap[v.val])
        return hashmap[1]


