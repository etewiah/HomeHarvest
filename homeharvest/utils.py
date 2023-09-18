import re


def parse_address_two(street_address: str):
    if not street_address:
        return None
    apt_match = re.search(r"(APT\s*[\dA-Z]+|#[\dA-Z]+|UNIT\s*[\dA-Z]+|LOT\s*[\dA-Z]+)$", street_address, re.I)

    if apt_match:
        apt_str = apt_match.group().strip()
        apt_str = re.sub(r"(APT\s*|UNIT\s*|LOT\s*)", "#", apt_str, flags=re.I)
        return apt_str
    else:
        return None

if __name__ == "__main__":
    print(parse_address_two("810 E Colter St APT 32"))
    print(parse_address_two("1234 Elm Street apt 2B"))
    print(parse_address_two("1234 Elm Street UNIT 3A"))
    print(parse_address_two("1234 Elm Street unit 3A"))
