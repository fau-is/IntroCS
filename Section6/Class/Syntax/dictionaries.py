dictionary = {}

d = {
    "key":"value",
    5:"value2"
}
condition = d["key"] == "value"

d[3.3] = "value3"

for elem in d:
    print(f"{elem}: {d[elem]}")
