class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_map = {i: [] for i in range(n)}

        for node1, node2 in edges:
            if node1 == node2:
                return False
            adj_map[node1].append(node2)
            adj_map[node2].append(node1)

        state_map = {i: 0 for i in range(n)}

        def has_cycle(node, parent):
            if state_map[node] == 1:
                return True
            if state_map[node] == 2:
                return False
            
            state_map[node] = 1
            for neighbor in adj_map[node]:
                if neighbor == parent:
                    continue
                if has_cycle(neighbor, node):
                    return True
            state_map[node] = 2
            return False

        if has_cycle(0, -1):
            return False

        return all(state_map[node] == 2 for node in range(n))