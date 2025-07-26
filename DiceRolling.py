class dice:
    def roll():
        import random
        first=random.randint(1,6)
        second=random.randint(1,6)
        result=(first,second)
        print(result)

dice.roll()