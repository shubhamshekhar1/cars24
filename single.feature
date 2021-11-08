Feature: Cars24 AU Functionality

    #Scenario: clicking on show me
      #  Given visit url "https://stage-consumer-web-au.qac24svc.dev/au"
        #Then check title
        ##When Passing make value "FORD" and "RANGER"
     #   Then clicking on show me

    #Scenario: Selecting one car
      #  Given User clicks on one car
     #   When User clicks on get started

    #Scenario: clicking find a car
        #Given visit url "https://stage-consumer-web-au.qac24svc.dev/au"
        #When User clicks on find a car
       # Then User clicks on one car

    #Scenario: Searching specific car
     #   Given visit url "https://stage-consumer-web-au.qac24svc.dev/au"
      #  When Passing make value "FORD" and "RANGER"



    Scenario: Login and booking a car
        Given visit url "https://www.cars24.com/au" and login with facebook
        When clicking on show me and clicks on one car