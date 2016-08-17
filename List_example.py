def extendList(val, list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" %list1
print "list2 = %s" %list2
print "list3 = %s" %list3


def extendList1(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list

list11 = extendList1(10)
list21 = extendList1(123,[])
list31 = extendList1('a')

print "list11 = %s" %list11
print "list21 = %s" %list21
print "list31 = %s" %list31
