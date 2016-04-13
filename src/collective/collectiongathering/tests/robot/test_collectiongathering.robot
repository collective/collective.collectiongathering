# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.collectiongathering -t test_collectiongathering.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.collectiongathering.testing.COLLECTIVE_COLLECTIONGATHERING_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_collectiongathering.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a CollectionGathering
  Given a logged-in site administrator
    and an add collectiongathering form
   When I type 'My CollectionGathering' into the title field
    and I submit the form
   Then a collectiongathering with the title 'My CollectionGathering' has been created

Scenario: As a site administrator I can view a CollectionGathering
  Given a logged-in site administrator
    and a collectiongathering 'My CollectionGathering'
   When I go to the collectiongathering view
   Then I can see the collectiongathering title 'My CollectionGathering'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add collectiongathering form
  Go To  ${PLONE_URL}/++add++CollectionGathering

a collectiongathering 'My CollectionGathering'
  Create content  type=CollectionGathering  id=my-collectiongathering  title=My CollectionGathering


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the collectiongathering view
  Go To  ${PLONE_URL}/my-collectiongathering
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a collectiongathering with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the collectiongathering title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
