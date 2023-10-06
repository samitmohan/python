from collections import defaultdict


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # adj matrix
        adj = defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node, parent):
            nonlocal ans
            passengers = 0
            # calculate the numbuer of passengers
            for child in adj[node]:
                if child != parent:  # there is no cycle forming
                    p = dfs(child, node)  # child and current node
                    passengers += p
                    ans += int(ceil(p / seats))
            return passengers + 1  # +1 because to go the root node also

        ans = 0  # global variable
        dfs(0, -1)
        return ans
