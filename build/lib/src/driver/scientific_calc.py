import math
import logging
# class driver:
#     def __init__(self,y):
#         self.y=y


class ScientificCalc:

    def __init__(self):
        self.number = 0
        self.result = 0

    @classmethod
    def ln_func(cls , x):
        logging.basicConfig(filename="ScientificCalcLog.log", level=logging.ERROR,
                            format="%(asctime)s:%(levelname)s:%(message)s", filemode="w")

        try:
            if "." in str(x):
                x=float(x)
                if x > 0:
                    result = math.log(x)
                elif x == 0:
                    result = "infinity"
                else:
                    result = "-NAN-"
                return result
            else:
                x=int(x)
                if x > 0:
                    result = math.log(x)
                elif x == 0:
                    result = "infinity"
                else:
                    result = "-NAN-"
                return result
            return result
        except ValueError as t:
            result = "string is not accepted"
            logging.error(t)
            return result

        except Exception as e:
            result = "Enter a valid value"
            logging.error(e)
            return result