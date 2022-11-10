import time, random
from tokenize import Double

class HashMap:
        def __init__(self, capacity = 6):
                self.capacity = capacity
                self.map = [None] * self.capacity
                self.name = "====[NoName]===="
		
        def _get_hash(self, key):
                hash = 0
                for char in str(key):
                        hash += ord(char)
                return hash % self.capacity
            
        def _h1(self, key):
            x = (((key + 7) * (key + 7)) / 16) + key
            return int(x % 11)
        
        def _reverse(self, key):
            return int(str(key)[::-1])
            
        def linear_probe(self, key, value, solveProblem = False):
            if not solveProblem:
                key_hash = self._get_hash(key)
            else:
                key_hash = self._h1(key)
            
            key_value = [key, value]
            
            if self.map[key_hash] is None:
                self.map[key_hash] = key_value
                return True;
            else:
                for index in range (key_hash, self.capacity):
                    if self.map[index] is None:
                        self.map[index] = key_value
                        return True;
                #This position means that the hashmap is full. No list storage, so we expand!
                #self.growMap()
                return False;
            
                
        def getDouble(self, key):
            key_hash = self._get_hash(key)
            if self.map[key_hash][0] == key:
                return self.map[key_hash][1]
            else:
                key_skip = (key_hash + self._reverse(key)) % self.capacity
                #BUG: So, what if the hash is not able to find an available spot? We need a contingency plan...
                while(self.map[key_skip][0] is not key):
                    key_hash = key_skip
                    key_skip = (key_hash + self._reverse(key)) % self.capacity
                return self.map[key_hash][1]
        
        def double_hash(self, key, value, solveProblem = False):
            if not solveProblem:
                key_hash = self._get_hash(key)
            else:
                key_hash = self._h1(key)
                
            key_skip = (key_hash + self._reverse(key)) % self.capacity
            key_value = [key, value]
                
            if self.map[key_hash] is None:
                self.map[key_hash] = key_value
                return True;
            else:
                while (self.map[key_skip] is not None):
                    key_hash = key_skip
                    key_skip = (key_hash + self._reverse(key)) % self.capacity
                self.map[key_skip] = key_value
                
		
        def Chaining(self, key, value):
                key_hash = self._get_hash(key)
                key_value = [key, value]
		
                if self.map[key_hash] is None:
                        self.map[key_hash] = list([key_value])
                        return True
                else:
                    for pair in self.map[key_hash]:
                        if pair[0] == key:
                            pair[1] = value
                            return True
                    self.map[key_hash].append(key_value)
                    return True
			
        def get(self, key):
                key_hash = self._get_hash(key)
                if self.map[key_hash] is not None:
                        for pair in self.map[key_hash]:
                                if pair[0] == key:
                                        return pair[1]
                return None
			
        def print(self):
                print(self.name)
                for item in self.map:
                    if item is None:
                        print([])
                    else:
                        print(str(item))
                        
        def _problem1(self):
            SET = [43,23,1,0,15,31,4,7,11,3]
            for item in SET:
                self.linear_probe(item,item,True)
            self.print()
        
        def _problem2(self):
            SET = [43,23,1,0,15,31,4,7,11,3]
            for item in SET:
                self.double_hash(item,item,True)
            self.print()
            
			
def main():
    '''start = time.time()   
    h = HashMap(capacity = 11)
    h.name = "Problem 1"
    h._problem1()
    end = time.time()
    RunTime = end - start
    print(f"TOTAL RUNTIME FOR PROBLEM 1: {RunTime*1000:.2f} ms")


    start = time.time()   
    y = HashMap(capacity= 11)
    y.name = "Problem 2"
    y._problem2()
    end = time.time()
    RunTime = end - start
    print(f"TOTAL RUNTIME FOR PROBLEM 2: {RunTime*1000:.2f} ms")
    '''
    #=====================================================================#
    '''start = time.time()
    z = HashMap(capacity= 100)
    z.name = "Chaining"
    for key in set
        z.Chaining(key,key)
    end = time.time()
    z.print()
    RunTime = end - start
    print(f"TOTAL RUNTIME FOR CHAINING ADD: {RunTime*1000:.2f} ms")
    
    start = time.time()
    for key in set:
        print(z.get(key))
    end = time.time()
    RunTime = end - start
    print(f"TOTAL RUNTIME FOR CHAINING GET: {RunTime*1000:.2f} ms")'''
    
    #=====================================================================#
    set = []
    for i in range (0,100):
        num = random.randint(0,100)
        set.append(num)
    DoubleHash = HashMap(capacity = 100)
    DoubleHash.name = "Double Hash"
    start = time.time()
    for key in set:
        DoubleHash.double_hash(key,key)
    end = time.time()
    RunTime = end - start
    print(f"TOTAL RUNTIME FOR DOUBLE HASH ADD: {RunTime*1000:.2f} ms")
    
    start = time.time()
    for key in set:
        DoubleHash.getDouble(key)
    end = time.time()
    RunTime = end - start
    print(f"TOTAL RUNTIME FOR DOUBLE GET: {RunTime*1000:.2f} ms")
    

