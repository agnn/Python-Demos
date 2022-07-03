import logging as lg

lg.basicConfig(filename= "logdict.txt" , level= lg.DEBUG , format= '%(name)s %(asctime)s %(levelname)s %(message)s')

class mydict:

    # this class contains all functions related to Dictionary operation

    def __init__(self, in_dict):
        lg.info("Constructor initialised")
        self.d = in_dict
        try:
            if type(self.d) != dict:
                lg.error("Passed value is not a dictionary, kindly retry with correct parameters")
                raise Exception ("Please provide correct parameters")
            lg.info("The dict passed by user is : %s", in_dict)
        except Exception as e:
            lg.error(e)


    def dict_keys(self):

        lg.info("Function call successful : dict_keys")
        _value , _keys , c = [] , [] , 0

        try:

            for k, v in self.d.items():
                _value.append(v)
                _keys.append(k)
                c += 1
            lg.info("The keys are : %s ",_keys)
            lg.info("The values are : %s", _value)
            lg.info("Total number of keys are : %s",c)

            return(c)
        except Exception as e:
            lg.error(e)



d = {"Name":("Agnik","Ritu","Sagnik","Sulata","Nilanjan"),
     "Age":(30,29,23,57,60,63)  ,
    "Location":("Bareilly","Bareilly","Delhi","Barasat","Barasat")
}

#d= [1,2,3,4,5]
d1=mydict(d)
d1.dict_keys()