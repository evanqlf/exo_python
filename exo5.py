def est_palindrome(mot):
    longeur = len(mot)
    for i in range(0, 4):
        if mot[i] != mot[-i]:
            return False
    return True

print(est_palindrome("radar")) # Affiche True
salut
