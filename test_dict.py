entry = {}

entry["row1"] = {"col1": 23, "col2": 42}
entry["row2"] = {"col1": 33, "col2": 35}

print(entry["row1"])

print(entry["row1"]["col1"])

print([entry[d]["col1"] for d in entry])
