############### Partie 1 ####################
# class BookNode :
class BookNode:
    def __init__(self, title, author, isbn, copies, genre=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.genre = genre
        self.next = None

# cLassCatalog :

class BookCatalog:
   
    def __init__(self):
        self.head = None
       


    def addBook(self, title, author, isbn, copies, genre):
        new_book = BookNode(title, author, isbn, copies, genre)
        # si le catalog est vide :
        if self.head is None:
            self.head = new_book
        # sinon on cherche le dernier livre dans la liste et on rajoute le livre juste à la fin
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_book
           
   

   
    def removeBook(self, isbn):
        # si le catalog est vide:
        if self.head is None:
            return
        # si le catalog continet un seul livre (le livre qu'on doit supprimer)
        if self.head.isbn == isbn:
            self.head = self.head.next
            return
        current = self.head
       
        # Sinon on parcours le catalog jusqu'à trouvé le livre à supprimer
        while current.next is not None:
            if current.next.isbn == isbn:
                current.next = current.next.next
                return
            current = current.next

    def searchBook(self, query):
        results = []
        current = self.head
        # on parcours le catalogue, si on trouve le titre ou l'auteur contient la query on renvoie le livre
        while current is not None:
            if query in current.title or query in current.author or query in current.genre:
                results.append((current.title, current.author, current.isbn, current.copies))
            current = current.next
        return results
   
    # cette fonction fait la meme chose que la fonction searchBook mais sur le genre elle sera utile dans la 2éme partie
    def searchGenre(self, genre):
        result = []
        curr_book = self.head
        while curr_book is not None:
            if genre in curr_book.genre :
                result.append((curr_book.title, curr_book.author, curr_book.isbn, curr_book.copies))
            curr_book = curr_book.next
        return result

   
###################### Partie2 ########################

# classe Patron
class Patron:
    def __init__(self, name, preferredGenres):
        self.name = name
        self.preferredGenres = preferredGenres
        self.readingHistory = []
   
    # cette finction permet de rajouter un livre dans l'historique de patron (elle aide à tester la fonction recommendBooks)
    def add_to_history(self,book):
        self.readingHistory.append(book)

# Foction recommandBooks fait appel à al fonction récursive recommender
def recommendBooks(patron, catalog):
    recommended_books = []
    recommender(patron, catalog, recommended_books, patron.preferredGenres)
    return recommended_books

def recommender(patron, catalog, recommended_books, genres):
    # si le liste des genres est vide :
    if not genres:
        return
    # Pour chaque livre dans le catalogue on vérifie si il répond aux conditions
    for book in catalog.searchGenre(genres[0]):
        if book[0] not in [rbook[0] for rbook in recommended_books] and book[0] not in [rbook.title for rbook in patron.readingHistory]:
            recommended_books.append(book[0])
    # on passe au genre suivant dans la liste en appel récursive:
    recommender(patron, catalog, recommended_books, genres[1:])
   
# test :
# creer un catalogue de livres et ajouter des livres
catalog = BookCatalog ()
catalog . addBook ( "Natural Language Processing " ,"Steven Bird, Ewan Klein, and Edward Loper" , "0596516495" , 2 , "NLP" )
catalog . addBook ( "Python for Data Analysis","Wes McKinney","1449319793",1,"Data Science" )
catalog . addBook ( "Data Structures and Algorithms in Python","Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser " ,"1118290275" , 3 , " Algorithms " )
catalog . addBook ( "The Catcher in the Rye" , " J.D.Salinger" , " 0316769177 " ,2 , " Fiction " )
catalog . addBook ( "To Kill a Mockingbird","Harper Lee" ,"0446310786",1 , "Fiction")

# creer un usager avec des genres preferes
patron = Patron ( "Alice" , [ "NLP" , "Fiction" ])
nlp = BookNode( "Natural Language Processing " ,"Steven Bird, Ewan Klein, and Edward Loper" , "0596516495" , 2 , "NLP" )
# ajouter le livre nlp à l'historique des livres:
patron.add_to_history(nlp)

# recommander des livres au visiteur en fonction de ses genres preferes
