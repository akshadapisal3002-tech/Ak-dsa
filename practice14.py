class Solution:
    def Fruiasket(self ,fruits:list[int])->int:
        n =len(fruits)
        max_len = 0
        basket = {}

        for high in range(n):
            basket[fruits[high]] = basket.get[fruits[high],0]+1

            while len(basket)> k:
                basket[fruits[low]]-=1
                if basket[fruits[low]] == 0:
                    del basket[fruits[low]]
                low +=1

            max_len = max(max_len , high-low+1)
        return max_len