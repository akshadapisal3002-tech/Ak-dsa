class Solution(object):
    def removeDuplicates(self, s, k):
        st =[]
        n = len(s)
        for i in range(n):
            c= s[i]
            if not st:
                st.append((c,1))
                continue
            if st[-1][0]!= c:
                st.append((c,1))
                continue
            if st[-1][1] <(k-1):
                p = st[-1]
                st.pop()

                st.append((p[0],p[1]+1))
                continue
            st.pop()
        res = ""
            
        while st:
            p = st[-1]
            st.pop()
            while p[1]>0:
                res+= p[0]
                p = (p[0],p[1]-1)
        return res[:: -1]