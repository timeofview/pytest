from controller.controller import Controller
from ui.cui import Cui


def main():
    controller = Controller()
    cui = Cui(controller)
    cui.start()
    exit(0)


if __name__ == '__main__':
    main()
