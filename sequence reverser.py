def Complement(Pattern):
    complement= {"A":"T","T":"A","G":"C","C":"G"}
    modified= "".join([complement[base]for base in Pattern])
    return modified


Pattern="AAAACCCGGT"
modifier=Complement(Pattern)[::-1]

print(modifier)
