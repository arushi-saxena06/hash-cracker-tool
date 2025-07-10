# hash-cracker-tool 🔓

A Python-based hash cracking tool using dictionary and brute-force attacks with support for common hash types (MD5, SHA1, SHA256, SHA512).

This project was developed as part of the **InLighn Tech Internship Program** to demonstrate the concepts of **hash cracking**, **multithreading**, and **password security** in cybersecurity.

---

## 🔑 Features:
- Supports **MD5**, **SHA-1**, **SHA-256**, and **SHA-512** hashes (auto-detects by hash length)
- Cracks passwords using:
  - ✅ Wordlist-based dictionary attack
  - ✅ Brute-force attack with configurable character set & length
- Detects common hash types automatically
- Provides warnings for potentially long brute-force runs
- Handles keyboard interruptions gracefully (Ctrl + C)
- Easy-to-use via command-line interface

---

## 🚀 How It Works:
1. User provides a hashed password via command-line.
2. The tool tries to crack it via wordlist first.
3. If the password isn’t found, user can optionally run a brute-force attack.

---

### Usage:
```bash
python password_cracker.py --hash <hash_value>

Optional Arguments:

    --wordlist → Path to wordlist file (default: wordlist.txt)

    --type → Manually specify hash type (usually auto-detected)

📄 Example:

python password_cracker.py --hash 098f6bcd4621d373cade4e832627b4f6

## ⚠️ Disclaimer:

This tool is for educational and ethical testing purposes only.
Do NOT use it for unauthorized access or malicious activities.
📜 License:

## 📜 MIT License (Free to use, with conditions)

## ✨ Credits:

Developed by Arushi Saxena ([Github]https://github.com/arushi-saxena06/hash-cracker-tool) during the InLighn Tech Internship Program.