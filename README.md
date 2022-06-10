# About

**Supercazzola** which in italian means nonsense; "a phrase devoid of logical sense composed of a random set of real and non-existent words". Let's skip the pretentious talk about wine and just focus on really good wine!
For us it is just about good, non pretentious low intervention wines from our friends in Italy and South Africa. 
They may be the sons and daughters from the more classic wineries or new vinyard experimenting and just doing their own thing. Either way, they are making their own paths and pushing wine making into the future, experimenting on their own and providing us with outstanding wines. As long as we find it great, we are proud to be your local wine distributor in Southern Sweden. 
Because we assure you - you will come back for more. 

# UX

The five elements of UX: 

## Strategy

#### Business Goal

Become the biggest importer of natural wine in Sweden. Targeting the people loving wine but may not necessarily know so much about it. 

#### Target Audience

- Age: 21-55
- Informed as well as non-informed winelovers
- Most likely to live in or close to cities 
- Interests: Music, design/art, going out-ers (bars/restaurants), books and independent magazines
- Persona: Curious, traveller, informed, openminded, likes spending money on the good stuff in life

Our target audience will be looking for a reliable source to find the best wine in a userfriendly and secure web application:
- Information about wine
- A product page with detailed information about each wine bottle 
- Be able to search for a product they are looking for
- User account information that stores their data upon return in the future
- Sign up to newsletters and links to external social media accounts

#### Tone of Voice

We'll share informational and "educational" content in a witty, non pretentious way - not taking for granted that our community know it all.  

#### Business Model

B2C (Buiness to Customer) - A carefully selected e-commerce of imported natural wines to sell to winelovers over 21 years old in Sweden. Selection will mainly come from South Africa and Italy, seeing the gap in the market of South African low intervention wines, will especially make Supercazzola a name for itself. 
B2B (Business to business) - A big part of Supercazzolas business model will be to distribute wine to bars and restaurants in the southern part of Sweden. Wine events, wine tastings and pop-up events will have our presence. 

Since we offer alcoholic beverage we will not have sales nor discounts on our products, but will rather make sure our community have fun at our accessable events and wine tastings, which will be shared by newsletter to those who sign up.


### Marketing 

**Mailchimp**
Our community will be reached through Newsletters in which users can sign up to from the `footer` of the site with embedded Mailchimp. Mailchimp will store the email addresses and with time we will organise the users into groups depending on what they want from us: Will it be updates regarding new wines coming in, or eventseekers or those that are most interested in reading about wine an a witty informative way. We will shape email groups after their preference.

**Instagram**
Our target audience is mostily on Instagram and that is where we will meet them - adding posts ourselves and resharing posts from our community (if they fit our brand image) on a close to daily basis in order to rank high in our followers post stream. 

