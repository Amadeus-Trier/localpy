#--------------------------------------------------------------------------------------------------#
#---    Projekt:    Speisehelpy		                                                            ---#
#---    Author:     Amadeus Werbung | Deine Fullservice Werbe- & Marketingagentur in Trier      ---#
#---    Version:    0.4                                                                         ---#
#---    Date:       2022-06-03                                                                  ---#
#---    last mod:   2022-06-28                                                                  ---#
#--------------------------------------------------------------------------------------------------#
fin = open("/Users/amadeus/Creative Cloud Files/localpy/SpeiseHelpi/in-out/speisekarte.txt", "rt")
fout = open("/Users/amadeus/Creative Cloud Files/localpy/SpeiseHelpi/in-out/speisekarte-export .txt", "wt",)
for line in fin:
    fout.write(line.replace("Brot", "Brot a")
	.replace("Brot", "Brot a")
	.replace("Soße", "Soße g")
	.replace("Käse", "Käse g")
	.replace("Sahnesoße", "Sahnesoße g")
	.replace("scharfe Soße", "scharfe Soße g")
	.replace("Pizza", "Pizza a")
	.replace("Pide", "Pide a")
	.replace("Chicken Nuggets", "Chicken Nuggets 4, a, c, g, i")
	.replace("Tsatziki", "Tsatziki g")
	.replace("Zigarrenbörek", "Zigarrenbörek g")
	.replace("Weinblätter", "Weinblätter a, g, m")
	.replace("Schinken", "Schinken 2, 5, i, j")
	.replace("Thunfisch", "Thunfisch d")
	.replace("Krabben", "Krabben b")
	.replace("Weichkäse", "Weichkäse g")
	.replace("Salami", "Salami 2, 5")
	.replace("Oliven", "Oliven 7")
	.replace("Ei", "Ei c")
	.replace("Dressing", "Dressing g")
	.replace("Tomatensoße", "Tomatensoße i")
	.replace("Peperoniwurst", "Peperoniwurst 3, 5")
	.replace("Hähnchenschinken", "Hähnchenschinken 5, i, j")
	.replace("Knoblauchwurst", "Knoblauchwurst 5, 6")
	.replace("Putenfleisch", "Putenfleisch 6, a, f, j")
	.replace("Shrimps", "Shrimps b")
	.replace("Putenschnitzel", "Putenschnitzel 2, 5, a, c")
	.replace("Jägersoße", "Jägersoße 2, 6, a, g, i")
	.replace("Zigeunersoße", "Zigeunersoße 6, a, g, i")
	.replace("Rahmsoße", "Rahmsoße g"))
fin.close()
fout.close()


