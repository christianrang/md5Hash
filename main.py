"""
This script will compare two md5 hashes one inputted by the user the other pulled from the
file

Example:

  $ python3 main.py
  Correct md5 hash: 0800fc577294c34e0b28ad2839435945
  Comparing hashes...
  Hashes match!
"""
import subprocess
import re

__authors__= ["T", "P"]
__version__= 1

def get_files_md5_hash(file_name):
  """
  Gets the md5 hash of a file

  Returns:
    str: md5 hash of a file
  """
  md5hash = subprocess.run(['md5sum', file_name], stdout=subprocess.PIPE).stdout
  md5hash = md5hash.decode('utf-8')
  md5hash = md5hash.split(' ')[0]
  return md5hash

def get_input_md5_hash():
  """
  Gets the md5 a user inputs
  
  Returns:
    str:   md5 hash inputted from the user
  """
  while True:
    md5_hash=input("enter_md5_hash: ")
    if verify_md5_hash(md5_hash):
      return md5_hash
    else:
      print("Inputted value was not a md5 hash")

def verify_md5_hash(md5_hash):
  """
  Verifies if the hash is an md5 hash

  Args:
    md5_hash (str): suspected md5 hash to be verified

  Returns:
    True if md5 hash, false if not
  """
  if re.match('[a-fA-F0-9]{32}', md5_hash):
    return True
  else:
    return False

def compare_md5_hashes(input_hash, file_hash):
  """
  Verifies if the md5 hashes are the same

  Args:
    input_hash (str): md5 hash input by the user
    file_hash (str): md5 hash pulled from the file
  
  Returns:
    True if md5 hashes match, false if not
  """
  if input_hash==file_hash:
    return True
  else:
    return False 

if __name__ == "__main__":
  users_md5_hash = get_input_md5_hash()
  print("Comparing hashes...")
  if compare_md5_hashes(input_hash=users_md5_hash, file_hash=get_files_md5_hash('test.txt')):
    print("Hashes match!")
  else:
    print("Something is fishy here... the hashes don't match")