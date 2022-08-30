link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
	browser.get(link)
	assert browser.find_element("class name", "btn-add-to-basket"), "button not found"
