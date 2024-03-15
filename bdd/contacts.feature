Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname>, <lastname>, <middlename>, <work>, <home> and <mobile>
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname   | lastname   | middlename  | work  | home | mobile |
    | firstname1  | lastname1  | middlename1 | 12341 | 2221 | 333331 |

Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Edit a contact
    Given a non-empty contact list
    Given a contact with <firstname>, <lastname>, <middlename>, <work>, <home> and <mobile>
    Given a random contact from the list
    When I edit the contact from the list
    Then the new contact list is equal to the old list with the modified contact

    Examples:
    | firstname   | lastname   | middlename  | work  | home | mobile |
    | firstname2  | lastname2  | middlename2 | 12342 | 2222 | 333332 |