class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_len= 0
        low=0
        basket ={}
        

        for high in range(n):
            basket[fruits[high]]= basket.get(fruits[high],0)+1
            

            while len(basket)>2:
                basket[fruits[low]] -=1    
                if basket[fruits[low]]==0:
                    del basket[fruits[low]]
                low+=1
            
            max_len= max(max_len,high-low+1)
        return max_len


