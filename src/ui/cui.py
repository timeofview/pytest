import sys


class Cui:
    def __init__(self, controller):
        self.controller = controller

    def start(self):
        print("Write run, draw or exit")

        for line in sys.stdin:
            print(line)
            if line.rstrip() == 'run':
                print("Started")
                self.controller.run()
                self.controller.save_groups()
            elif line == 'draw':
                self.controller.read_plots()
                self.controller.draw()
            else:
                exit(0)
