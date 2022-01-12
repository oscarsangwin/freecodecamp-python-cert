import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for k, v in kwargs.items():
            self.contents += [k] * v
    
    def draw(self, num_balls):
        hat_copy = self.contents

        if num_balls >= len(hat_copy):
            return hat_copy

        draw = []
        for _ in range(num_balls):
            index = random.randrange(len(hat_copy))
            draw.append(hat_copy[index])
            del hat_copy[index]

        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    found = 0

    def do_draw():
        draw = copy.deepcopy(hat).draw(num_balls_drawn)
        
        for k, v in expected_balls.items():
            for _ in range(v):
                if k in draw:
                    draw.remove(k)
                else:
                    # Failed
                    return False
        # Success
        return True

    for _ in range(num_experiments):
        found += do_draw()
    
    return found / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2)#000)