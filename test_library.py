from library import library_book_details

def test_library_book_details():
    expected_output = (
        "Book Id : 101\n"
        "Title : Python Programming\n"
        "Author : Jhon\n"
        "Year : 2020\n"
    )

    assert library_book_details(101, "Python Programming", "Jhon", 2020) == expected_output
