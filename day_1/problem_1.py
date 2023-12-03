def get_first_digit(s: str):
     for c in s:
         if c in "".join([str(i) for i in range(10)]):
             return int(c)
         
def main():
    final_sum = 0
    with open("data.txt", mode="r") as f:
        for line in f:
            first_digit = get_first_digit(line)
            last_digit = get_first_digit(line[::-1])
            final_sum += int(f"{first_digit}{last_digit}")
    return final_sum

print(main())