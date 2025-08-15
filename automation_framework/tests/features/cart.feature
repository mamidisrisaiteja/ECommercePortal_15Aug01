@cart
Feature: Cart Module
  As a logged in user
  I want to add products to cart and view cart contents
  So that I can proceed with purchasing

  Background:
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"

  @cart @smoke
  Scenario: TC_CART_01 - View cart contents
    And click Add to cart
    And click cart icon
    Then verify page has text "Your Cart"
    And Cart page displays selected items
