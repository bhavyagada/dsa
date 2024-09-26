from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: encoded += str(len(s)) + "#" + s
        return encoded
    
    def decode(self, str) -> List[str]:
        decoded, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#": j += 1
            length = int(str[i:j])
            decoded.append(str[j + 1:j + 1 + length])
            i = j + 1 + length
        return decoded

solution = Solution()
input_strs = ["neet", "co#de"]
encoded_str = solution.encode(input_strs)
print(encoded_str)
decoded_strs = solution.decode(encoded_str)
print(decoded_strs)

print("the list is decoded correctly:", input_strs == decoded_strs)
