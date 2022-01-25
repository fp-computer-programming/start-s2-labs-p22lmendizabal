#author: LM 1/24/22
last_intitial = ["B.", "D.", "H.", "E.", "G.", "G.", "H.", "R.", "M.", "L.", "I.", "I.", "N.", "N.", "O.", "P.", "P.", "X.", "T.", "S.", "S.", "P."]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
#using for loop to iterate thorugh the rows vaiable
for row in rows:
    #nested forloop to go through string 
    for index, value in enumerate(row):
        #adding value and first last initial element then deleting it
        row[index] = "{0} {1}".format(value, last_intitial[0])
        del last_intitial[0]
print(rows)
