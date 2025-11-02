import os
import time

def p(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

p('welcome to trypassme! to start, what is your name?', delay=0.08)
name = input().lower()
clear()

p(f'hi {name}, now i will explain the game.', delay=0.08)
p('game rules:', delay=0.08)
p('objective: try to find the correct login and password', delay=0.08)
p('you can try as many times as you want', delay=0.06)
p('tips: think like a hacker and try different combinations', delay=0.06)
p('if you fail too much, i might start teasing you', delay=0.06)
p('try to guess as fast as possible to prove you are good at this\n', delay=0.08)
clear()

while True:
    p(f'{name}, are you ready to start the game? press enter to start')
    enter = input()

    if enter == '':
        p('game starting...')
        clear()

        max_attempts = 5
        login = 'user1'
        password = 'abc123'

        login_hints = [
            'first hint: the login starts with "u"',
            'second hint: it ends with "1"',
            'third hint: the login is "user1"'
        ]

        password_hints = [
            'first hint: password has letters followed by numbers',
            'second hint: starts with "a" and ends with "123"',
            'third hint: the password is "abc123"'
        ]

        p('here is your first hint for login:')
        p(login_hints[0], delay=0.06)
        clear()

        for i in range(1, max_attempts + 1):
            print(f'attempt {i}/{max_attempts}')
            user_login = input('try login: ').lower()

            if user_login == login:
                p(f'correct, the login is "{login}", now try the password')
                clear()
                break
            else:
                p('wrong login')
                if i < len(login_hints):
                    show_hint = input('do you want another hint? (y/n): ').lower()
                    if show_hint == 'y':
                        p(login_hints[i], delay=0.06)
        else:
            p(f'out of attempts! the login was: {login}')
            clear()

        p('here is your first hint for password:')
        p(password_hints[0], delay=0.06)
        clear()

        for j in range(1, max_attempts + 1):
            print(f'attempt {j}/{max_attempts}')
            user_password = input('try password: ').lower()

            if user_password == password:
                p(f'correct, the password is "{password}". you completed the game!')
                break
            else:
                p('wrong password')
                if j < len(password_hints):
                    show_hint = input('do you want another hint? (y/n): ').lower()
                    if show_hint == 'y':
                        p(password_hints[j], delay=0.06)

        p('do you want to play again? (y/n)')
        again = input().lower()
        clear()
        if again != 'y':
            p('thanks for playing! goodbye')
            break
