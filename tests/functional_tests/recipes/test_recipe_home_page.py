import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import RecipeBaseFunctionalTest
from unittest.mock import patch


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body') 
        self.assertIn('No recipes found here 😅', body.text)

    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch()

        title_needed = 'This is what I needed'
        recipes[0].title = title_needed
        recipes[0].save()

        #user open page
        self.browser.get(self.live_server_url)

        #see a camp of search with text "Search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe"]'
            )
        
        #click on input and text the term of search
        #for find recipe with this title wished
        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)
        
        # The user sees what they looking for
        self.assertIn(
            title_needed,
            self.browser.find_element(By.CLASS_NAME,'main-content-list').text,
        )

    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_home_page_pagination(self):
        self.make_recipe_in_batch()

        #user open page
        self.browser.get(self.live_server_url)

        # Sees what have one pagination and click on page 2
        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]'
        )

        page2.click()

        # Sees what have 2 more recipes on page 2
        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe')),
            2
        )