from playwright.sync_api import Page
from pages.rahul_shetty_page import RahulShettyLoginPage
from data.test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    USER_TYPE_TEACHER,
    USER_TYPE_STUDENT,
    ERROR_MESSAGE_INCORRECT
)


def test_login_with_valid_credentials(page: Page):
    """Test successful login with valid credentials."""
    login_page = RahulShettyLoginPage(page)
    login_page.navigate_to_login()
    login_page.login(VALID_USERNAME, VALID_PASSWORD, USER_TYPE_STUDENT, agree_terms=True)
    login_page.verify_login_success()


def test_login_with_invalid_credentials(page: Page):
    """Test login failure with invalid credentials."""
    login_page = RahulShettyLoginPage(page)
    login_page.navigate_to_login()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD, USER_TYPE_STUDENT, agree_terms=True)
    login_page.verify_error_message(ERROR_MESSAGE_INCORRECT)


def test_login_with_teacher_user_type(page: Page):
    """Test login with teacher user type."""
    login_page = RahulShettyLoginPage(page)
    login_page.navigate_to_login()
    login_page.login(VALID_USERNAME, VALID_PASSWORD, USER_TYPE_TEACHER, agree_terms=True)
    login_page.verify_login_success()
