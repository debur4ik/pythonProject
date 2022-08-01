import pandas as pd
films_df = pd.read_csv("films.csv",index_col=[0])
pd.set_option('display.max_columns', 800)
pd.set_option('display.width', 1500)
print(films_df)
print()

print('What do you want to do. Make your choose:')
print('Read note - input 1')
print('Print note  - input 2')
print('Get films with the highest rating - input 3')
print('Get films with the lowest rating - input 4')
print('Get average rating among all films - input 5')
doing = int(input())
print()
if doing==1:
    print ('What films Note do you want to read. Print number of film, if nothing - press"n"')
    s=input()
    if s!='n':
        print(films_df['Note'][int(s)])
    print()
if doing == 2:
    print('What films Note do you want to print to console. Print number of film, if nothing - press"n"')
    s = input()
    if s != 'n':
        print(films_df['Note'][int(s)])
    print()
if doing == 3:
    sorted_df = films_df.sort_values(by='Rating',ascending = False)
    print(sorted_df.head())
if doing == 4:
    sorted_df = films_df.sort_values(by='Rating')
    print(sorted_df.head())
if doing == 5:
    print('average rating = ', films_df['Rating'].mean())