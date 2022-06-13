![Am I Responsive](/misc/readme_images/amiresponsive.png)

# About

**Supercazzola** which in italian means nonsense; "a phrase devoid of logical sense composed of a random set of real and non-existent words". Let's skip the pretentious talk about wine and just focus on really good wine!
For us it is just about good, non pretentious, low intervention wines from our friends in Italy and South Africa. 
They may be the sons and daughters from the more classic wineries or new vinyard experimenting and just doing their own thing. Either way, they are making their own paths and pushing wine making into the future, experimenting on their own and providing us with outstanding wines. As long as we find it great, we are proud to be your local wine distributor in Southern Sweden. 
Because we assure you - you will come back for more. 

# UX 

# Strategy

## Business Goal:

Become the biggest importer of natural wine in Sweden. Targeting the people loving wine but may not necessarily know so much about it. 

## Target Audience:

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

## Tone of Voice:

We'll share informational and "educational" content in a witty, non pretentious way - not taking for granted that our community know it all.  

## Business Model:

B2C (Buiness to Customer) - A carefully selected e-commerce of imported natural wines to sell to winelovers over 21 years old in Sweden. Selection will mainly come from South Africa and Italy, seeing the gap in the market of South African low intervention wines, will especially make Supercazzola a name for itself. 
B2B (Business to business) - A big part of Supercazzolas business model will be to distribute wine to bars and restaurants in the southern part of Sweden. Wine events, wine tastings and pop-up events will have our presence. 

Since we offer alcoholic beverage we will not have sales nor discounts on our products, but will rather make sure our community have fun at our accessable events and wine tastings, which will be shared by newsletter to those who sign up.


## User Stories:

### Epic: Login/Register

1. As a user I want to register an account so that I can store delivery information for quick and easy checkout
2. As a returning user I want to login to my account so that I can manage my account
2. As a returning user I want to login to my account so that I can view order history
3. As a returning user I want to login to my account so that I can add items I like to a favourite list
4. As a returning user I want to logout from my account so that I know it is secure


### Epic: Shop/Products

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

### Epic: Payment/Checkout

15. As a user I want to see a summary of my bag so that I know what I am eventually paying for
16. As a user I want to see the shipping fee so that I know the total price
17. As a user I want to be able to change quanities in the bag so that I can edit the bag in case I have changed my mind or I see the total cost is too high
18. As a user I want to fill out my delivery information so that I can control where my order is being sent
19. As a user I want to securely pay for my items so that my card details are safe
20. As a user I want to be notified when an order has gone through so that I know it was successful 
21. As a returning user I want to store my shipping information so that I quickly can checkout next time
22. As a store owner I want to see an order summary of confirmed purchase so that I can proceed with delivery of products

### Epic: Site

23. As a user I want to read about the company when I land on the page so I can find out about what they do and who they are
24. As a user I want to sign up for emails so that I can stay up to date with events/wine tastings and other news
25. As a user I want to see Social Media links so that I easily can follow and be part of their community
26. As a user I want to see a navigation menu so that I can easily navigate on the site
27. As a user I want to be notified by messages when on the site so I know about alerts/errors/success
28. As a user I want to be emailed an order confirmation so that I can keep it as a reciept of successful order
29. As a bar/restaurant owner I want see contact information so that I can potentially buy your wine for my business

-------

# Scope

To achieve the user and business goals, the following features will be included in this project:

- Responsive navbar
- Landing page with About Us section and links to relevant pages such Shop and Contact
- Shop page, that displays all products available with the option to search for a specific product or filter
- Register/login feature so that users can create an account
- Contact for for business that wants to reach out for potential collaborations
- My Account page, for logged in users to update their details and view their previous orders and wishlist products
- Footer with links to social media accounts as well as a newsletter signup


# Structure

## Data Models:

Following models have been created for this project:

- Profile App:
    - User - Django AllAuth user account that is being create upon registration
    - User Profile - Storing users contact information, order history and wishlist items
- Product App: 
    - Product - Stores product image, details, price and description
    - Category - Linked to product
- Checkout App:
    - Order - Creates an instance of an order when succesfully progressed with billing/shipping information, a foreign key to the UserProfile and users details. Also includes information of payment, the stripe PID and basket contents.
    - OrderItem - Each orderline of the total Order that includes: product, quantity and price
