def jobSequencing(profit, deadline):
    jobs=[]
    for i in range(len(profit)):
        jobs.append((profit[i], deadline[i]))
    jobs.sort(key=lambda x:x[0], reverse=True)

    totalProfit=0
    jobSeqence=[]
    slot=[-1]*(max(deadline)+1)
    for job in jobs:
        for t in range(job[1],0,-1):
            if slot[t]==-1:
                slot[t]=job[1]
                jobSeqence.append(job[1])
                totalProfit+=job[0]
                break
    print(jobSeqence)
    print(totalProfit)
profit=[10,20,40,30]
deadline=[1,1,1,4]
jobSequencing(profit, deadline)
