# A Dictionary with a List of votes as values
# Each of the list can hold multiple values
result = {
    1: ["PH"],
    2: ["PN"],
    3: ["PH"],
    4: [],
    5: ["BN"],
    6: ["PN"],
    7: ["PH"],
    8: ["PN"],
    9: ["PH"],
    10: ["BN", "PH"],
}


def processResult(result: dict[str, list[str]]):
    spoilt_amount = 0
    total_valid = 0
    votes = {}
    for val in result.values():
        if len(val) != 1:
            spoilt_amount += 1
            continue
        num_of_votes = votes.get(val[0], 0)
        num_of_votes += 1
        votes[val[0]] = num_of_votes
        total_valid += 1
    print(votes)
    print(
        f"""
Vote    Count   Percentage
BN      0{votes["BN"]}      {round(votes["BN"]/total_valid*100,2)}
PN      0{votes["PN"]}      {round(votes["PN"]/total_valid*100,2)}
PH      0{votes["PH"]}      {round(votes["PH"]/total_valid*100,2)}
Spoilt  0{spoilt_amount}
"""
    )


processResult(result)
