#https://www.codewars.com/kata/52cf02cd825aef67070008fa/train/python
'''
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ 0123456789.,?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ 0123456789.,?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ 0123456789.,?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ 0123456789.,?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ 0123456789.,?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ 0123456789.,?
 1 1   1       1               1                               1                                                               1                                                                                                                               1     
 2 4   8       16              32                              64                                                              128               
                                                                                                          
 b 1  2
 d 2  4
 h 3  8
 p 4  16
 F 5  32 
   '''
def decode(s):
    alfe = "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa"
    nochange = "!@#$%^&*()_+-/="
    rez = ''
    for i, c in enumerate(s):
        if c in nochange:
             rez += c
        else:
            pos = alfe.index(c)
            rez +=  alfe[ (pos - i - 1) % len(alfe) ]
    return rez

def encode(s):
    
    alfe = "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa"
    nochange = "!@#$%^&*()_+-/"
    rez = ''
    for i in range(len(s)):
        if s[i] in nochange:
             rez += s[i]
        else:
            print(f'{s[i]}')
            pos = alfe.index(s[i])
            rez +=  alfe[ (pos + i + 1) % len(alfe) ]
    return rez

print(decode('QDDe/BlG/e%g5cEaqv4+CAHkoS+0CelZ#k,api7l*F)UWcHFhU^yc(emapvmRz2pNenzuGsOB=UVQ'))