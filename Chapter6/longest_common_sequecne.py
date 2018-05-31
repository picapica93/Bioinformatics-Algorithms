#longest common sequence
#indel=0 point align=1point

def lcsbacktrack(v, w):
    import numpy as np
    s=np.zeros((len(v)+1,len(w)+1))
    backtrack=np.zeros((len(v)+1,len(w)+1))
    #1 stands for deletion, 2 stands for insertion, 3 stands for match
    backtrack[1:len(v)+1,0]=1
    backtrack[0, 1:len(w)+1] = 2
    for i in range(len(v)):
        for j in range(len(w)):
            if v[i]==w[j]:
                s[i+1,j+1]=max(s[i,j+1],s[i+1,j],s[i,j]+1)
            else:
                s[i + 1, j + 1] = max(s[i, j + 1], s[i + 1, j])
            if s[i+1,j+1]==s[i,j+1]:
                backtrack[i+1,j+1]=1
            elif s[i+1,j+1]==s[i+1,j]:
                backtrack[i+1,j+1] = 2
            else:
                backtrack[i+1,j+1] = 3
    return backtrack


def outputlcs(backtrack1,v,i,j,result):
    if i==0 or j==0:
        return
    if backtrack1[i,j]==1:
        outputlcs(backtrack1,v,i-1,j,result)
    elif backtrack1[i,j]==2:
        outputlcs(backtrack1,v,i,j-1,result)
    else:
        outputlcs(backtrack1, v, i - 1, j - 1,result)
        result.append(v[i-1])


v='apple'
w='happe'

v='CAGCTGGGCTTAGTCGCTGAGGTAGCTCTGTGCAGTATGGTCCAGCATCTGGGGTAACCTGGCTTATTCATGGAGCATCTAGGGTCGCCGCCCTATTCATTGCCGAGTTAAATTATTGTCTTACGAAACTCCTGACGGTACTGGATGGCCGAGGGTTAGGGACGGCAGTCGCTACCCAGGGTCGACATGCTGCGCCCCAAGGGAAATTGAGGGAGACGGACGGCCTAGAACCATGCGGGGTCTATGGGATACTTTCCATGTGTACGGCTGCGCATTGACGTTGGCGGCAATATGTTAGAGTTGGAGGTGAGTTACCCGTCCGGGTCGACCCTGCGAGTAATTGCACTTCAATTCCACTCCGGATGTGATTATCTAAATTTTTAGTAGGAATACTCTCCGTGTTGACAGACAGATTTCAGCGTTTGTAGCACGCTAACGTCCTGGCGCGCAACGGACTGCAAAAGACGACTGAATCACCCAGGGACAACGATTCTAGGTGTGTGGCACACAGAAGGGCACCAAATGAAAGCACTTATTTAACCGCAACTACACGCGAAGCCAGTCACGTGCTAACGTAAATTGTCCAATAAATGGCCCGAGCTATTTAATGACTACCATGGGGAACAGCTTGCAAGAGAAAGGTGCGCACAAATGCCATTTGATACATTGTTAGTACGAACAGAACTGCAGCGTCTCTTCGTCGACGGATCCCCTCCCCGCGAAGCGCCCGCACAGTTCATGCGAGTATAGTGCCGATTCCTTATCAAGAGCATGTGGATTATGTCTCGGTCAGCCCTCGAGGAAATAG'
w='ATGTTATATCTGTAATCGTCGACTCGCGCCGATAAAAGGGTGGTTCAGCACGCGCAGATGCCATATATTATGGCAGTGATATCAGTAACCATGGCTAGTTTTCACGGCGTCCACACTTGCGGGGGGCCTGGACTGTTTTTATCAGCAACGCGGGACGCTAAGAGCTGCAACCTACAACAAAAATCCCTTTCCCAGTATTAGCTGCAAATGGGGACAGTGGATTGGTTGGGTTGGTGGCATGAACAACTCAATTGCATAACGGACACCCGTATTGGCATCAATGGGTAACCTGTTCGAGAAGGTGGTCACCAACGCCCTTCCTCGTCCATGAATACCCATTGTCCGGCTGTGAGATACCTCCCCCAAAAAAGATGGAAGGTGCAATCACCCAATCGTGAAAACAGGAGTTGGGTATTTTCAGTGGAGCAAACATTGTTTTCTACCCTGCGTTGATCAGCTAGCCTGGTTCGCGTCCCCTCTCAAGATTCCGTTTGGAGGACCTCCCCGAGCTTACTCCGTATCTGGGGTATAATGAACGATCTAGCTACACGAGTCTTGACTCGAGCAGAGTCAAAGTTGAGATAGCGGAGTGCCAGAATCCCATCGGGTTCAGTCGCGGTATTGTTTAGCCTCCGACACCGTCGTTAGACGTTAGACGAGGCAGCGCGTCCGACTGCCAAACATTGCACTATCGCGTCCACAGTAAAAGTACTACCGTGCCCCGTCGGTCTAATTGAAGATGGGTTCACAATGTTCCAGATGTGCTACCCTAAACACTTGCTGTGCCAGAGTCAATGATACCGCCTCACCGTGCGCAACGCCCTTCGTAGCCTACGTCAACTAAAACATGAATCCAGGTACGGGTTTTGATGCGGGTGAGACGCTCGTAGAAACGTGTTCATCTCCTCTTTCCGTCGATAGCAAAGTCTTGTAGGGGAAGATGAACACGAATGGGAGGTCGGAGCGAATCGAGGCCCCGTATGCATAG'

v='CTG'
w='TTAT'
import sys
sys.setrecursionlimit(10000)

backtrack=lcsbacktrack(v, w)
result=[]
outputlcs(backtrack,v,len(v),len(w),result)
print(''.join(result))