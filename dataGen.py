from faker import Faker
fake = Faker()
import time 
#  to create sample data in form of given schema with
# author name , text, and timestamp

def get_registered_user():
    return {
        "author_name": fake.name(),
        "content": fake.paragraph(nb_sentences=20),
        "created_at": fake.date_time()
    }


if __name__ == "__main__":
    while True:
        print(get_registered_user())
        time.sleep(3)
    