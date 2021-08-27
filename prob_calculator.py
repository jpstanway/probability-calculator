import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.balls = kwargs
        self.contents = []

        for ball in self.balls:
            counter = self.balls[ball]
            while (counter > 0):
                self.contents.append(ball)
                counter -= 1

    def draw(self, num):
        count = num
        selections = []

        if (num <= len(self.contents)):
            while (count > 0):
                idx = random.randint(0, len(self.contents) - 1)
                ball = self.contents.pop(idx)
                selections.append(ball)
                count -= 1

        return selections


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    instance = hat
    matches = 0
    counter = num_experiments

    while (counter > 0):
        draw = instance.draw(num_balls_drawn)
        isEqual = False

        for ball in expected_balls:
            if(draw.count(ball) == expected_balls[ball]):
                isEqual = True
            else:
                isEqual = False

        if (isEqual):
            matches += 1

        counter -= 1

    return matches / num_experiments
