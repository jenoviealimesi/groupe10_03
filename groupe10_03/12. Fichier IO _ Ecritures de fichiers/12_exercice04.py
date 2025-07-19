notes = [float(x) for x in input("Entrez des notes : ").split()]
moyenne = sum(notes) / len(notes)

with open("Statistiques.txt", "w", encoding="utf-8") as f:
    f.write(f"Notes : {notes}\n")
    f.write(f"Moyenne : {moyenne:.2f}\n")

print("Statistiques sauvergardées dans 'statistiques.txt' .")