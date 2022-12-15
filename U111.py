import csv

bok = [["книга", "автор", "год выпуска"],
       ["To Kill a Mockingbird", "Harper Lee", "1960"],
       ["A Brief History of Time", "Stephen Hawking", "1988"],
       ["The Great Gatsby", "F. Scott Fitzgerald", "1922"],
       ["The Man Who Mistook His Wife for a Hat", "Oliver Sacks", "1985"],
       ["Pride and Prejudice", "Jan Austen", "1813"]
       ]

with open("Books.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(
        bok
    )