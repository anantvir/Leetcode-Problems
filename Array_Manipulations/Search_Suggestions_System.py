import bisect
class Solution(object):
    """-------------------------------- Log(n) for each char search and O(n*log(n)) for sorting the array once---------------------"""
    def suggestedProducts(self,products,searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        curr = ''
        idx = 0
        global_list = []
        for char in searchWord:
            curr += char
            local_list = []
            idx = bisect.bisect_left(products,curr,idx)
            for product in products[idx:idx+3]:
                if product.startswith(curr):
                    local_list.append(product)
            global_list.append(local_list)
        return global_list



    """------------------------------ Brute Force O(N) for each character where N = No. of Products -----------------------------"""
    def suggestedProducts2(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        curr = ''
        global_lst = []
        if len(searchWord) == 0 or len(products) == 0:
            return []
        for char in searchWord:
            curr += char
            local_lst = []
            for product in products:
                if product[:len(curr)] == curr:
                    local_lst.append(product)
            local_lst.sort()
            if len(local_lst) >= 3:
                global_lst.append(local_lst[:3])
            else:
                global_lst.append(local_lst)
        return global_lst

s = Solution()

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(s.suggestedProducts(products,searchWord))

