s = input().strip()
if s.lstrip('-').isdigit():
    n = int(s)
    if 0 <= n <= 9 and len(s) == 1:
        words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        print(words[n])
    else:
        if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
            print("yes")
        else:
            print("no")
else:
    if s in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonant")
