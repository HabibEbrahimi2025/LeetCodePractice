def verifyPreorder(preorder):
    arr=preorder.split(',')

    slot=1

    for ch in arr:
        slot-=1
        if slot<0:
            return False
        if ch!='#':
            slot+=2
    return slot==0

preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(verifyPreorder(preorder))
