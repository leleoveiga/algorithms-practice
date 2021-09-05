

# append - Append string  to the end of .
# delete - Delete the last  characters of .
# print - Print the  character of .
# undo - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.

q = int(input())
s = ""

last_commands = []

for i in range(q):
    command = input().split()
    # print("command: ", command)
    if len(command) > 1:
        if command[0] == "1":
            s += (command[1])
            last_commands.append(["1", command[1]])
        elif command[0] == "2":
            removed = s[-int(command[1])::]
            s = s[0:-int(command[1])]
            # print(s)
            last_commands.append(["2", removed])
            # print(removed)
        elif command[0] == "3":
            # print(command)
            res = s[int(command[1])-1] if int(command[1]) > 0 else ""
            print(res)
    
    elif command[0] == "4":
        # print("entrouaqui")
        if len(last_commands) > 0:
            command = last_commands[-1]
            # print("last command", command)
            if command[0] == "2":
                s += (command[1])
                last_commands.pop()
            elif command[0] == "1":
                removed = s[-len(command[1])::]
                s = s[0:-len(command[1])]
                # print(s)
                last_commands.pop()
                # print(removed)
        else:
            continue
    # print("string:", s)
    # print("last commands:", last_commands)