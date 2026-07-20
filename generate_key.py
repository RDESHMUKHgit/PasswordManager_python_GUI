from cryptography.fernet import Fernet

key = Fernet.generate_key()

#!! Never regenerate this key unless you want to lose access to all previously encrypted passwords.
# with open("secret.key", "wb") as key_file:
#     key_file.write(key)
    