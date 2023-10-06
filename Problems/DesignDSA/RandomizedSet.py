# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
class RandomizedSet(object):
    def __init__(self):
        self.nMap = {}
        self.nList = []

    def insert(self, val):
        res = val not in self.nMap
        if res:
            # add
            # key = value we want to add, val = index where it should be added (reference from array (last element))
            self.nMap[val] = len(self.nList)
            # add to list
            self.nList.append(val)
        return res  # false otherwise

    def remove(self, val):
        res = val in self.nMap
        if res:
            # remove by swapping the number with last element in array
            idx = self.nMap[val]
            lastVal = self.nList[-1]
            self.nList[idx] = lastVal  # swapping
            # remove from list
            self.nList.pop()
            # update map
            self.nMap[lastVal] = idx
            # delete that element from map
            del self.nMap[val]

        return res

    def getRandom(self):
        return random.choice(self.nList)
