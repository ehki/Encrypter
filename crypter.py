from crypttools import Window
import threading


def main() -> int:
    lw = Window()
    thread1 = threading.Thread()
    thread1.setDaemon(True)
    thread1.start()
    lw.start_loop()
    return 0


if __name__ == '__main__':
    main()
