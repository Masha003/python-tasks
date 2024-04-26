# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for num in numbers:
    if num % 2 == 0:
        print(num)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {
    "name": "John",
    "age": "13",
    "city": "Chisinau"
}

for key, value in person.items():
    print(key, value)

# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[1,2,3], [4,5,6], [7,8,9]]

for row in matrix:
    for el in row:
        print(f"Element: {el}")
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
numbers = list(range(15))
for num in numbers:
    print(num)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
animals = ["cat", "dog", "wolf"]
for i, el in enumerate(animals):
    print(f"Animal: {el}; Index: {i}")
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
students = ["Alice", "John", "Ema"]
uni_status = ["restanta", "pass", "restanta"]

for student, rest in  zip(students, uni_status):
    print(f"{student} - {rest}")
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = []
for i in range(1, 11):
    numbers.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
i = 0
while numbers[0] < 50:
    numbers[i] *= 2
    i += 1
    if i >= len(numbers):
        i = 0
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
perfect_squares = [i*i for i in range(1, 11)]
print(perfect_squares)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1, 11):
    print(f"7 * {i} = {i * 7}")
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
pairs_list = [[(i, j) for j in range(1, 6)] for i in range(1, 6)]
print(pairs_list)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for lst in pairs_list:
    for pair in lst:
        if(pair[0] < pair[1]):
            print(pair)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
random_numbers = [43, 3, 12, 10, 4, 5, 64]
i = 0
while i < len(random_numbers):
    if random_numbers[i] < 10:
        print(random_numbers[i])
        break
    i+=1
else:
    print("Nu există valori mai mari decât 10")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
square_len = int(input("Enter square dimenstion: "))
for i in range(square_len):
    for j in range(square_len):
        print("*", end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):
    for j in range(1, i+1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end="")
    print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
litere = "abcdefg"
for i in range(len(litere)):
    print(litere[i:])


# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
square_len = 8
for i in range(square_len):
    for j in range(square_len):
        if i % 2 == 0:
            print("+-", end="")
        else:
            print("-+", end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:

powers_of_three = [3**i for i in range(1, 6)]

for i in range(len(powers_of_three)):
    for j in range(i+1): 
        print(powers_of_three[j], end=' ')
    print()

for i in range(1, len(powers_of_three)):
    for j in range(i, len(powers_of_three)):
        print(powers_of_three[j], end=' ')
    print()

print(powers_of_three[-1])
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.