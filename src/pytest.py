import writer
import reader
import draw

def main():
    writer.write()
    groups = reader.group_by(reader.read_csv())
    draw.draw(groups)

if __name__ == '__main__':
    main()