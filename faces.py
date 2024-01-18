def faces():
    faces_statement = input("enter a statement here: ")
    new_statement = faces_statement.replace(":)", "🙂")
    new_statement2 = new_statement.replace(":(", "🙁")
    print(new_statement2)

faces() 