class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        hash_map={}
        for i in range(0,len(arr)):
            hash_map[arr[i]]=hash_map.get(arr[i],0)+1
        arr.clear()
        for j in hash_map:
            arr.append(j)
        k=0
        for i in range(len(arr)):
            k+=1
        return k
