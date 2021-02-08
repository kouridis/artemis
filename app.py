import operator

class Adjacency(object):
    def __init__(self,object_Id,priority,distance,tier,attempts,hosr):
        self.object_Id=object_Id
        self.priority=priority
        self.distance=distance
        self.tier=tier
        self.attempts=attempts
        self.hosr=hosr

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.object_Id,self.priority,self.distance,self.tier,self.attempts,self.hosr)



res = []
with open('adjacencies.csv', 'r') as f:
    header = f.readline()
    for line in f:
        (object_Id, priority, distance, tier, attempts, hosr) = line.split(',')
        res.append(Adjacency(object_Id, priority, distance, tier, attempts, hosr))


#Sort on first level
res.sort(key=operator.attrgetter('priority'))

#Break on sublists based on first level
pr1 = [x for x in res if x.priority == '1']
pr2 = [x for x in res if x.priority == '2']
pr3 = [x for x in res if x.priority == '3']
pr4 = [x for x in res if x.priority == '4']

#Sort on second level
pr1.sort(key=operator.attrgetter('distance'), reverse=True)
pr2.sort(key=operator.attrgetter('tier'), reverse=True)
pr3.sort(key=operator.attrgetter('attempts'))
pr4.sort(key=operator.attrgetter('hosr'))

#Append sublists
final = pr1 + pr2 + pr3 + pr4

#Write output
with open('result.csv', 'w') as ff:
    ff.write(header)
    for x in final:
        ff.write(x.__str__())
