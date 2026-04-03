import os
from time import sleep


def ft_tqdm(lst: range) -> None:
    """Custom tqdm-like progress bar using yield."""
    total = len(lst)
    terminal_w = os.get_terminal_size().columns
    bar_width = terminal_w * 77 // 100
    percentage_width = terminal_w * 3 // 100
    counter_w = terminal_w - bar_width - percentage_width
    for index, item in enumerate(lst, 1):
        progress = index / total
        filled = int(progress * bar_width)

        bar = "█" * filled + "=" * (bar_width - filled)
        counter = f" {index}/{total} ".ljust(counter_w)
        percentage = f"{progress * 100:.0f}%".ljust(percentage_width)

        print("\r" + percentage + bar + counter, end="")

        yield item

    print()


def main():
    for i in ft_tqdm(range(333)):
        sleep(0.01)


if __name__ == '__main__':
    main()
