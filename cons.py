s = input().strip()

if s.isdigit():
    n = int(s)
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    if 0 <= n <= 9:
        print(words[n])
    else:
        print(words[n%10]) 
else:
    # Vowel check
    if s in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonant")
