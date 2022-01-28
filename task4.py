with open("Odd-Numbers.txt", "r") as input_file:

    with open("Output.txt", "w") as output_file:

        odds = []

        for num in input_file:
            try:
                num = int(num)
                if num % 2:
                    odds.append(num)
            except ValueError:
                pass

        for line in odds:
            output_file.write(str(line) + '\n')