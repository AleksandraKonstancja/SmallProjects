class testCase():

    def __init__(self, point, integer):
    
        self.result = -1
        self.time = 0
        self.P = point
        self.k = integer

    def reset(self):
        self.time = 0
        self.result = -1

    def pointDouble(self, P):
        self.time+=1
        return 2*P

    def pointAdd(self,P,Q):
        self.time+=2
        return P+Q

    def original(self):

        Q = 0
        R = self.P
        for i in range(len(self.k)):
            if(self.k[i] == 1):
                Q = self.pointAdd(Q,R)
            R = self.pointDouble(R)

        self.result= Q

        print("Original: " + str(Q) + " Time: " + str(self.time))
        return Q

    def updated( self):
        Q = [0]*2
        R = self.P
        for i in range(len(self.k)):
            Q[1] = self.pointAdd(Q[0],R)
            R = self.pointDouble(R)
            Q[0] = Q[self.k[i]]

        self.result = Q[0]

        print("Updated: " + str(Q[0]) + " Time: " + str(self.time))
        return Q[0]


def main():

    testK = [[0,1,0,0,0,0],[0,0,0,1,1,1],[1,1,1,1,1,1]]
    for i in testK:
        test = testCase(5, i)
        test.original()
        test.reset()
        test.updated()
        

main()

# test1: implementation of original is correct, gives correct results
# test2: implementation of updated is correct, results are the same as original
# test3: original should have the higher execution time the more 1s in value
# test4: if P and Q are equal both operations become doubling
