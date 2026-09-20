class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Add two binary strings without converting them to decimal first."""
        left = len(a) - 1
        right = len(b) - 1
        carry = 0
        result = []

        while left >= 0 or right >= 0 or carry:
            total = carry
            if left >= 0:
                total += int(a[left])
                left -= 1
            if right >= 0:
                total += int(b[right])
                right -= 1
            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))


print(Solution().addBinary("11", "1"))