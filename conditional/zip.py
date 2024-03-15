job=["police officer","Eye surgeon",'Snake Handler']

salaries=[28000,42500,84250]

age=[28,32,45]

for role in zip(job,salaries,age):
  print(f'The {role[0]} job pays {role[1]} annually and his age {role[2]}')

name="suganya"
print(name[len(name)::-1])

print(name[::-1])
print(name.split())

lis=[]
for i in name:
  lis.append(i)

print(lis)