'''
11. STR 6%
12. DEX 6%
13. LUK 6%
14. INT 6%
15. HP 6%
16. MP 6%
17. DEF 6%
18. ALL 3%

19. STR 3%
20. DEX 3%
21. LUK 3%
22. INT 3%
23. HP 3%
24. MP 3%
25. DEF 3%
26. STR12
27. DEX 12
28. LUK 12
29. INT 12
30. HP 120
31. MP 120
32. DEF 120
33. Hp Heal
34. MP Heal
'''


class Maple:
    a = 0
    b = 0
    c = 0

    def __init__(self):
        self.F = None
        self.S = None
        self.T = None

    def first(self):
        self.F = int(input(
            '1번째 줄\n 1. STR 6% \n 2. DEX 6% \n 3. LUK 6% \n 4. INT 6% \n'
            ' 5. HP 6% \n 6. MP 6% \n 7. DEF 6% \n 8. ALL 3% \n'))
        a = self.F + 10
        return a

    def second(self):
        self.S = int(input(
            '2번째 줄\n 1. STR 3% \n 2. DEX 3% \n 3. LUK 3% \n 4. INT 3% \n 5. HP 3% \n 6. MP 3% \n 7. DEF 3% \n '
            '8. STR12 \n 9. DEX 12 \n 10. LUK 12 \n 11. INT 12 \n 12. HP 120 \n 13. MP 120 \n 14. DEF 120 \n'
            ' 15. Hp Heal \n 16. MP Heal \n'))
        b = self.S + 18
        return b

    def third(self):
        self.T = int(input(
            '2번째 줄\n 1. STR 3% \n 2. DEX 3% \n 3. LUK 3% \n 4. INT 3% \n 5. HP 3% \n 6. MP 3% \n 7. DEF 3% \n '
            '8. STR12 \n 9. DEX 12 \n 10. LUK 12 \n 11. INT 12 \n 12. HP 120 \n 13. MP 120 \n 14. DEF 120 \n'
            ' 15. Hp Heal \n 16. MP Heal \n'))
        c = self.T + 18
        return c

    def ary(self, times):
        f = open("C:/Users/mtn20/Desktop/values.txt", 'w')
        ray = []
        for i in range(times):
            fi = Mp.first()
            si = Mp.second()
            th = Mp.third()
            arr = list([fi, si, th])
            ray.append(arr)

        print(ray)
        f.write(str(ray))
        f.close()


if __name__ == '__main__':
    Mp = Maple()
    Mp.ary(2)
