name1=input("Enter your name:").lower()
name2=input("Enter your name2:").lower()

full_name=name1+name2

t=full_name.count('t')
r=full_name.count('r')
u=full_name.count('u')
e=full_name.count('e')
true=t+r+u+e

l=full_name.count('l')
o=full_name.count('o')
v=full_name.count('v')
e=full_name.count('e')
love=l+o+v+e

love_score=str(true)+str(love)

print(f"your Love Percent is {love_score}%")
