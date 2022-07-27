vowels = 'aeiou'

ip_str = str(input("enter the sentence: "))

ip_str = ip_str.casefold()

c = {}.fromkeys(vowels,0)

for char in ip_str:
    if char in c:
        c[char] += 1

print(c)
