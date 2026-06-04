chars = input() + input() + input()
check = "AaBCcEeHKMOoPpTXxy"
result = [char for char in chars if char in check]

if len(result) == len(chars):
    print("en")
elif not result:
    print("ru")
else:
    print("mix")
