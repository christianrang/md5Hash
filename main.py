"""
This script will compare two md5 hashes one inputted by the user the other pulled from the
file

Example:

  $ python3 main.py
  Correct md5 hash: 0800fc577294c34e0b28ad2839435945
  Comparing hashes...
  Hashes match!

TODO:
  * uhhhh write the actual code???
"""
import subprocess

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
  md5_hash=input("enter_md5_hash: ")
  print("Md_5_hash is "  + md5_hash)
  return md5_hash

def verify_md5_hash(md5_hash):
  """
  Verifies if the hash is an md5 hash

  Args:
    md5_hash (str): suspected md5 hash to be verified

  Returns:
    True if md5 hash, false if not
  """


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
    print("file hash match hoooray!")
    print(f"hash: {input_hash}")
    return(True)


  else:
    print("NO MATCH. NO DICE. COULD BE MALICIOUS. UHOH")
    return(False)

if __name__ == "__main__":
  compare_md5_hashes(input_hash=get_input_md5_hash(), file_hash=get_files_md5_hash('test.txt'))