import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.balls = kwargs
        self.content = []

        for ball in self.balls:
            counter = self.balls[ball]
            while (counter > 0):
                self.content.append(ball)
                counter -= 1


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return True
