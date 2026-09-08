class Solution:
    def countCommas(self, n: int) -> int:
        return (n > 999) * (n - 999)
        ##so if n>999 returns 1 and multiplies with n-999 else returns 0 and multiplies with the same resu;ts zero eff