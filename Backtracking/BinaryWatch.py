def binaryWatch(turnedOn):
    res=[]
    for hours in range(12):
        for minutes in range(60):
            c=bin(hours).count('1') + bin(minutes).count('1')

            if c==turnedOn:
                res.append(f"{hours}:{minutes:02d}")
    return res
binaryWatch(10)