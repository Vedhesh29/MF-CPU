import os

data_list = []
text_list = []
instruction_set = []
current = None

opcode_map = {
    "Ad": "00",
    "Su": "01",
    "Lo": "10",
    "St": "11"
}

with open("demo.mf", "r", encoding="utf8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line.lower() == "data:":
            current = "data"
            continue
        if line.lower() == "text:":
            current = "text"
            continue

        if current == "data":
            parts = line.split()
            data_list.extend(parts)

        elif current == "text":
            text_list.append(line)

# Makes sure new data.txt file is created every time its ran
try:
    os.remove("data.txt")
except FileNotFoundError:
    pass

with open("data.txt", "w") as file:
    file.write("v3.0 hex words plain \n")
    for i in data_list:
        file.write(i + " ") 

character = "/"
for i in text_list:
    index = i.index(character)
    instruction = i[:index]
    parts = instruction.split()

    op = opcode_map[parts[0]]
    rest = "".join(parts[1:])

    binary = op + rest

    int_value = int(binary, 2)
    hex_instruction = hex(int_value)

    instruction_set.append(hex_instruction)

# Makes sure new instruction.txt file is created every time its ran
try:
    os.remove("instruction.txt")
except FileNotFoundError:
    pass
character = "x"
with open("instruction.txt", "w") as file:
    file.write("v3.0 hex words plain \n")
    for i in instruction_set:
        index = i.index(character)
        instruction = i[index+1:]
        file.write(instruction + " ") 

    