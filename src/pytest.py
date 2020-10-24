from model.config import Config
from persistence import reader


def main():
    # file = open('file.csv', "w")
    # file.write(Config('version', 'name', 'path', 'filename', 'extension', 'args', 'threads', 'stdin').toString())

    reader.read_configs('file.csv')
    # writer.write()
    # groups = reader.group_by(reader.read_csv())
    # draw.draw(groups)


if __name__ == '__main__':
    main()
