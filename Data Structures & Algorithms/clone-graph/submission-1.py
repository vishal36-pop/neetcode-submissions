"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node == None:
            return None
        visited = set()
        q = collections.deque()
        q.append(node)
        #q to handle the duplicates 
        dq = collections.deque()
        dup_visited = {}
        first_node = Node(node.val)
        dup_visited[first_node.val] = first_node
        dq.append(first_node)
        visited.add(node)
        while q:
            u = q.popleft()
            #process it
            #create a deep copy of this
            du = dq.popleft()
            temp = []
            for v in u.neighbors:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
                    temp_node = Node(v.val)
                    temp.append(temp_node)
                    dq.append(temp_node)
                    dup_visited[temp_node.val] = temp_node
                else:
                        temp.append(dup_visited[v.val])
            du.neighbors = temp
        return first_node

            


            

