@auth
Feature: Authentication Module
  As a user
  I want to login to the application
  So that I can access the inventory

  Background:
    Given user is on Login Page

  @auth @smoke
  Scenario: TC_AUTH_01 - Login with Valid credentials
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"

  @auth @negative
  Scenario: TC_AUTH_02 - Login with invalid credentials
    When user enters user name as "standard_use" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Login"
    And Login Button should be still displayed
