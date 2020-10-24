from model.config import Config


def main():
    file = open('file.csv', "w")
    file.write(Config('version', 'name', 'path', 'filename', 'extension', 'args', 'threads', 'stdin').toString())
    # writer.write()
    # groups = reader.group_by(reader.read_csv())
    # draw.draw(groups)


if __name__ == '__main__':
    main()
