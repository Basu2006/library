def library_book_details(book_id, title, author, year):
    return (
        f"Book Id : {book_id}\n"
        f"Title : {title}\n"
        f"Author : {author}\n"
        f"Year : {year}\n"
    )

if __name__ == "__main__":
    book_id = input("Enter the bookId")
    title = input("Enter the title: ")
    author = input("Enter author name: ")
    year = input("Enter the year: ")

    print(library_book_details(101,"Python Programming","Jhon", 2020))
