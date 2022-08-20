import os
from utils import *

# parsing
from argparse import ArgumentParser, RawTextHelpFormatter
import textwrap

# annotations
from io import TextIOWrapper


def check_and_notify(password_file: str, password: str) -> None:
    hash = string_to_sha1(password)
    
    found, freq = hash_in_breach(password_file, hash)
    if found:
        print(
            f"[WARNING] The password '{password}' has been seen " 
            + f"{freq:,} times before!"
            )
    else:
        print(f"[INFO]    The password '{password}' was not found.")


def my_parser() -> Tuple[TextIOWrapper, TextIOWrapper]:
    parser = ArgumentParser(
        description='Check if your password(s) appeared in a data breach.',
        formatter_class=RawTextHelpFormatter,
        epilog="...if it did, you should change it pronto(!)")

    parser.add_argument('-f', '--file', type=open,
        help=textwrap.dedent('''\
        use a password file instead of inputting passwords one by one.
        File must contain one password per line.
        '''))

    parser.add_argument('breach_file', type=open,
        metavar='leaked_passwords_file', 
        help=textwrap.dedent('''\
        a (SHA-1 hashed) passwords file, from several past data breaches.
        You can get (a really big) one here: https://haveibeenpwned.com/Passwords
        Note: the file MUST be ordered by hash.
        '''))

    args = parser.parse_args()

    return args.file, args.breach_file

if __name__ == '__main__':
    user_file, breach_file = my_parser()
    
    if user_file:
        # input-file mode
        with open(user_file.name) as f:
            for line in f:
                password = line.strip()
                check_and_notify(breach_file.name, password)
    else:
        # manual (one-by-one) mode
        while True:
            inp = input("\nEnter your password (q to exit): ")
            if inp == 'q':
                print("Exiting...")
                break
            elif inp in ['cls', 'clear']:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            check_and_notify(breach_file.name, inp)
