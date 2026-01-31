Feature: Google Search
  As a web user
  I want to search on Google
  So that I can find information

  Scenario: Verify Google Page Title
    Given I launch the browser
    When I open the Google homepage
    Then the page title should be "Google"
