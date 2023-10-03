from faker import Faker
from faker.providers import bank, company, internet, person

fake=Faker()

#ejemplo de un banco
fake.add_provider(bank)
fake.add_provider(company)
fake.add_provider(internet)
fake.add_provider(person)

#genero en japones nani
#fake=Faker("ja_JP")

for n in range(5):
    #print(fake.name())
    #print(fake.address())
    #print(fake.text())
    #print(fake.first_name())
    #print(fake.bban())
    print(fake.company())