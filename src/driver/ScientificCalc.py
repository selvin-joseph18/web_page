"""program"""
import logging
logging.basicConfig(filename="configfile.log", level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')


class scientific_calc:
    """program"""

    def _init__(self, n_value):
        self.n_value = n_value

    @classmethod
    def cube_root(cls, n_value):
        """function"""
        try:

            v_value = int(n_value)
            if v_value > 0:
                print(v_value ** (1 / 3))
                return v_value ** (1 / 3)

            if v_value < 0:
                print(-(-v_value) ** (1 / 3))
                return -(-v_value) ** (1 / 3)

        except ValueError:
            logging.error(ValueError)
            return "ValueError"
