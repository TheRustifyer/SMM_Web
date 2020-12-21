# Social Media Manager WebSite

Django based website for commercial product "Social Media Manager" for Zero Day Code.

# Why Django?

Because it's a powerful open-source web development tool made it in Python.
Python it's an awesome and productive language that is entirely focused on developers productivity,
so Django is made on same philosophy.

# Why REST-api?

It's the most common standard protocol nowadays, and this web page serves as a manager for the Desktop Commercial APP.
So one on the main goals was to separate the Desktop APP and the management of your account, so we decided to build a `REST api` on same language
that the original APP was created.

Another powerful reason it's the fact that with this structure, we need to authenticate the customers of our APP against an `MySql DB`,
which handles the data administrated and recolected by Django website about an user (remember, our APP auth an user against something, this case
against Django stored data on DB) which also allow us to encrypt (256 SHA) that data in a 2F process and retrieve that data and sent it to the D-App
in a strongest safer communication way that another availiable options.

So in order to get that data request, we need a safer protocol than plane HTTP, and there is... our APP gets data from external back-end in order to 
know what user is going to be the `Authenticated User`.
