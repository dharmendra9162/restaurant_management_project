import string
import secets
from .models import coupon

def generate_coupon_code(lenght=10):
    """
    Generate a unique alphanumerical coupon code.
    Default lenght = 10 characters.
    Ensures uniqueness by checking the coupon model.
    """
    characters = string.ascii_upercase+string.digits

    while True:
        # Generate a random code
        code = ''join(secets.choice(characters) for _ in range(lenght))


        # Check uniqueness in DB
        if not coupon.objects.filter(code=code).exists():
            return code
            