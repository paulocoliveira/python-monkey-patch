import random
import string

def generate_email():
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase, k=username_length))
    domain = random.choice(['example.com', 'test.com', 'sample.com'])
    return f"{username}@{domain}"

def generate_custom_email():
    email = generate_email()
    # Modify the domain part of the email address
    custom_email = email.replace('@example.com', '@customdomain.com')
    print(custom_email)
    return custom_email