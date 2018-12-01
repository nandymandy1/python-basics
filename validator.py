# Example of a custom module to be imported

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$", email))