if __name__ == '__main__':


    student_list = ['Supreeth','Nishad Sir','Sharma','Singh','Sanketh']
    print(student_list)
    user_name = str(input('username:'))
    password   = str(input('password:'))
    if (user_name  in student_list) and (password == 'admin'):
        print(user_name , " login succesfull")
    else:
        print("login failed")

