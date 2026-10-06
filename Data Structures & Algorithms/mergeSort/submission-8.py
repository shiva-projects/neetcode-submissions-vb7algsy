# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def merges(arr, s, e):
            if e - s + 1 <= 1:
                return 
            m = (s + e) // 2
            merges(arr, s, m)
            merges(arr, m + 1, e)
            merge(arr, s, m, e)
        def merge(arr, s, m, e):
            la, ra = arr[s : m + 1], arr[m + 1 : e + 1]
            l, r = 0, 0
            start = s
            while l < len(la) and r < len(ra):
                if la[l].key <= ra[r].key:
                    arr[start] = la[l]
                    l += 1
                else:
                    arr[start] = ra[r]
                    r += 1
                start += 1
            while l < len(la):
                arr[start] = la[l]
                start += 1
                l += 1
            while r < len(ra):
                arr[start] = ra[r]
                r += 1
                start += 1
        merges(pairs, 0, len(pairs) - 1)
        return pairs
