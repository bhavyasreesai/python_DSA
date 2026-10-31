def bonus(rating,experience):
    if rating>=4:
        if rating>=5:
            if experience>=5:
                return "bonus is 25%"
        else:
            return "bonus is 20%"
    elif experience>=5:
        return"bonus is 5%"
    else:
        return "0 bonus"
rating=6
experience=6
print(bonus(rating,experience))