**Facebook Business Page**
In the footer users will find a link to our [Facebook Business page](https://www.facebook.com/supercazzolawine/) where we will marketing most of our wine events and be avaialble to chat to our customers if they have any questions.

![Facebook Business](/misc/readme_images/facebook_business.png)

![Facebook mobile](/misc/readme_images/facebook_mobile.png.png)

**SEO**
I started with a Google analysis and realised people frequently ask what natural wine is. Which I believe is a valid quiestion seeing it is relatively new on the market - So I wanted to include the question in a h2 header and a short answer to what it is in the homepage to increase SEO.
In the Abous Us section there are also a lot of keywords included, such as: *Supercazzola* (our brand!), *wine, good wine, low intervention wine, Italy, South Africa, wineries, vineyard, wine making, local wine distributor, Southern Sweden*

META --------


### User Stories

#### Epic: Login/Register

1. As a user I want to register an account so that I can store delivery information for quick and easy checkout
2. As a returning user I want to login to my account so that I can manage my account
2. As a returning user I want to login to my account so that I can view order history
3. As a returning user I want to login to my account so that I can add items I like to a favourite list
4. As a returning user I want to logout from my account so that I know it is secure


#### Epic: Shop/Products

5. As a store owner I want to add products to site so that I can increase sales
6. As a store owner I want to edit products on site so that I can update products
7. As a store owner I want to delete products to site so that I can manage products that are no longer available for sale
8. As a user I want to view all products available to I can see what the offering is
9. As a user I want to search for products so that I can easily navigate around on the site
10. As a user I want to filter amongst the products so that I can easily find what is in my interest
11. As a user I want to click on a product so I can see more details about it
12. As a user I want to be able to see description, price, origin and color of wine so I know what I am buying
13. As a user I want to add products to a shopping bag so that I can browse around before I checkout
14. As a user I want to add quantity from product page so that I easily can buy more than one 

#### Epic: Payment/Checkout

15. As a user I want to see a summary of my bag so that I know what I am eventually paying for
16. As a user I want to see the shipping fee so that I know the total price
17. As a user I want to be able to change quanities in the bag so that I can edit the bag in case I have changed my mind or I see the total cost is too high
18. As a user I want to fill out my delivery information so that I can control where my order is being sent
19. As a user I want to securely pay for my items so that my card details are safe
20. As a user I want to be notified when an order has gone through so that I know it was successful 
21. As a returning user I want to store my shipping information so that I quickly can checkout next time
22. As a store owner I want to see an order summary of confirmed purchase so that I can proceed with delivery of products

#### Epic: Site

23. As a user I want to read about the company when I land on the page so I can find out about what they do and who they are
24. As a user I want to sign up for emails so that I can stay up to date with events/wine tastings and other news
25. As a user I want to see Social Media links so that I easily can follow and be part of their community
26. As a user I want to see a navigation menu so that I can easily navigate on the site
27. As a user I want to be notified by messages when on the site so I know about alerts/errors/success
28. As a user I want to be emailed an order confirmation so that I can keep it as a reciept of successful order
29. As a bar/restaurant owner I want see contact information so that I can potentially buy your wine for my business

#### Epic: Marketing

-------

## Scope

To achieve the user & business goals, the following features will be included in this project:

- Responsive navbar
- Landing page with About Us section and links to relevant pages such Shop and Contact
- Shop page, that displays all products available with the option to search for a specific product or filter
- Register/login feature so that users can create an account
- Contact for for business that wants to reach out for potential collaborations
- My Account page, for logged in users to update their details and view their previous orders and wishlist products
- Footer with links to social media accounts as well as a newsletter signup


## Structure

### Data Models

Following models have been created for this project:

Profile App:
- User - Django AllAuth user account that is being create upon registration
- User Profile - Storing users contact information, order history and wishlist items
Product App: 
- Product - Stores product image, details, price and description
- Category - Linked to product
Checkout App:
- Order - Creates an instance of an order when succesfully progressed with billing/shipping information, a foreign key to the UserProfile and users details. Also includes information of payment, the stripe PID and basket contents.
- OrderItem - Each orderline of the total Order that includes: product, quantity and price
Wishlist App:
- Wishlist - Stores all users liked item
- WishlistItem - Allowing users to add individual items to their wishlist

### Database Schema

![Database Schema](/misc/readme_images/database_schema.png)


## Skeleton

## Wireframes
The wiresframes differs slightly from the end result, but the main idea is still very much there. A consistent page layout on most pages for a no-surprising user experience with the focus on straight-to-the-point and product sales. 
Some content is hidden on smaller devices to ensure the mobilescreen gives the user the most important and relevant information. 

![Alert Box](/misc/readme_images/Alertbox.png)

![Home](/misc/readme_images/Home.png)

![Shop](/misc/readme_images/Shop.png)

![Product Detail](/misc/readme_images/Product_detail.png)

![Bag](/misc/readme_images/Bag.png)

![Checkout](/misc/readme_images/Checkout_pay.png)

![Thanks for shopping](/misc/readme_images/Thanks_for_shopping.png)



## Surface

### UX Design

Use a clean layout and a proven e-commerce structure for a smooth navigation on the site. 
Research amongst competitors show quite pale choice of colors and the few that caught my eye had a stronger visual approach and therefor decided to go with a strong shade of yellow (quite a characteristic color of natural wine capsules, which you sometime see made of rubber), also the color of the sun and without sun no wine. Black and white for simplicity and generated complimentary colors through [Colormind.io](http://colormind.io/) to set the contrasting colors for strong visual identity.
This also supports by our target audience being interested in art and design, looking for that different wine to stand out amongst their friends. 
The age of target audience is proven to spend most of their time on the phone - therefor a fully responsive website on smaller devices is crucial. 

### Font

I wanted to create an artsy look of the logo and first went for a grafitti style font. When doing research of font pairings I found the Google Font "Permanent Marker" matched with "Overpass Regular" on [Heyreliable.com](https://heyreliable.com/) and knew immediately that I wanted these two - one for an artsy "not giving a f"-look that suits the brand image and tone of voice, and one for a clean and neat read.




Color: #DDC445







## Planning / Agile Management
I used the Github kanban board to create issues and user stories in the early development stages of this project and moved them across the board as I progressed from TODO -> In Progress -> Done. 
Link to [Github Project here](https://github.com/viktoriamahrberg/supercazzola/projects/1)
Userstories were organised in "must-have", "could-have" or "should-have" labels in order to make prioritization of the scope easier. 
I added userstories as I went on and realised what I want to add to the site in the future and have kept them in Backlog for further assessment after this project has been handed in.

I set up the project into 3 sprints:

*Sprint 1* (23-25th May):
- Researching competitors
- Planning
- User Stories 
- UX / designing the site
- Set up wireframes
- Database schema

*Sprint 2* (25 May - 8th June):
- Building the site

*Sprint 3* (8 May - 13th June):
- Readme.md
- Tweaks
- Testing
- Responsiveness 




## Features to be implemented in future:

- The legal age to buy alcohol is above 21 so a feature to implement in the future would be to link Bank ID for users to log in and confirm their age.

- Klarna for seamless checkout, as well as remove test mode for Stripe




# Technology used

- **Python:**
    - Python modules used:      
        - asgiref==3.5.2
        - boto3==1.24.4
        - botocore==1.27.4
        - dj-database-url==0.5.0
        - Django==3.2
        - django-allauth==0.41.0
        - django-countries==7.2.1
        - django-crispy-forms==1.14.0
        - django-storages==1.12.3
        - gunicorn==20.1.0
        - jmespath==1.0.0
        - oauthlib==3.2.0
        - Pillow==9.1.1
        - psycopg2-binary==2.9.3
        - python3-openid==3.2.0
        - pytz==2022.1
        - requests-oauthlib==1.3.1
        - s3transfer==0.6.0
        - sqlparse==0.4.2
        - stripe==3.2.0

- **[Bootstrap 4.6 boilerplate]**(https://getbootstrap.com/docs/4.6/getting-started/introduction/) 
- **HTML**
- **CSS**
- **JavaScript**
- **Jquery**
- **Crispyforms** (Display forms)
- **Heroku Postgres** (Database after deployment)
- **AWS** S3 Bucket (Storage of static files)
- **Github** (Project Management and storage for repo)
- **Gitpod** (Development hosting platform)
- **Google Dev Tools** (Debugging and check responsiveness)
- **Google Fonts** (Fonts)
- **Font Awsome** (Icons)
- **Balsamiq** (Wireframes)
- **DBdiagram** (Database schema)
- **TinyPNG** (Compress image file)


## Database
- SQLite was used in delevopment to store data
- PostgreSQL was used in production to store data



# Testing
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS

[Html Checker](https://validator.w3.org/nu) to test HTML

[JSHint](https://jshint.com/) to test Javascript

[PEP8 Validator](http://pep8online.com/) to test all Python files

## Manual Testing


## Performance testing

I run Lighthouse tool to check performance of the website. 

![Lighthouse]


## Bugs during development:

- I accidentally made a commit with the `STRIPE_SECRET_KEY` in the `view.py` which ended up in version control, so I created a new secret key in Stripe and exported it and set a new variable 


## Bugs to be debugged after Project Deadline:


# Deployment


## Local Deployment



# Credits

- [Colormind.io](http://colormind.io/) - Color palette picker 

- [How to make footer stay at bottom with Bootstrap](https://radu.link/make-footer-stay-bottom-page-bootstrap/) 

- [When migrating an already existing model](https://pytutorial.com/how-to-solve-you-are-trying-to-add-a-non-nullable-field-to-without-a-default)

- [Build a contact form](https://learndjango.com/tutorials/django-email-contact-form)

- Photos: My partner William Thornton

- Product images and description: https://www.cybercellar.com/product-category/wine/













