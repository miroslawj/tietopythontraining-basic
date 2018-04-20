number_of_files = int(input())
file_access_rights = dict()

OPERATIONS_DICT = {
        'read': 'R',
        'write': 'W',
        'execute': 'X'
    }

for _ in range(number_of_files):
    file, *access_rights = input().split()
    file_access_rights[file] = access_rights

number_of_file_operations = int(input())
for _ in range(number_of_file_operations):
    access_denied = True
    file_operation = input().split(' ')
    if file_operation[0] in OPERATIONS_DICT.keys():
        file_operation[0] = OPERATIONS_DICT[file_operation[0]]

    if file_operation[1] in file_access_rights:
        for allowed_access in file_access_rights[file_operation[1]]:
            if file_operation[0] == allowed_access:
                access_denied = False
    if access_denied:
        print("Access denied")
    else:
        print("OK")
