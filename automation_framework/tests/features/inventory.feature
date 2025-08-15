@inventory
Feature: Inventory Module
  As a logged in user
  I want to view and interact with products
  So that I can browse the inventory

  Background:
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"

  @inventory @smoke
  Scenario: TC_INV_01 - Verify product listing
    Then verify page has text "Products"
    And verify page has text "Add to cart"

  @inventory @sorting
  Scenario: TC_INV_02 - Sort products by Name (A–Z)
    And click Sort Icon
    And click Sort the Products by Name A–Z
    Then all the products must be sorted from A to Z
