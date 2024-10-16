class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely apoken language of India")
    def type(self):
        print("India is a developing country.")



class Bangladesh():
    def capital(self):
        print("Dhaka is the capital of Bangladesh.")
    def language(self):
        print("Bangla is the primary language of banladesh")
    def type(self):
        print("Bangladesh is a developing country.")


objInd = India()
objBD = Bangladesh()

for country in (objInd, objBD):
    country.capital()
    country.language()
    country.type()
    print()



