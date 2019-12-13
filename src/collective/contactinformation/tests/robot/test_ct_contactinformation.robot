# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.contactinformation -t test_contactinformation.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.contactinformation.testing.COLLECTIVE_CONTACTINFORMATION_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/collective/contactinformation/tests/robot/test_contactinformation.robot
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

Scenario: As a site administrator I can add a Contactinformation
  Given a logged-in site administrator
    and an add Contactinformation form
   When I type 'My Contactinformation' into the title field
    and I submit the form
   Then a Contactinformation with the title 'My Contactinformation' has been created

Scenario: As a site administrator I can view a Contactinformation
  Given a logged-in site administrator
    and a Contactinformation 'My Contactinformation'
   When I go to the Contactinformation view
   Then I can see the Contactinformation title 'My Contactinformation'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Contactinformation form
  Go To  ${PLONE_URL}/++add++Contactinformation

a Contactinformation 'My Contactinformation'
  Create content  type=Contactinformation  id=my-contactinformation  title=My Contactinformation

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Contactinformation view
  Go To  ${PLONE_URL}/my-contactinformation
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Contactinformation with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Contactinformation title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
