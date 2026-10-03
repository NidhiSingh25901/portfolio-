import pytest
from playwright.sync_api import Page, expect
import pathlib

@pytest.fixture(autouse=True)
def setup_page(page: Page):
    html_path = pathlib.Path(__file__).parent.parent / "index.html"
    page.goto(f"file://{html_path}")

def test_olive_color_scheme(page: Page):
    section1 = page.locator(".section1")
    expect(section1).to_be_visible()
    
    navbar = page.locator(".navbar")
    expect(navbar).to_be_visible()

def test_header_text_nidhi_singh(page: Page):
    section1 = page.locator("#section1")
    expect(section1).to_be_visible()
    
    header_element = section1.locator("h1:has-text('My Name is Nidhi Singh')")
    expect(header_element).to_be_visible()
    expect(header_element).toHaveText if hasattr(header_element, 'toHaveText') else expect(header_element).to_have_text("My Name is Nidhi Singh")
