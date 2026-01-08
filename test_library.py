def library_book_details(book_id, title, author, year):
    return (
        f"Book Id : {book_id}\n"
        f"Title : {title}\n"
        f"Author : {author}\n"
        f"Year : {year}\n"
    )


    assert library_book_details(101, "Python Programming", "Jhon", 2020) == expected_output
    
