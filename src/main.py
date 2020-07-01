def myfunc():
    def unused() -> str:
        smth = 42
        max = 24
        if smth == smth:
            print("Hello?")
        return smth

    print("Hello!")


def main():
    myfunc()


if __name__ == "__main__":
    main()
