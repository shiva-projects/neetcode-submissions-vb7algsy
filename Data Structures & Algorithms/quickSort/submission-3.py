# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def quickS(arr, s, e):
            if s >= e:
                return
            l = s 
            pivote = arr[e]
            for i in range(s, e):
                if arr[i].key < pivote.key:
                    arr[l], arr[i] = arr[i], arr[l]
                    l += 1
            arr[l], arr[e] = arr[e], arr[l]
            quickS(arr, s, l - 1)
            quickS(arr, l + 1, e)
        quickS(pairs, 0, len(pairs) -  1)
        return pairs 