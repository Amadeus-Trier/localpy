fin = open("W:/Creative Cloud Files/Intern Unterlagen/Schulungsmaterial/Python/Pgrogramierübungen/app/tutorial/speisekarte-test/speise.txt", "rt", encoding="utf-8")
fout = open("W:/Creative Cloud Files/Intern Unterlagen/Schulungsmaterial/Python/Pgrogramierübungen/app/tutorial/speisekarte-test/speiseneu.txt", "wt", encoding="utf-8")
for line in fin:
    fout.write(line.replace("Oliven", ",Oliven 2, 3, 4, 2, 3wefwefwefwefwe")
    .replace("Soße", "Soße 6, 7, 4")
    .replace("Käse", "Käse 7, 9, dsfsdfdsfdsfd3, b")
    .replace("Sahnesauce", "Sahnesauce a, b, c, d")
    .replace("Pide", "Pide a, 4, 5, 6")
    .replace("Mozzarella", "Mozzarella 7, 5, h, j")
    .replace("Weichkäse", "Weichkäse s, d, f, k, l")
    .replace("Schinken", "Schinken b, n, m, k, 9, 7")
    .replace("Ei", "Ei 7, 8, 2")
    .replace("Krabben", "Krabben 3, 7, 8, 2")
    .replace("Thunfisch", "Thunfisch ü, ä, l"))
fin.close()
fout.close()