main()

'''
Testing The Get for Chaining:
Chaining
[[22, 22], [40, 40], [31, 31], [13, 13]]
[[23, 23], [50, 50], [32, 32]]
[[15, 15], [33, 33], [60, 60], [51, 51], [24, 24]]
[[43, 43], [16, 16], [34, 34], [52, 52]]
[[62, 62], [26, 26], [71, 71], [17, 17], [44, 44]]
[[81, 81], [45, 45], [54, 54], [72, 72], [18, 18]]
[[46, 46], [64, 64], [91, 91], [73, 73], [82, 82]]
[[83, 83], [56, 56], [38, 38], [92, 92], [65, 65]]
[[39, 39], [66, 66], [84, 84], [48, 48], [75, 75]]
[[76, 76], [94, 94], [58, 58], [85, 85]]
[[68, 68], [77, 77]]
[[96, 96]]
[[97, 97], [79, 79], [88, 88]]
[]
[[99, 99]]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[[100, 100]]
[]
[]
[[0, 0]]
[]
[[2, 2]]
[[3, 3]]
[[4, 4]]
[]
[[6, 6]]
[[7, 7]]
[]
[[9, 9]]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[[10, 10]]
[[11, 11], [20, 20]]
[[12, 12], [21, 21]]
TOTAL RUNTIME FOR CHAINING ADD: 1.00 ms
2
39
10
76
97
46
81
83
56
68
64
15
22
91
3
99
38
9
43
92
62
83
76
65
40
4
11
26
73
16
64
39
68
71
33
66
100
15
6
94
96
45
62
58
77
54
40
46
34
84
60
82
51
65
68
23
79
65
50
99
32
2
72
31
11
85
34
96
88
3
18
20
3
13
34
12
0
48
62
7
97
76
71
46
99
43
12
2
6
10
24
9
12
75
52
17
44
85
62
21
TOTAL RUNTIME FOR CHAINING GET: 15.96 ms


Sample Run from number 1-5
Problem 1
[31, 31]
[43, 43]
[23, 23]
[0, 0]
[15, 15]
[1, 1]
[4, 4]
[]
[7, 7]
[11, 11]
[3, 3]
TOTAL RUNTIME FOR PROBLEM 1: 2.00 ms
Problem 2
[31, 31]
[43, 43]
[23, 23]
[0, 0]
[4, 4]
[1, 1]
[]
[7, 7]
[15, 15]
[11, 11]
[3, 3]
TOTAL RUNTIME FOR PROBLEM 2: 2.00 ms
Chaining
[[13, 13], [22, 22], [31, 31], [40, 40]]
[[50, 50], [32, 32]]
[[33, 33], [24, 24], [60, 60], [51, 51]]
[[52, 52], [34, 34], [25, 25], [70, 70]]
[[71, 71], [53, 53], [26, 26]]
[[72, 72], [90, 90], [54, 54], [36, 36], [63, 63], [27, 27]]
[[73, 73], [28, 28], [37, 37], [46, 46], [19, 19], [64, 64], [91, 91], [82, 82], [55, 55]]
[[47, 47], [92, 92], [74, 74], [29, 29], [65, 65], [83, 83]]
[[57, 57], [84, 84], [66, 66], [48, 48], [39, 39]]
[[49, 49], [67, 67], [85, 85], [76, 76]]
[[68, 68], [77, 77]]
[[78, 78], [69, 69]]
[[97, 97], [79, 79]]
[[98, 98]]
[[99, 99]]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[[100, 100]]
[]
[]
[[0, 0]]
[[1, 1]]
[[2, 2]]
[[3, 3]]
[]
[[5, 5]]
[[6, 6]]
[[7, 7]]
[[8, 8]]
[[9, 9]]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[]
[[10, 10]]
[[20, 20], [11, 11]]
[[21, 21]]
TOTAL RUNTIME FOR CHAINING: 1.99 ms
'''