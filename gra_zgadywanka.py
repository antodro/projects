#gra zgadywanka

secret_world = 'dron'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_world and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Print your guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('You lost')
else:
    print('Congratulations, right guess')
