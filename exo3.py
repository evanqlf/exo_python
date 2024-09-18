def plus_grand_nombre(liste):
    max_nombre = liste[0]
    for nombre in liste:
        if nombre > max_nombre:
            max_nombre = nombre #58
    return max_nombre

print(plus_grand_nombre([3,58,11,21])) # Affiche 58
