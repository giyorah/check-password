# core functionality
import hashlib
from io import SEEK_END

# annotations
from typing import BinaryIO, Tuple

# constants
HASH_SIZE = 40

def string_to_sha1(s: str) -> str:
    """
    Convert a string to SHA-1

    Args:
        s (str): a string

    Returns:
        str: SHA-1 hash, containing only uppercase hexadecimal digits
    """
    
    return hashlib.sha1(s.strip().encode('utf-8')).hexdigest().upper()

def get_whole_line(fh: BinaryIO, fp: int) -> bytes:
    """
    This function gets a pointer to a byte anywhere within a file
    and returns the whole line it's in.

    Args:
        fh (BinaryIO): the file object
        fp (int): a pointer to anywhere within the file

    Returns:
        bytes: the whole line, as a 'bytes' object
    """
    
    fh.seek(fp, 0)
    
    # get current line - b"db_hash:freq"
    curr_line = fh.readline() # might need alignment
    
    hash_freq = curr_line.strip().split(b':')
    while len(hash_freq) < 2 or len(hash_freq[0]) < HASH_SIZE:
        fp -= (HASH_SIZE - len(hash_freq[0]))
        fh.seek(fp, 0)
        curr_line = fh.readline()
        hash_freq = curr_line.strip().split(b':')
    
    return curr_line

def hash_in_breach(password_file: str, hash: str) -> Tuple[bool, int]:
    '''
    This function searches a given hash in a
    very very big hashed passwords file.

    - password_file: the path to the big password file, from several past
                     data breaches.
    - hash:          a SHA-1 hash to look for

    '''
    
    # open the passwords file -
    # binary mode is used for keeping the '\r' character
    pf = open(password_file, 'rb') 
    pf.seek(0, SEEK_END)

    # set file pointers (both point to bytes)
    begin = 0
    end = pf.tell() # points to last byte!
    while begin < end:
        mid = (end + begin) // 2   
        
        curr_line = get_whole_line(pf, mid) # in bytes
        db_hash, freq = curr_line.decode().strip().split(':')
        
        if (db_hash == hash):
            pf.close()
            return True, int(freq)
        elif hash > db_hash:
            begin = pf.tell()            
        else:
            end = pf.tell() - len(curr_line)
            
    pf.close()
    return False, 0
