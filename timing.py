import time

def original( P, k):
    start = time.time()
    Q = 0
    R = P
    for i in range(len(k)):
        if(k[i] == 1):
            Q = Q+R
        R = 2*R
    end = time.time()
    print("Original: " + str(Q) + " Time: " + str(end-start))
    return Q

def updated( P, k):
    start = time.time()
    Q = [0]*2
    R = P
    for i in range(len(k)):
        Q[1] = Q[0] +R
        R = 2*R
        Q[0] = Q[k[i]]
    end = time.time()
    print("Updated: " + str(Q[0]) + " Time: " + str(end-start))
    return Q[0]

def main():
    testK = [[1,0,0,0,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1]]
    testP = [ 3,4,7]
    for i in testK:
        print(i)
        original(5,i)
        updated(5,i)
          
main()


