class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def freq(a,b):
            l2=[]
            my_dict={}
            for i in a:
                if i not in my_dict:
                    my_dict[i]=0
                else:
                    my_dict[i]+=1
            for i in range(k):
                    l2.append(max(my_dict, key=my_dict.get))
                    del my_dict[max(my_dict, key=my_dict.get)]
            return l2
        out=freq(nums,k)
        return out