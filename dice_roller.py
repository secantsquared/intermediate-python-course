import random


def main():
    dice_rolls = 2
    dice_sum = 0

    for i in range(dice_rolls):
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}")
        dice_sum += roll

    print(f"You rolled a sum of {dice_sum}")


if __name__ == "__main__":
    main()
