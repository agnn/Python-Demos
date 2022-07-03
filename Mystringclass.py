import logging as lg

lg.basicConfig(filename= "logstr.txt" , level= lg.DEBUG , format= '%(name)s %(asctime)s %(levelname)s %(message)s')


class mystring :
    # this class contains all fucntions related to string operation

    def __init__(self,in_str):
        self.s = in_str
        lg.info("Constructor initialised")
        lg.info("The list passed by user is : %s", in_str)


    def str_slice(self,start_index, end_index, jump):
        'This function takes 3 parameter start index, end index and jump, and return you sliced string '
        lg.info("str_slice function initialised")
        try:
            lg.info("start index : %s , end index : %s , jump : %s ",start_index,end_index, jump)
            i = (self.s[start_index:end_index:jump])
            lg.info("Sliced string is %s " ,i )
            return i
        except Exception as e:
            lg.error(e)


    def str_reverse(self):
        'This function will reverse your string'
        lg.info("str_reverse function initialised")
        try:
             lg.info("Reversed string is : %s", self.s[::-1])
             return (self.s[::-1])
        except Exception as e:
            lg.error(e)

    def str_upper_split(self):
        'This function will convert to uppercase and split the string'
        lg.info("str_upper_split function initialised")
        try:

            z = self.s.upper()
            z = z.split(' ')
            lg.info("Converted string is : %s", z)
        except Exception as e:

            lg.error(e)

    def str_replace(self, var_find, var_replace):
        'This function will replace one word with the other'
        lg.info("str_replace function initialised")
        try:
            z= self.s.replace(var_find,var_replace)
            lg.info("The modifed string is : %s",z)
            return z
        except Exception as e:
            lg.error(e)

####End of Class###
'''
st = "this is My First Python programming class and i am learNING python string and its function"
s = mystring(st)
s.str_slice(0,300,3)
s.str_reverse()
s.str_upper_split()
s.str_reverse()
s.str_slice(0,300,3)

s.str_replace('Python','Java')
