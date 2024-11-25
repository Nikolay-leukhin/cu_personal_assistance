from lexicon import Lexicon as lx


def main():
    print(lx.welcome)

    while True:
        act = int(input('lx.choose_act'))

        match act:
            case 1:
                ...
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 5:
                ...
            case 6:
                break
            case _:
                print(lx.no_such_action)




if __name__ == '__main__':
    main()