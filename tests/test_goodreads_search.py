from pytest_bdd import parsers, scenarios, given, when, then
from pages.goodreads_page import GoodReadsPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage

goodreads_page = GoodReadsPage()
login_page = LoginPage()
search_page = SearchPage()

scenarios('../features/search.feature')


@given("User is on 'Goodreads' page")
def goodreadsPage():
    goodreads_page.load_page()

@when("User clicks on 'Log In' button at Goodreads page")
def goodreadsPage_login():
    goodreads_page.click_login_lbl()


@then(parsers.parse("User enters '{username}' and '{password}'"))
def loginPage_userpass(username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)


@then("User clicks on 'Log In' button at Login page")
def loginPage_login():
    login_page.click_login_btn()


@then(parsers.parse("User searches for a book with '{name_book}'"))
def searchPage_search_book(name_book):
    search_page.search_a_book(name_book)


@then("User can mark it for reading")
def searchPage_mark_reading():
    search_page.mark_a_reading()
