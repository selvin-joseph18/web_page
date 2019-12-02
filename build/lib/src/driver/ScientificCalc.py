"""Program for calculating square root"""
import logging
logging.basicConfig(filename="confile.log", level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')


class ScientificCalc:
    def __init__(self,x_value):
        self.x_value=x_value

    @classmethod
    def square_root(self,x_value):
        """function for calculating square root"""
        try:
            x_value = int(x_value)
            if x_value >= 0:
                return x_value**0.5
            elif x_value < 0:
                imaginary_no = complex(x_value)**0.5
                return imaginary_no
        except ValueError:
            logging.error(ValueError.message)
            return "expecting integer value"

