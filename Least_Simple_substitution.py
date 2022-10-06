count_Freq = {}


# Python3 code to remove whitespace
def remove(string):
    return string.replace(" ", "")


# Driver Program

# input the string


P_Text = input("give me the Plant text Please")
P_Text = P_Text.upper()
P_Text.strip()
P_Text = remove(P_Text)

P_Text = ''.join([i for i in P_Text if i.isalpha()])
# P_Text = "abcdefghijklmnopqrstuvwxyz"

# contents = []
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     contents.append(line)

letterFrequency = {'E': 12.0,
                   'T': 9.10,
                   'A': 8.12,
                   'O': 7.68,
                   'I': 7.31,
                   'N': 6.95,
                   'S': 6.28,
                   'R': 6.02,
                   'H': 5.92,
                   'D': 4.32,
                   'L': 3.98,
                   'U': 2.88,
                   'C': 2.71,
                   'M': 2.61,
                   'F': 2.30,
                   'Y': 2.11,
                   'W': 2.09,
                   'G': 2.03,
                   'P': 1.82,
                   'B': 1.49,
                   'V': 1.11,
                   'K': 0.69,
                   'X': 0.17,
                   'Q': 0.11,
                   'J': 0.10,
                   'Z': 0.07}
#  finding freqancy
print(P_Text)
for i in P_Text:
    if i in count_Freq:
        count_Freq[i] += 1
    else:
        count_Freq[i] = 1
print(P_Text)
print("\n")
print(count_Freq)

# percentage
per_oo = {}
ss = sorted(list(count_Freq))
ss = set(ss)
# print(ss)
letterCount = 0
for k, m in count_Freq.items():
    letterCount += m
print(letterCount)

for i, j in count_Freq.items():
    per_oo[i] = (j / letterCount) * 100

print(per_oo)

# deciding rules
