import operator

class Adjacency(object):
    def __init__(self,object_Id,priority,distance,tier,attempts,hosr):
        self.object_Id=int(object_Id)
        self.priority=int(priority)
        self.distance=int(distance)
        self.tier=int(tier)
        self.attempts=int(attempts)
        self.hosr=float(hosr)

    def __repr__(self):
        return "{},{},{},{},{},{}\n".format(self.object_Id,self.priority,self.distance,self.tier,self.attempts,self.hosr)


with open('adjacencies.csv', 'r') as inputFile:
    header = inputFile.readline()
    adjacencyList = [x.strip().split(',') for x in inputFile.readlines()]

adjacencyList = [Adjacency(*x) for x in adjacencyList]

#Sort on first level
adjacencyList.sort(key = lambda x: x.priority)

#Sort on second level
secondLevelSort = zip(list({adjacency.priority for adjacency in adjacencyList}), \
    ['distance','tier','attempts','hosr'], \
    [True,True,False,False])

finalAdjacencyList = []
for i in secondLevelSort:
    finalAdjacencyList += (sorted(list(filter(lambda x: x.priority == i[0], adjacencyList)), \
                                  key = lambda x: getattr(x, i[1]), \
                                  reverse= i[2]))

#Write output
with open('result.csv', 'w') as outputFile:
    outputFile.write(header)
    for x in finalAdjacencyList:
        outputFile.write(str(x))
