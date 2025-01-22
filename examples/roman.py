from enum import Enum


class Roman(Enum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000


class Solution:
    def romanToInt(self, s: str):
        idx = 0
        sumR = 0
        while idx <= len(s) - 1:
            letter = s[idx]
            next_idx = idx + 1 if idx < len(s) - 1 else len(s) - 1
            next_letter = s[next_idx]
            match letter:
                case Roman.I.name:
                    if next_letter == Roman.I.name:
                        sumR += Roman.I.value
                    elif next_letter == Roman.V.name or next_letter == Roman.X.name:
                        sumR -= Roman.I.value
                    else:
                        sumR += Roman.I.value
                    idx += 1
                    continue
                case Roman.V.name:
                    sumR += Roman.V.value
                    idx += 1
                    continue
                case Roman.X.name:
                    if next_letter == Roman.X.name:
                        sumR += Roman.X.value
                    elif next_letter == Roman.L.name or next_letter == Roman.C.name:
                        sumR -= Roman.X.value
                    else:
                        sumR += Roman.X.value
                    idx += 1
                    continue
                case Roman.L.name:
                    sumR += Roman.L.value
                    idx += 1
                    continue
                case Roman.C.name:
                    if next_letter == Roman.C.name:
                        sumR += Roman.C.value
                    elif next_letter == Roman.D.name or next_letter == Roman.M.name:
                        sumR -= Roman.C.value
                    else:
                        sumR += Roman.C.value
                    idx += 1
                    continue
                case Roman.D.name:
                    sumR += Roman.D.value
                    idx += 1
                    continue
                case Roman.M.name:
                    sumR += Roman.M.value
                    idx += 1
                    continue
                case _:
                    print("That's not a valid day of the week.")
        return sumR

    def intToRoman(self, num: int) -> str:
        roman = ''
        while num > 0:
            if num // 1000 >= 1:
                roman += Roman.M.name
                num -= Roman.M.value
                continue
            elif num // 900 >= 1:
                roman += Roman.C.name + Roman.M.name
                num -= Roman.M.value - Roman.C.value
                continue
            elif num // 500 >= 1:
                roman += Roman.D.name
                num -= Roman.D.value
                continue
            elif num // 400 >= 1:
                roman += Roman.C.name + Roman.D.name
                num -= Roman.D.value - Roman.C.value
                continue
            elif num // 100 >= 1:
                roman += Roman.C.name
                num -= Roman.C.value
                continue
            elif num // 90 >= 1:
                roman += Roman.X.name + Roman.C.name
                num -= Roman.C.value - Roman.X.value
                continue
            elif num // 50 >= 1:
                roman += Roman.L.name
                num -= Roman.L.value
                continue
            elif num // 40 >= 1:
                roman += Roman.X.name + Roman.L.name
                num -= Roman.L.value - Roman.X.value
                continue
            elif num // 10 >= 1:
                roman += Roman.X.name
                num -= Roman.X.value
                continue
            elif num // 9 >= 1:
                roman += Roman.I.name + Roman.X.name
                num -= Roman.X.value - Roman.I.value
                continue
            elif num // 5 >= 1:
                roman += Roman.V.name
                num -= Roman.V.value
                continue
            elif num // 4 >= 1:
                roman += Roman.I.name + Roman.V.name
                num -= Roman.V.value - Roman.I.value
                continue
            elif num // 1 >= 1:
                roman += Roman.I.name
                num -= Roman.I.value
                continue
        return roman


print(Solution().romanToInt("IV"))
print(Solution().romanToInt("III"))
print(Solution().romanToInt("V"))
print(Solution().romanToInt("VI"))
print(Solution().romanToInt("VII"))
print(Solution().romanToInt("VIII"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("X"))
print(Solution().romanToInt("XIII"))
print(Solution().romanToInt("XV"))
print(Solution().romanToInt("LXV"))
print(Solution().romanToInt("LXVI"))
print(Solution().romanToInt("LXVI"))
print(Solution().romanToInt("MLXVI"))
print(Solution().romanToInt("MDLXVI"))
