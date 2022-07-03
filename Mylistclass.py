import logging as lg

#Create basic log file
lg.basicConfig(filename= "loglist.txt" , level= lg.DEBUG , format= '%(name)s %(asctime)s %(levelname)s %(message)s')


class mylist : 
    # this class contains all functions related to List operation

        def __init__(self,in_list):  #Constructor to take a list from user.

            lg.info("Constructor initialised")
            self.l = in_list
            try:
                if type(self.l) != list:
                    raise Exception("Please pass only list")
                lg.info("The list passed by user is : %s",in_list)
            except Exception as e:
                lg.error(e)


        def list_reverse(self):             
            'This function will reverse your list'
            lg.info("list_reverse function initialised")
            try:
                 lg.info("Reversed list is : %s", self.l[::-1])
                 return (self.l[::-1])
            except Exception as e:
                lg.error(e)

        def find_all_list(self):
            'This function finds all list elements inside a given list'
            lg.info("find_all_list function initialised")
            try:
                z=[]
                for i in range(len(self.l)):
                    if type(self.l[i]) == list:
                        z.append(self.l[i])
                lg.info("All list elements are : %s", z)
            except Exception as e:
                lg.error(e)

        def extract_numbers_list(self):
            'This function will extract all numbers from the given list, returns the sum of all numbers'
            lg.info("extract_numbers_list function initialised ")

            try:

                s = []

                'Loop to extract numbers and append to a temporary list'
                for i in self.l:
                    if type(i) == list or type(i) == tuple or type(i) == set:
                        for j in i:
                            if type(j) == int:
                                s.append(j)

                    if type(i) == dict:

                        for k in i.items():
                            for v in k:
                                if type(v) == int:
                                    s.append(v)
                lg.info("All numbers in the list are  : %s", s)
                return s
            except Exception as e:
                lg.error(e)

        def sum_list(self):
            'It returns the sum of all numbers in list'

            try:
                lg.info("sum_list function initialised")

                u= mylist.extract_numbers_list(self) #fucntion call within a funciton from the same class

                lg.info("The list of numbers imported from function extract_numbers_list : %s", u)

                sum = 0

                for i in range(len(u)):
                    sum = sum + i

                lg.info("The sum of all numbers in the list are : %s", sum)
                return sum

            except Exception as e:
                lg.error(e)

        def extract_odd(self):
            'Function to extract odd numbers from given list'
            o=[]
            lg.info("extract_odd function initialised")
            try:
                u = mylist.extract_numbers_list(self)

                for i in range(len(u)):
                    if ((u[i] % 2) != 0):
                        o.append(u[i])

                lg.info("The odd numbers are : %s" ,o)
                return o

            except Exception as e :

                lg.error(e)

        def count_element_list(self):
            'This function will return you the occurrence of each element in a given list'

            lg.info("count_element_list function initialised")

            try:
                _temp = [] #temporary list to append all data from list

                for i in self.l:
                    if type(i) == list or type(i) == tuple or type(i) == set:
                        for j in i:
                            _temp.append(j)

                    if type(i) == dict:

                        for k, v in i.items():
                            _temp.append(k)
                            _temp.append(v)

                _s = list(set(_temp))

                for i in _s:
                    lg.info("element : %s , count : %s ",i,_temp.count(i))

                return _temp

            except Exception as e:

                lg.error(e)

        def count_string_list(self):
            'The function returns all strings in list'

            lg.info("count_String_list function initialised")

            try:

                _ad = mylist.count_element_list(self)
                _str = []
                for i in _ad:
                    if type(i) == str:
                        _str.append(i)

                lg.info('All the strings in dataset : %s', str(set(_str)))

            except Exception as e:

                lg.error(e)

        def listappend(self,a):
            'This function will append the existing list with passed element'
            lg.info("listappend function initialised")
            try:
                if type(self.l) != list:
                    lg.error("Only list can be appended with list")
                b = [a]
                lg.info("appended list is : %s", self.l+b)
                return (self.l + b)
            except Exception as e:
                lg.error(e)
                
    ######## End of Class ########
    
    




#Example below


#l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
#l=[[1,2,3,'a',4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh','k2':'ineuron','k3':'kumar',99:100,101:108},["ineuron","data science"]]
l = [9,8,1,2,3,4,'a','b']
l1 = mylist(l)

'''l1.list_reverse()
l1.find_all_list()
l1.sum_list()
l1.extract_numbers_list()
l1.extract_odd()
l1.count_element_list()
l1.count_string_list()

l1.listappend("Appended")'''
