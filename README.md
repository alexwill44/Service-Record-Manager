# service-record-manager 

Deployed and live at: https://service-record-keeper.herokuapp.com/
Feel free to play around - the Tech privalage for a test user are:

username: testnician
password: tester88

please note at the time of deployment (12/1/21) all databases are mostly empty

A management system for tracking parts and service associated with specific motorcycles (though the application could easily be built out for any repair facility). 

service-record-manager (Record Keeper) was built using Django Python and Postgres SQL.

In order to run this app on your own machine you will need to install the following dependancies:
    - django cripsy forms v1.13.0
    - django sass processing v1.1 

All other libraries are accessed via hardcoded CDN: 
    - TinyMCE 
    - Bootstrap 
    - jQuery ( with popper )
    - Font Awesome

Version 1: 

    The concect behind this application is to provide a portal for commiunication between repair shops and customers. 
    
    The business side: 
        - The business side is meant to be primarily viewed on a computer
        - Allows for databasing of technicians and customers, thier associated vehicals, repairs and reccomendations assciated with these vehicals, the parts assciated with those repairs. 
        - There is functionality for real time status updates on vehicals that are currently in the shop. 

    The customer side:
        - This is much more streamlined view of the application that will be viewable on mobile devices. 
        - The customer will be able to see thier vehicals and associated service records 
        - The customer will also be able to view the real time status of thier vehicals repair. 

    
Version 2: 

    There is a lot of functional to come: 
        - A search function for parts that is connected to a parts api / database
        - The ability for the tech / admin to make certain records private from the customer 
        - The ability to add technicians notes to repair orders rather than just update the text of the original repair order (in order to perserve customer notes etc.) 
        - There is even more on the the way not the least of which is a better color scheme and more styling 
        
** (please keep in mind version 1 of this app was build is arond a week by one person) **

Wireframes : 

 ![wireframe](https://i.imgur.com/Y0wlqCQ.jpg)