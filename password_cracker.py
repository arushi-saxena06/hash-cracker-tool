import hashlib
import argparse
import string
import itertools
import sys
from tqdm import tqdm
import time

parser = argparse.ArgumentParser(description="Password Cracker")
parser.add_argument("--hash", required=True, help="Target hash to crack")
parser.add_argument("--type", help="Hash type (md5/sha256)")
parser.add_argument("--wordlist", default="wordlist.txt", help="Path to wordlist file")

args = parser.parse_args()

target_hash = args.hash
hash_type = args.type
wordlist_path = args.wordlist

# Auto-detect hash type by length
hash_type = None
hash_length = len(target_hash)

if hash_length == 32:
    hash_type = 'md5'
elif hash_length == 40:
    hash_type = 'sha1'
elif hash_length == 64:
    hash_type = 'sha256'
elif hash_length == 128:
    hash_type = 'sha512'
else:
    # Ask user manually if detection fails
    print("⚠️ Unable to auto-detect hash type by length.")
    hash_type = input("Please enter hash type (e.g., md5, sha1, sha256, sha512): ").strip().lower()

print(f"Detected hash type: {hash_type}")

# Read passwords from wordlist file
found = False
try:
    with open(wordlist_path, "r") as f:
        passwords = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(f"Wordlist file '{wordlist_path}' not found.")
    sys.exit()

# Crack password
for pwd in passwords:
    try:
        hashed_pwd = hashlib.new(hash_type, pwd.encode()).hexdigest()
    except ValueError:
        print(f"Unsupported hash type: {hash_type}")
        exit()

    if hashed_pwd == target_hash:
        print(f"✅ Password found: {pwd}")
        break
else:
    ch = input("Password not found in wordlist. Start brute-force attack? (y/n)").lower()
    if ch == "y":
        charset = string.ascii_lowercase + string.digits
        try:
            max_length = int(input("Enter maximum length:"))
            if max_length > 6:
                print("🚨 [WARNING] 🚨")
                print(f"You have set maximum password length to {max_length}.")
                print("Brute-force attacks beyond length 6 may take very long time!")
                print(f"Estimated combinations for length {max_length}: {len(charset)}^{max_length} = {len(charset) ** max_length} possibilities.")
        except ValueError:
            print("Invalid length input")
            sys.exit()
        try:
            for length in range(1, max_length + 1):
                total_combinations = len(charset) ** length
                print(f"\n🔍 Trying passwords of length {length} ({total_combinations} combinations)...")
                for pwd_tuple in tqdm(itertools.product(charset, repeat=length), total=total_combinations, desc=f"Length {length}"):
                    pwd = ''.join(pwd_tuple)
                    hashed_pwd = hashlib.new(hash_type, pwd.encode()).hexdigest()
                    if hashed_pwd == target_hash:
                        print(f"Password found (brute-force attack): {pwd}")
                        found = True
                        break
                if found:
                    break

            if not found:
                print("Password not found in brute-force attack.")
        except KeyboardInterrupt:
            print("⚠️ Brute-force interrupted by user!\nExiting...")
            sys.exit()
    else:
        print("Brute-force attack skipped.")