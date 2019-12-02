import sys
from src.driver.ScientificCalc import ScientificCalc
import logging
logging.basicConfig(filename="logarithm_file.log", level=logging.INFO,
                    format='%(name)s - %(levelname)s - %(message)s',
                    filemode='w')


def main():
    try:
        number = float(sys.argv[1])
        class_obj = ScientificCalc()
        print(class_obj.logarithm(number))
    except ValueError as e:
        logging.debug(e)
    except TypeError as e:
        logging.debug(e)
    except Exception as e:
        logging.debug(e)