- Wishlist App:
    - Wishlist - Stores all users liked item
    - WishlistItem - Allowing users to add individual items to their wishlist

## Database Schema:

![Database Schema](/misc/readme_images/database_schema.png)


# Skeleton

## Wireframes:
The wireframes differs slightly from the end result, but the main idea is still very much there. A consistent page layout on most pages for a no-surprising user experience with the focus on straight-to-the-point and product sales. 
Some content is hidden on smaller devices to ensure the mobilescreen gives the user the most important and relevant information. 

**Alert Box:**

![Alert Box](/misc/readme_images/Alertbox.png)

**Home:**

![Home](/misc/readme_images/Home.png)

**Shop:**

![Shop](/misc/readme_images/Shop.png)

**Product Detail:**

![Product Detail](/misc/readme_images/Product_detail.png)

**Cart:**

![Cart](/misc/readme_images/Bag.png)

**Checkout:**

![Checkout](/misc/readme_images/Checkout_pay.png)

**Thanks for shopping:**

![Thanks for shopping](/misc/readme_images/Thanks_for_shopping.png)


# Surface

## UX Design:

A clean layout and a proven e-commerce structure for a smooth navigation on the site. 
Research amongst competitors show quite pale choice of colors and the few that caught my eye had a stronger visual approach and therefor decided to go with a strong shade of yellow (quite a characteristic color of natural wine capsules, which you sometime see made of rubber), also the color of the sun and without sun no wine. Black and white for simplicity and for a professional look. I generated complimentary colors through [Colormind.io](http://colormind.io/) to set the color scheme for strong visual identity.
This also supports by our target audience being interested in art and design, looking for that different wine to stand out amongst their friends. 
The age of target audience is proven to spend most of their time on the phone - therefor a fully responsive website on smaller devices is crucial. 

### Colors:
![Colormind Colors](/misc/readme_images/colormind_colors.png)


### Font:

I wanted to create an artsy look of the logo and first went for a grafitti style font. When doing research of font pairings I found the Google Font "Permanent Marker" matched with "Overpass Regular" on [Heyreliable.com](https://heyreliable.com/) and knew immediately that I wanted these two - one for an artsy "not giving a f"-look that suits the brand image and tone of voice, and one for a clean and neat read.
Heyreliable also just happened to have a yellow color below:

Heyreliable font pairing:

![Heyreliable fonts](/misc/readme_images/Heyreliable_fonts.png)

Fonts: *Permanent Marker* paired with *Overpass Regular*

![Fonts Permanent Marker and Overpass Regular](/misc/readme_images/fonts.png)

Logo Font: *Londrina Solid*

![Logo](/misc/readme_images/logo.png)


## Features:

**Navbar** 
A fixed navbar that remains at the top of the screen throughout the site, allowing the user to easily navigate through the website. On smaller devicese the *Shop* and *Home* collapsese down to a burger. Includes:
- Logo: Linked to home page
- Search bar
- User Account: Login/Register
- Logged in user will also see the heart symbol that takes the user to the wishlist page and can also navigate to My Profile in the navbar. 

![Navbar](/misc/readme_images/navbar.png)

Mobile Navbar:

![Navbar mobile](/misc/readme_images/navbar_mobile.png)

**Home**

The home page consists of most relevant call-to-action buttons as well as information for a smooth UX so the user doesn't have to navigate around the site to find what he/she is looking for:
- A short tagline
- Shop Now-button
- Contact-form for bar/restaurant owners
- About us section
- What is Natural wine - section

The page is structured in two columns which on mobile version stacks as one column and some photos are removed so the scrolling doesn't have to be too long.

**Footer** 

I used Bootstrap for a fixed footer that stacks the columns when on smaller screens. Footer is showing on all pages and links to Social Media and provides a newsletter signup form from Mailchimp

![Footer](/misc/readme_images/footer.png)

Mobile Footer:

![Footerbar mobile](/misc/readme_images/footer_mobile.png)


**Shop** 

A grid of three to display all products available as well as a Sort-By tab. The Sort-By tab can organise products by Price(Low to High), Price(High to Low) or By Color. 
Products displays an image (default image will be set if none is provided), product title, wine origin (Country), alcoholic ratio, category (color of wine) and price. When clicking on the product user is being linked to the Product Details page.

![Shop_all Page](/misc/readme_images/shop_page.png)

Mobile Footer:

![Shop mobile](/misc/readme_images/shop_all_mobile.png)


**Product Details page** 
Further information about the individual product is visible here with same details as the Shop page as well as Description. 
User can also increment or decrement quantity they wish to purchase and click on Add To Cart-button. 
When adding to cart a pop-up message is shown that the product was sucessfully added with a summary of the cart so far.

![Product details page](/misc/readme_images/product_details_page.png)

Pop-up message:

![Message cart](/misc/readme_images/messages_cart.png)


**Cart/Checkout**

The Cart provides a summary of the chosen products in a table, including product, price, quantity and subtotal. 
In each product row the user can adjust quantity to press the X to remove the item completely from the cart. The psuptotal and total is beeing adjusted accordingy when pressing the Update Cart button. 
At the bottom the button to Checkout is provided. Or a Keep Shopping link that takes the user back to the shop page. 
If nothing exists in the cart the page will show "Your Cart is Empty" with a link to Keep Shopping.

The checkout page is the final step where the users completes the order. Split in two columns the first one allows the user to enter shipping information and full_name and email in a form. If the user is logged in default shipping details is prepopulated and the user also has an option to save the shipping information for future. 
The second column is a summary of the cart.

The payment has been set up using [Stripe](https://stripe.com/en-gb-se) and is for this deployment in test mode. A purchase can be tested by entering the following Stripe card details:
4242 4242 4242 4242, any future date for expire date and any five digits for post code. 


![Shopping cart](/misc/readme_images/shopping_cart.png)

![Checkout page](/misc/readme_images/checkout_page.png)

![Payment section](/misc/readme_images/payment_section.png)


**Successful Checkout**

If a successful order was proceeded the user will be taken to a checkout_success page where a summary of the order is provided. An email with the order details will also be sent out. 

**Sign Up/User Profile/Wishlist**

When a user has registered an account and logged in the user can view past orders and shipping information as well as like products that will be added to a wishlist.
Each product has a heart on the shop page, and when clicking on it it is beeng added to the wishlist or promptin the user to login/signup in order to do so. Products can be removed from the wishlist, by clicking on the heart. 

![Sign Up](/misc/readme_images/signup.png)

![My Account](/misc/readme_images/my_account.png)

![Wishlist](/misc/readme_images/wishlist.png)


**ADMIN: Product Management**

A superuser (an admin of the store) can add products when clicking on Product Management in the Account-navbar. Products can also be edited or deleted when clicking on the links to the specific product they want to be changed.
After adding a product or editing a product the user is being redirected to that new Product Detail page. 

![Admin Edet/Delete product](/misc/readme_images/admin_edit_delete.png)

![Admin Edit product](/misc/readme_images/admin_edit_product1.png)

![Admin Edit product](/misc/readme_images/admin_edit_product.png)

**ADMIN: Admin Console**

The Django framework provides a great Admin interface which has taken advantage of during development of this project. The admin panel allows superusers to add/edit products, remove/add users, check order information and see users wislist and wishlists items.

![Admin panel](/misc/readme_images/adminpanel.png)
![Admin panel](/misc/readme_images/adminpanel1.png)
![Admin panel](/misc/readme_images/adminpanel2.png)


## Marketing:

**Mailchimp**

Our community will be reached through Newsletters in which users can sign up to from the `footer` of the site with embedded Mailchimp. Mailchimp will store the email addresses and with time we will organise the users into groups depending on what they want from us: Will it be updates regarding new wines coming in, or eventseekers or those that are most interested in reading about wine an a witty informative way. We will shape email groups after their preference.

![Mailchimp signup](/misc/readme_images/mailchimp.png)

**Instagram**

Our target audience is mostily on Instagram and that is where we will meet them - adding posts ourselves and resharing posts from our community (if they fit our brand image) on a close to daily basis in order to rank high in our followers post stream. 

**Facebook Business Page**

In the footer users will find a link to our [Facebook Business page](https://www.facebook.com/supercazzolawine/) where we will marketing most of our wine events and be avaialble to chat to our customers if they have any questions.

![Facebook Business](/misc/readme_images/facebook_business1.png)
![Facebook Business](/misc/readme_images/facebook_business2.png)

![Facebook mobile](/misc/readme_images/facebook_mobile.png)

**SEO**

I started with a Google analysis and realised people frequently ask what natural wine is. Which I believe is a valid quiestion seeing it is relatively new on the market - So I wanted to include the question in a h2 header and a short answer to what it is in the homepage to increase SEO.
In the Abous Us section there are also a lot of keywords included, such as: *Supercazzola* (our brand!), *wine, good wine, low intervention wine, Italy, South Africa, wineries, vineyard, wine making, local wine distributor, Southern Sweden*

On top of this I made google searches to see questions that people ask frequently and intergrated them in Meta Keywords, as well as other keywords that ranked high on google. Seeing the competition of natural wine distribution is not that high in Sweden I wanted to make sure that we include the most common keywords people search on, rather than niched ones.

![SEO Meta keywords](/misc/readme_images/seo_meta.png)



# Planning / Agile Management
I used the Github kanban board to create issues and user stories in the early development stages of this project and moved them across the board as I progressed from TODO -> In Progress -> Done. 
Link to [Github Project here](https://github.com/viktoriamahrberg/supercazzola/projects/1)
Userstories were organised in "must-have", "could-have" or "should-have" labels in order to make prioritization of the scope easier. 
I added userstories as I went on and realised what I want to add to the site in the future and have kept them in Backlog for further assessment after this project has been handed in.

![Project Management Kanban board](/misc/readme_images/agile_project_management.png)

I set up the project into 3 sprints:

_Sprint 1 (23-25th May):_
- Researching competitors
- Planning
- User Stories 
- UX / designing the site
- Set up wireframes
- Database schema

_Sprint 2 (25 May - 8th June):_
- Building the site

_Sprint 3 (8 May - 13th June):_
- Readme.md
- Tweaks
- Testing
- Responsiveness 

### Backlog: Features to be implemented in future:

- Overlay with an alert message asking if customer is above legal age of 21 to buy alcohol

- Heart to change color on Products page when adding to Wishlist

- The legal age to buy alcohol is above 21 so a feature to implement in the future would be to link Bank ID for users to log in and confirm their age.

- Klarna for seamless checkout, as well as remove test mode for Stripe

- In Admin panel: Rank the wishlist items according to most 'likes' in order to see popular wines for company to increase sales


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
        
- **[Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)**
- **[Bootstrap 4.6 boilerplate](https://getbootstrap.com/docs/4.6/getting-started/introduction/)**
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


# Testing
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS

[Html Checker](https://validator.w3.org/nu) to test HTML

[JSHint](https://jshint.com/) to test Javascript

[PEP8 Validator](http://pep8online.com/) to test all Python files.
All files in the following apps have have been tested manually in Pep8 and shown code is all right:
- Bag

- Checkout

- Contact 

- Home

- Products

- Profiles

- Supercazzola

- Wishlist
    
![Pep8 Validator](/misc/readme_images/pep8.png)


## Responsiveness Testing

I have tested the deployed version on different devices such Iphone5/SE, Ipad Mini and my Macbook'11. Any responsive issues have been fixed. 



## Manual Testing

[Link to manual User Story testing](/manual_testing.md)


## Bugs during development:

- I accidentally made a commit with the `STRIPE_SECRET_KEY` in the `view.py` which ended up in version control. FIX - I created a new secret key in Stripe and exported it and set a new variable 

- I added one Update Bag button to update all products quantity in Cart-page and had issues to wrap my head around why it didn’t work to update the cart. FIX - I realised after trying many different options that the button is supposed to update *one* item - not the entire column. So I had to insert one on each row. 

- Allauth templates (login-, signup-, logout.html etc) did not work to change and I tried to {% extend 'account/base.html' %} as well as {% extend 'base.html' %} but no changes I do renders in the preview. FIX - Django requires Allauths account folder had to be out of allauth - in templates folder.

![Allauth bug](/misc/readme_images/bug_allauth.png)

![Allauth bug fix](/misc/readme_images/bug_allauth_fix.png)

- Stripe Webhook did not show any responses except for a 401 error in stripe events page. FIX - Turns out the Gitpod preview window needs to be made public for Stripe to be able to communicate.

![Webhook fix](/misc/readme_images/stripe_webhook.png)

- Images not showing when deployed to Heroku and synced with AWS S3 bucket. FIX - Tips from Stackoverflow - I had missed adding a line in settings: `django_template.context_processors_media`

![No Image bug](/misc/readme_images/debug_no_image.png)

![No Image Fix](/misc/readme_images/bug_allauth_fix.png)

- I had a bug with the footer coming up on homescreen at first:

![Footer Bug](/misc/readme_images/responsive_home_footer.png)

FIX: Followed this link - [How to make footer stay at bottom with Bootstrap](https://radu.link/make-footer-stay-bottom-page-bootstrap/) 

![Fixed footer](/misc/readme_images/responsive_fixed_footer.png)


## Bugs to be debugged after Project Deadline:

- Increment and decrement button on full screen in Cart page is not blocking user from going below 0. I tried several options with changing ID to classes and make two different Javascript codes for the mobile version and full screen version. Unfortunately the time was not enough for this matter and will be sorted after project deadline.

- Mailchimp input label doesn't remove automatically when entering an email

- Burger menu is not opening dropdown on Ipad Mini

# Deployment
### Github & Gitpod

My app was built from the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) and followed the deployment process from Code [Institute Django Blog Cheat Sheet]
(https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

### Deploy to Heroku
1. Create a new account or login to your Heroku account
2. Create a New Heroku app
3. Give the app a unique name choose a region closest to you
4. Click Resources and add 'Heroku Postgres' in Add-ons section
5. To use the Postgres database it needs to be installed in Gitpod: Type `pip3 install dj_database_url` in the terminal and `pip3 install psycopg2-binary`
6. Freeze these requirements with `pip3 freeze > requirements.txt`
7. Set up new database in settings.py: import dj_database_url
8. In Gitpod you also need to create a Procfile to tell Heroku to create a web dyno which will run gunicorn and serve our django app
9. Go to Deploy section tab in Heroku and scroll down to Deployment Method. I connected to my Github pages and could thereafter linked to the Github repo.
10. Choose the branch you want to buid your app from
11. Manual deployment from Gitpod to Heroku is made with command: `git push heroku main` in CLI.
12. After finishing working on the site: DEBUG = False was changed in settings.py.

![Successful Deployment](/misc/readme_images/deploymentsuccess.png)

### AWS S3

AWS Amazon S3 bucket was used to load and store statics.
I have created a Bucket, User Group and User that can access this site and the relevant files. In order for the files to be correctly served I have added the following settings in settings.py file:

![AWS S3 Bucket](/misc/readme_images/aws_s3_bucket.png)

## Local Deployment

**Forking a GitHub Repository**

To 'Fork' a repository, for instance if you want to make changes to the repository without affecting it, follow the steps below:

- Login to your GitHub account and find the relevant repository
- Click on 'Fork' on the top right of the page
- You will find a copy of the repository in your own Github account

**Cloning a GitHub Repository**

Cloning your repository allows you to download a local version to be worked on. 
Cloning can also be a great way to back up your work:

- Find the relevant repository
- Press the 'Code' button
- Copy the link that is shown in the drop-down
- Now open Gitpod & select the directory location where you would like the clone created
- In the terminal type 'git clone' and paste the link you copied in GitHub
- Press enter and your local clone will be created


# Credits

- **Code:** The core functionality of Supercazzola is coming from the [Code Institute's](https://codeinstitute.net/) walkthrough project - [Boutique Ado Project](https://boutique-ado-vikmah.herokuapp.com/).
Thank you Code Institute - it's been a real hero for my understanding of Django.

- Thank you all fantastic tutors at Code Institute

- [Colormind.io](http://colormind.io/) - Color palette picker 

- [How to make footer stay at bottom with Bootstrap](https://radu.link/make-footer-stay-bottom-page-bootstrap/) 

- [When migrating an already existing model](https://pytutorial.com/how-to-solve-you-are-trying-to-add-a-non-nullable-field-to-without-a-default)

- [Build a contact form](https://learndjango.com/tutorials/django-email-contact-form)

- Photos: My partner William Thornton

- Product images and description: https://www.cybercellar.com/product-category/wine/















