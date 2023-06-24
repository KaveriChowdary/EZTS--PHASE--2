pq=[]
pq.append((1,"kaveri"))
pq.append((2,"hani"))
pq.append((3,"varshi"))
pq.append((4,"thrishi"))
print("priority queue is")
pq.sort(reverse =True)
print(pq)
print("original queue is")
while pq:
    print(pq.pop())