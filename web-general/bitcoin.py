def validate(address):
    """Validate a bitcoin address"""
    try:
        # Basic format check
        if not isinstance(address, str):
            return False
        if len(address) < 26 or len(address) > 35:
            return False
        
        # Check for valid characters
        allowed_chars = set("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
        if not all(char in allowed_chars for char in address):
            return False
            
        # Basic format validation passed
        return True
    except:
        return False

def is_valid(address):
    """Alias for validate function"""
    return validate(address)
