def repeatedDNA(s):
    seen=set()
    repated=set()

    for i in range(len(s)-9):
        seqeunce=s[i:i+10]

        if seqeunce in seen:
            repated.add(seqeunce)
        else:
            seen.add(seqeunce)
    print(repated)
s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
repeatedDNA(s)