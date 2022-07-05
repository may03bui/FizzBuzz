# Opted not to go down the command line route, though this could just as easily be done using 'sys'

def main():

    def define_rules():
        maxi = int(input("Enter the maximum number. "))
        print("There are rules for the following numbers: 3, 5, 7, 11, 13, 17.")

        rules = []
        num = -1
        while num != "/":
            num = input("Enter a number for that rule to be applied. / to exit; 0 to add all. """)
            if num == "0":
                rules = [3, 5, 7, 11, 13, 17]
            elif num != "/":
                rules.append(int(num))

        return maxi, rules

    def fizz_buzz(maxi, rules):

        for i in range(1, maxi+1):
            string_arr = []

            if i % 3 == 0 and 3 in rules:
                string_arr.append("Fizz")
            if i % 5 == 0 and 5 in rules:
                string_arr.append("Buzz")
            if i % 7 == 0 and 7 in rules:
                string_arr.append("Bang")
            if i % 11 == 0 and 11 in rules:
                string_arr = ["Bong"]

            if i % 13 == 0 and 13 in rules:

                # first_b = next(filter(lambda a : a[0] == "B", string_arr), -1)
                # Found the first occurrence of the actual word, not the index. Could add an extra line using
                # index(), but that just means there will be two linear searches.

                first_b = -1
                for n in range(0, len(string_arr)):
                    if string_arr[n][0] == "B":
                        first_b = n
                        break

                if first_b == -1:  # B not found
                    string_arr.append("Fezz")
                else:
                    string_arr.insert(first_b, "Fezz")

            if i % 17 == 0 and 17 in rules:
                string_arr.reverse()

            print(i, "".join(string_arr))

    fizz_buzz(*define_rules())


main()

# If I wanted to allow a user to define their own rules, I could allow them to enter a list of paired tuples.
# The first element could be the number that we take the modulo with, as above. The second element could be
# a function which is applied to the string - perhaps a lambda. If we want to add to the string if a multiple
# is found, then the function could look something like "lambda a : a + 'Fezz'", for example.
# The user would have to supply the rules in the tuple in the same order in which they wish the rules to be applied.
