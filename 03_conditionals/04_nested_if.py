age = 17
has_parent_permission = True

if age >= 13:
    if age >= 18:
        print("Access granted.")
    else:
        if has_parent_permission:
            print("Access granted with parental permission.")
        else:
            print("Ask a parent first.")
else:
    print("Too young.")
