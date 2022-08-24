import sys

import dns.resolver

resolver = dns.resolver.Resolver()

try:
    target = sys.argv[1]
    wordlist = sys.argv[2]
except Exception as error:
    print("Something went wrong ", error)
    sys.exit()
try:
    with open(wordlist, "r") as file:
        wordlist = file.read().splitlines()
    target = input("Type the target -> ")
except Exception as error:
    print("Wordlist not found ", error)

for subdomain in wordlist:
    try:
        sub_target = "{}.{}".format(subdomain, target)
        results = resolver.resolve(sub_target, "A")
        for r in results:
            print("{} -> {}".format(sub_target, r))

    except Exception as error:
        print(error)


