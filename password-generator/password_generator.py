"""
Author          : Surya Teja <suryateja1919@gmail.com>
Description     : Random Password Generator
Website         : https://suryasr007.github.io
"""

import string
from copy import deepcopy
from random import shuffle, randint

try:
    from secrets import choice
except ImportError:
    from random import choice"""
Author          : Surya Teja <suryateja1919@gmail.com>
Description     : Random Password Generator
Website         : https://suryasr007.github.io
"""

import string
from copy import deepcopy
from random import shuffle, randint

try:
    from secrets import choice
except ImportError:
    from random import choice


class PasswordGenerator:
    """
    Password Generator Class
    """

    def __init__(self):
        self.minlen = 6
        self.maxlen = 16
        self.minuchars = 1
        self.minlchars = 1
        self.minnumbers = 1
        self.minschars = 1

        self.excludeuchars = ""
        self.excludelchars = ""
        self.excludenumbers = ""
        self.excludeschars = ""

        self.lower_chars = string.ascii_lowercase
        self.upper_chars = string.ascii_uppercase
        self.numbers_list = string.digits

        self._schars = [
            "!", "#", "$", "%", "^", "&", "*",
            "(", ")", ",", ".", "-", "_",
            "+", "=", "<", ">", "?"
        ]

        self._allchars = (
            list(self.lower_chars)
            + list(self.upper_chars)
            + list(self.numbers_list)
            + self._schars
        )

    def generate(self):
        """Generate password"""

        if (
            self.minlen < 0
            or self.maxlen < 0
            or self.minuchars < 0
            or self.minlchars < 0
            or self.minnumbers < 0
            or self.minschars < 0
        ):
            raise ValueError("Character length should not be negative")

        if self.minlen > self.maxlen:
            raise ValueError(
                "Minimum length cannot be greater than maximum length."
            )

        collectiveMinLength = (
            self.minuchars
            + self.minlchars
            + self.minnumbers
            + self.minschars
        )

        if collectiveMinLength > self.minlen:
            self.minlen = collectiveMinLength

        final_pass = [
            choice(list(set(self.lower_chars) - set(self.excludelchars)))
            for _ in range(self.minlchars)
        ]

        final_pass += [
            choice(list(set(self.upper_chars) - set(self.excludeuchars)))
            for _ in range(self.minuchars)
        ]

        final_pass += [
            choice(list(set(self.numbers_list) - set(self.excludenumbers)))
            for _ in range(self.minnumbers)
        ]

        final_pass += [
            choice(list(set(self._schars) - set(self.excludeschars)))
            for _ in range(self.minschars)
        ]

        currentpasslen = len(final_pass)

        all_chars = list(
            set(self._allchars)
            - set(
                list(self.excludelchars)
                + list(self.excludeuchars)
                + list(self.excludenumbers)
                + list(self.excludeschars)
            )
        )

        if len(final_pass) < self.maxlen:
            randlen = randint(self.minlen, self.maxlen)
            final_pass += [
                choice(all_chars)
                for _ in range(randlen - currentpasslen)
            ]

        shuffle(final_pass)

        return "".join(final_pass)

    def shuffle_password(self, password, maxlen):
        """Shuffle the given characters"""
        final_pass = [choice(list(password)) for _ in range(int(maxlen))]
        shuffle(final_pass)
        return "".join(final_pass)

    def non_duplicate_password(self, maxlen):
        """Generate password without duplicate characters"""

        allchars = deepcopy(self._allchars)
        final_pass = []

        try:
            for _ in range(maxlen):
                character = choice(allchars)
                element_index = allchars.index(character)

                final_pass.append(character)
                allchars.pop(element_index)

        except IndexError:
            raise ValueError(
                "Length should be less than 77 characters."
            )

        shuffle(final_pass)

        return "".join(final_pass)


# ----------------------------
# CLI PROGRAM
# ----------------------------
if __name__ == "__main__":

    print("=" * 40)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    pg = PasswordGenerator()

    while True:

        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password length should be at least 4.")
                continue

            pg.minlen = length
            pg.maxlen = length

            password = pg.generate()

            print("\nGenerated Password:")
            print(password)

        except ValueError:
            print("Please enter a valid number.")

        choice_input = input(
            "\nGenerate another password? (y/n): "
        ).lower()

        if choice_input != "y":
            print("\nThank you for using Password Generator.")
            break


