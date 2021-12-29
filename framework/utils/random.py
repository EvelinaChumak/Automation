import random
import string


class Random():

    digits=string.digits
    leters_up=string.ascii_uppercase
    leters_low=string.ascii_lowercase
    symbols=string.punctuation 

    @staticmethod
    def get_string(length):
        choose = Random.leters_low + Random.leters_up + Random.digits + Random.symbols + ' '
        result =''.join(random.choice(choose) for x in range(length))
        return result
