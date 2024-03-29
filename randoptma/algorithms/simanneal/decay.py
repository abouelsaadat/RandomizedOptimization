"""  """

# Author: Mohamed Abouelsaadat
# License: MIT

import math


class Bezier:
    def __init__(self, init_T: float = 100, mid_point: float = 50) -> None:
        self.mid_pt = mid_point
        self.itr = -1
        self.init_T = init_T
        self.a = init_T - 2 * self.mid_pt
        self.b = 2 * self.mid_pt

    def __str__(self) -> str:
        return f"Bz {round(self.mid_pt/self.init_T, ndigits=2)}"

    def next_T(self) -> float:
        self.itr = max(0, min(self.itr + 1, self.init_T))
        if math.isclose(self.a, 0.0):
            t = self.itr / self.b
        else:
            t = (-self.b + math.sqrt(self.b**2 + 4 * self.a * self.itr)) / (2 * self.a)
        return (1 - t) ** 2 * self.init_T + 2 * (1 - t) * t * self.mid_pt


class Logarithmic:
    def __init__(self, init_T: float = 1e3) -> None:
        self.t = -1
        self.c = init_T * math.log(2)

    def next_T(self):
        self.t += 1
        return self.c / math.log(1 + self.t)


class Geometric:
    def __init__(self, init_T: float = 1e3, a: float = 0.8) -> None:
        self.T = init_T / a
        self.a = a

    def next_T(self):
        self.T = self.a * self.T
        return self.T


class TunedGeometric:
    def __init__(
        self, init_T: float = 1e3, a: float = 0.8, tuned_val: float = 100
    ) -> None:
        self.init_T = init_T
        self.tuned_val = tuned_val
        self.a_originl = a
        self.factor = init_T / tuned_val
        self.a = a ** (1 / self.factor)
        self.T = tuned_val / self.a

    def __str__(self) -> str:
        return f"TG {self.a_originl}/{self.tuned_val}"

    def next_T(self):
        self.T = self.a * self.T
        return self.T * self.factor


class Linear:
    def __init__(self, init_T: float = 1000, step: float = 10) -> None:
        self.T = init_T + step
        self.step = step

    def next_T(self):
        self.T = self.T - self.step
        return self.T


class ArithmeticGeometric:
    def __init__(self, init_T: float = 1e3, a: float = 0.8, b: float = 1e-5) -> None:
        self.T = (init_T - b) / a
        self.a = a
        self.b = b

    def next_T(self):
        self.T = self.a * self.T + self.b
        return self.T
