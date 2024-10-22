#3ASSIGNMENT3

#book class and the functions
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.purchase_count = 0

    def purchase(self):
        self.purchase_count += 1

#EBookReader class and the functions
class EBookReader:
    def __init__(self):
        self.books = []

#function to add a book to the system
    def add_book(self, book):
        self.books.append(book)

#function to display genres
    def display_available_genres(self):
        genres = set([book.genre for book in self.books])
        print("Available genres:", ", ".join(genres))

#function to filter books by selected genre
    def filter_by_genre(self, genre):
        books_in_genre = [book for book in self.books if book.genre == genre]
        if books_in_genre:
            print(f"Books in genre '{genre}':")
            for book in books_in_genre:
                print(f"  - {book.title} by {book.author}")
        else:
            print(f"No books found in genre '{genre}'")

#function to track how many times a book has been purchased
    def track_purchases(self, title):
        for book in self.books:
            if book.title == title:
                book.purchase()
                print(f"Book '{title}' has been purchased {book.purchase_count} time(s).")
                return
        print(f"Book '{title}' not found.")

#function to display the books
    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Purchases: {book.purchase_count}")

#function to display the top 3 most purchased books
    def top_purchased_books(self):
        top_books = sorted(self.books, key=lambda book: book.purchase_count, reverse=True)[:3]
        if top_books:
            print("Top Purchased Books:")
            for book in top_books:
                print(f"  - {book.title} with {book.purchase_count} purchase(s)")
        else:
            print("No books have been purchased yet.")

#function to search books by author 
    def search_by_author(self, author):
        result = [book for book in self.books if book.author == author]
        if result:
            print(f"Books by '{author}':")
            for book in result:
                print(f"  - {book.title} ({book.genre})")
        else:
            print(f"No books found by author '{author}'")

#function to search books by title 
    def search_by_title(self, title):

        self.books.sort(key=lambda book: book.title)
        low, high = 0, len(self.books) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.books[mid].title == title:
                print(f"Found Book: {self.books[mid].title} by {self.books[mid].author}")
                return self.books[mid]
            elif self.books[mid].title < title:
                low = mid + 1
            else:
                high = mid - 1
        print(f"Book '{title}' not found.")
        return None

#function to save purchase data to a file
    def save_purchases(self, filename):
        with open(filename, 'w') as f:
            for book in self.books:
                f.write(f"{book.title},{book.purchase_count}\n")
        print(f"Purchases saved to '{filename}'.")

#function to load purchase data from a file
    def load_purchases(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    title, count = line.strip().split(',')
                    for book in self.books:
                        if book.title == title:
                            book.purchase_count = int(count)
            print(f"Purchases loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


if __name__ == "__main__":
    #creating an EBookReader instance
    reader = EBookReader()

    #books in the program
    reader.add_book(Book("Edge of Survival: A Post-Apocalyptic", "Kyla Stone", "Fiction"))
    reader.add_book(Book("The Wife Upstairs", "Freida McFadden", "Drama"))
    reader.add_book(Book("Mercy Falls", " William Kent Krueger", "Science Fiction"))
    reader.add_book(Book("Basketball & More", "LeBron James", "Sport"))

    #display all genres
    reader.display_available_genres()

    #filter books by genre
    reader.filter_by_genre("Fiction")

    #book purchases
    reader.track_purchases("Basketball & More")
    reader.track_purchases("Mercy Falls")
    reader.track_purchases("The Wife Upstairs")

    #display all books and their purchase counts
    print("\nAll Books:")
    reader.display_books()

    #top 3 purchased books
    print("\nTop 3 Purchased Books:")
    reader.top_purchased_books()

    #books by a specific author
    print("\nSearch by Author:")
    reader.search_by_author("Kyla Stone")

    #book by title
    print("\nSearch by Title:")
    reader.search_by_title("Basketball & More")

    #saving purchases to a file
    reader.save_purchases("purchase.txt")

    #saving purchases from a file
    reader.load_purchases("purchase.txt")