class PasswordGenerator:
    """

    We can set properties such as

    | minlen     |   Minimum length of the password | 6\n
    | maxlen     |   Maximum length of the password | 16\n
    | minuchars  |   Minimum upper case characters required in password | 1\n
    | minlchars  |   Minimum lower case characters required in password | 1\n
    | minnumbers |   Minimum numbers required in password               | 1\n
    | minschars  |   Minimum special characters in the password         | 1\n

    Methods implemented in this class are

    generate() : Generates a password using default or custom propertiesself.

    shuffle_password(password, length) : Shuffle the given charactes and return a password from given characters.

    non_duplicate_password(length) : Generate a non duplicate key of givrn length

    """

    def __init__(self):
        self.minlen = 6
        self.maxlen = 16
        self.minuchars = 1
        self.minlchars = 1
        self.minnumbers = 1
        self.minschars = 1
        self.excludeuchars = ""
        self.excludelchars = ""
        self.excludenumbers = ""
        self.excludeschars = ""

        self.lower_chars = string.ascii_lowercase
        self.upper_chars = string.ascii_uppercase
        self.numbers_list = string.digits
        self._schars = [
            "!",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            ",",
            ".",
            "-",
            "_",
            "+",
            "=",
            "<",
            ">",
            "?",
        ]
        self._allchars = (
            list(self.lower_chars)
            + list(self.upper_chars)
            + list(self.numbers_list)
            + self._schars
        )

    def generate(self):
        """Generates a password using default or custom properties"""
        if (
            self.minlen < 0
            or self.maxlen < 0
            or self.minuchars < 0
            or self.minlchars < 0
            or self.minnumbers < 0
            or self.minschars < 0
        ):
            raise ValueError("Character length should not be negative")

        if self.minlen > self.maxlen:
            raise ValueError(
                "Minimum length cannot be greater than maximum length. The default maximum length is 16."
            )

        collectiveMinLength = (
            self.minuchars + self.minlchars + self.minnumbers + self.minschars
        )

        if collectiveMinLength > self.minlen:
            self.minlen = collectiveMinLength

        final_pass = [
            choice(list(set(self.lower_chars) - set(self.excludelchars)))
            for i in range(self.minlchars)
        ]
        final_pass += [
            choice(list(set(self.upper_chars) - set(self.excludeuchars)))
            for i in range(self.minuchars)
        ]
        final_pass += [
            choice(list(set(self.numbers_list) - set(self.excludenumbers)))
            for i in range(self.minnumbers)
        ]
        final_pass += [
            choice(list(set(self._schars) - set(self.excludeschars)))
            for i in range(self.minschars)
        ]

        currentpasslen = len(final_pass)
        all_chars = list(
            set(self._allchars)
            - set(
                list(self.excludelchars)
                + list(self.excludeuchars)
                + list(self.excludenumbers)
                + list(self.excludeschars)
            )
        )

        if len(final_pass) < self.maxlen:
            randlen = randint(self.minlen, self.maxlen)
            final_pass += [choice(all_chars) for i in range(randlen - currentpasslen)]

        shuffle(final_pass)
        return "".join(final_pass)

    def shuffle_password(self, password, maxlen):
        """Shuffle the given charactes and return a password from given characters."""
        final_pass = [choice(list(password)) for i in range(int(maxlen))]
        shuffle(final_pass)
        return "".join(final_pass)

    def non_duplicate_password(self, maxlen):
        """Generate a non duplicate key of given length"""
        allchars = deepcopy(self._allchars)
        final_pass = []
        try:
            for i in range(maxlen):
                character = choice(allchars)
                element_index = allchars.index(character)
                final_pass.append(character)
                allchars.pop(element_index)
        except IndexError as e:
            raise ValueError("Length should less than 77 characters.")

        shuffle(final_pass)
        return "".join(final_pass)
