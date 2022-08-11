import numpy as np


def display(x, y, figure, pose, occupied):
    for i in range(x * y):
        print("-" if i not in (*figure[pose], *occupied) else "0",
              end=" " if (i + 1) % x != 0 else "\n")


def main():
    positions = {"O": [[4, 14, 15, 5]],
                 "I": [[4, 14, 24, 34], [3, 4, 5, 6]],
                 "S": [[5, 4, 14, 13], [4, 14, 15, 25]],
                 "Z": [[4, 5, 15, 16], [5, 15, 14, 24]],
                 "L": [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
                 "J": [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
                 "T": [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]}
    x, y = (int(i) for i in input().split())
    occupied = set()
    figure = np.array([])
    display(x, y, [[""]], 0, occupied)

    while True:
        command = input("\n")
        if command == "piece":
            figure = np.asarray(positions[input()])
            pose = 0
        elif command == "exit":
            return
        while command == "break" and not set(range(x * y - x, x * y)) - occupied:
            occupied -= set(range(x * y - x, x * y))
            occupied = {i + x for i in occupied}
        if not figure.any():
            display(x, y, [[""]], 0, occupied)
            continue
        if command in ("down", "right", "left", "rotate"):
            figure = np.array([i + x if (i + x <= x * y).all() else i for i in figure])
        if command == "right":
            figure = np.array(
                [i + 1 if (i // x >= (i + 1) // x).all() and not set(i + 1) & occupied else i for i in figure])
        elif command == "left":
            figure = np.array(
                [i - 1 if (i // x <= (i - 1) // x).all() and not set(i - 1) & occupied else i for i in figure])
        elif command == "rotate":
            new_pose = (pose + 1) % len(figure)
            if not set(figure[new_pose]) & occupied:
                pose = new_pose
        display(x, y, figure, pose, occupied)
        if (figure[pose] + x > x * y).any() or set(figure[pose] + x) & occupied:
            occupied.update(figure[pose])
            figure = np.array([])
        if set(range(x)) & occupied:
            print()
            display(x, y, [[""]], pose, occupied)
            return print("\nGame Over!")


if __name__ == "__main__":
    main()
