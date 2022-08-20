# Check-Password

There are millions of real world passwords previously exposed in data breaches.

This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.

This is a python script that helps you check if your password(s) appeared in a data breach. You may do so online, but not without giving away the password in question.

This tool lets you check whether a password was exposed **locally**, using a [hashed password file](https://haveibeenpwned.com/Passwords). 

## Required Programs & Files

* Python3 (no special requirements needed)
* Leaked (SHA-1) passwords list, ordered by hash

## Usage

```
git clone https://github.com/giyorahy/check-password.git
cd check-password
check_pass.py [-h] [-f FILE] leaked_passwords_file
```


## Brief 
```
Check if your password(s) appeared in a data breach.

positional arguments:
  leaked_passwords_file
                        a (SHA-1 hashed) passwords file, from several past data breaches.
                        You can get (a really big) one here: https://haveibeenpwned.com/Passwords
                        Note: the file MUST be ordered by hash.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  use a password file instead of inputting passwords one by one.
                        File must contain one password per line.

...if it did, you should change it pronto(!)
```
