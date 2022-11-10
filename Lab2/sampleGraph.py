from matplotlib import pyplot

l1 = [1,2,3,4,5,6,7,8,9,10,11,12]
l2 = [1.1,4,5,9,10,14,15,16.32,20.33,25.4,44.5,61.0]

#pyplot.bar([1, 2, 3, 4, 5], [1.1, 10.0, 25.4, 44.5, 61.0]) 
pyplot.bar(l1,l2)

pyplot.xlabel("MONTH")
pyplot.ylabel("TEMPERATURE")
pyplot.xticks(l1, 
   ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
pyplot.show()