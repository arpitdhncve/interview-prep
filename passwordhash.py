import os

def hash_password(password: str, salt: bytes = None) -> dict:
    if salt is None:
        # Generate a new salt if one is not provided
        salt = os.urandom(16)
    
    # Hash the password with the salt using SHA-256
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    # Return the salt and the hashed password
    return {
        "salt": salt,
        "hashed_password": hashed_password
    }

def verify_password(stored_password: dict, provided_password: str) -> bool:
    # Hash the provided password with the stored salt
    hashed_provided_password = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), stored_password['salt'], 100000)
    
    # Compare the stored hashed password with the hashed provided password
    return hashed_provided_password == stored_password['hashed_password']

# Example usage
password = "my_secure_password"
result = hash_password(password)
print("Salt:", result["salt"].hex())
print("Hashed Password:", result["hashed_password"].hex())

# Verify the password
is_valid = verify_password(result, "my_secure_password")
print("Password is valid:", is_valid)
