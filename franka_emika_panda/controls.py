import numpy as np

class PositionController:
    def __init__(self, model):
        self.nu = model.nu
        self.q_des = np.zeros(self.nu)

    def compute(self, data):
        # retorna posição desejada
        return self.q_des
