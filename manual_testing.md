# Manual Testing Functionality

[Back to README.md](/README.md)

NAVBAR
| Element | Action | Expected Output | Pass/Fail |
| ----------- | ---- | ----------- | ---- |
|  **NAVBAR** |  |  |
|  Logo | Click | Redirects to Home | Pass
|  Searchbar | Input | Loads the page with products or display "No products found" | Pass
|  Searchbar | No Input | Message pops up that nothing was searched for | Pass
|  Shop | Click | Dropdown menu with products to shop by color or All Products | Pass
|  Profile icon | Click | As logged in user: Dropdown with 'My Profile' and 'Log Out' | Pass
|  Profile icon | Click | As logged in superuser: Dropdown with 'Manage Products', 'My Profile' and 'Log Out' | Pass
|  Profile icon | Click | As first visitor user: Dropdown with 'Register' and 'Log in' | Pass
|  **MOBILE NAVBAR** |  |  |
|  Burger menu | Click | Open Dropdown | Pass
|  -Home | Click | Return to Home page | Pass
|  -Shop | Click | Redirects to Shop All Products page | Pass
|  Search icon | Click | Displays search field | Pass
|  Searchbar | Input | Loads the page with products or display "No products found" | Pass
|  Searchbar | No Input | Message pops up that nothing was searched for | Pass
|  Profile icon | Click | As logged in user: Dropdown with 'My Profile', 'My Wishlist' and 'Log out' | Pass
|  Profile icon | Click | As logged in superuser: Dropdown with 'Manage Products', 'My Profile', 'My Wishlist' and 'Log Out' | Pass
|  Profile icon | Click | As first visitor user: Dropdown with 'Register' and 'Log in' | Pass
|  -Register | Click | Redirects to Sign Up page | Pass
|  -Login | Click | Redirects to Login page | Pass
|  -Logout | Click | Redirects to Sign Out | Pass
|  -My Wishlist| Click | Redirects to My Wishlist page | Pass
|  -Product Management | Click | Redirects to Product Management page | Pass
|  Cart/ €0.00 | Click | Redirect to Cart page | Pass
|  **HOME PAGE** |  |  |
|  Shop Now-button | Click | Redirect to Product page | Pass
|  Contact Us Here-button | Click | Redirect to Contact page | Pass
|  **FOOTER** |  |  |
|  -Social Media icons | Click | Redirects to Supercazzola Facebook Business page, Twitter homepage and Instagram homepage | Pass
|  Signup Mailchimp | Input | Redirects to 'Mailchimp-Thank you for signing up page' | Pass
|  Signup Mailchimp | Wrong Input | Redirects to 'Mailchimp-Error page and asks user to fill out correct details again' | Pass










| User loads the home page as signed in | Only Logout and Create Post links show in nav bar and all content loads and work as expected |  [x]

# User Stories Testing

### Epic: Login/Register
- As a user I want to register an account so that I can store delivery information for quick and easy checkout
- As a returning user I want to login to my account so that I can manage my account
- As a returning user I want to login to my account so that I can view order history
    - User can login or register for an account and will be able to see order history and store delivery information in "My Account". Upon Checkout there is a "Save this information to my Profile" which updates My Account with new personal information and pulls this to the Checkout form next time user is making a purchase.

    ![Email verification upon registration](/misc/readme_images/register_verifyemail.png)

    ![My Account](/misc/readme_images/my_account.png)


- As a returning user I want to login to my account so that I can add items I like to a favourite list
    - Users can add items to their wishlist by clicking on the heart of a product when logged in and is being stored in the menu "My Wishlist"

    ![My wishlist items](/misc/readme_images/my_wishlist_user.png)


- As a returning user I want to logout from my account so that I know it is secure
    - In the User Navbar users can log out from their account successfully

    ![Logout](/misc/readme_images/signout.png)


### Epic: Shop/Products

- As a store owner I want to add products to site so that I can increase sales
- As a store owner I want to edit products on site so that I can update products
- As a store owner I want to delete products to site so that I can manage products that are no longer available for sale
    - Store owners, or so called superusers, can edit/delete a product on the product page or add a new product in the Product Management navbar

    ![Edit/delete product](/misc/readme_images/admin_edit_delete.png)
    ![Add product](/misc/readme_images/admin_edit_product.png)

- As a user I want to view all products available to I can see what the offering is
- As a user I want to search for products so that I can easily navigate around on the site
- As a user I want to filter amongst the products so that I can easily find what is in my interest
    - Users can search in the search field for a product and a selection will be shown, either matching description or name. Products can be sorted by Price(Low to High), Price(High to Low) or By Category (Rose, Orange, Red or White wine color). By clicking on the shop button in the navbar the option to display "All products" is there.

    ![Shop, filer or search product](/misc/readme_images/shop_filter_search.png)

- As a user I want to click on a product so I can see more details about it
- As a user I want to be able to see description, price, origin and color of wine so I know what I am buying
    - Users can click on the product image from "All Products" page in order to see detailed product description. Price, origin/country, description, alcoholic ratio and color is displayed. 
    
    ![Product details](/misc/readme_images/product_details.png)


- As a user I want to add products to a shopping bag so that I can browse around before I checkout
- As a user I want to add quantity from product page so that I easily can buy more than one 
    - On the product details page an increment and decrement button is added that updates the bag accordingly and an "Add to Bag" button which stores the products in a cart for later checkout. 

    ![Quantity and Add to bag button](/misc/readme_images/add_to_bag.png)


### Epic: Payment/Checkout

- As a user I want to see a summary of my bag so that I know what I am eventually paying for
- As a user I want to see the shipping fee so that I know the total price
- As a user I want to be able to change quanities in the bag so that I can edit the bag in case I have changed my mind or I see the total cost is too high
    - In the Cart users can find a summary of product, product image, price, quanity and subtotal. User can also add, or remove quanity or remove product completely from cart here. 
    At the bottom of the Cart summary useres can find shipping price and total price before choosing to checkout.
    There is also a pop-up message displaying with all the above details when user is updating the cart so they are constantly aware of what they have in their cart.

    ![Cart Summary](/misc/readme_images/cart_summary.png)

    ![Total Price in cart](/misc/readme_images/total_price.png)

    ![Popup message with cart summary](/misc/readme_images/message_box.png)

- As a user I want to fill out my delivery information so that I can control where my order is being sent
- As a user I want to securely pay for my items so that my card details are safe
- As a returning user I want to store my shipping information so that I quickly can checkout next time
    - Users fill out their information and shipping address upon checkout. All fields are required to be filled in by user in order to proceed. This can be stored for logged in users for next time by checking the box before proceeding with payment. 
    Secure checkout is integrated with Stripe (as of this deployment only in test mode). 

    ![Shipping information](/misc/readme_images/shipping_details.png)

    ![Stripe payment secure checkout](/misc/readme_images/stripe_payment.png)

    ![Save Info checkbox](/misc/readme_images/saveinfo_box.png)

- As a user I want to be notified when an order has gone through so that I know it was successful 
    - Users are being redirected to a confirmation page upon succesfull checkout and a pop-up message confirms the payment was successful. The confirmation page shows an order summary including shipping information, total price, order summary, order number and order date.

    ![Checkout Confirmation](/misc/readme_images/checkout_confirmation.png)


- As a store owner I want to see an order summary of confirmed purchase so that I can proceed with delivery of products
    - Store owners can see all placed order in the Admin panel. It shows the products sold, total price, shipping price and full customer details including shipping details.

    ![Admin Order history](/misc/readme_images/admin_order_history.png)

    ![Admin Order history](/misc/readme_images/admin_order_product_history.png)

### Epic: Site

- As a user I want to read about the company when I land on the page so I can find out about what they do and who they are
    - About Us section is on the home page

    ![About us](/misc/readme_images/fonts.png)

- As a user I want to sign up for emails so that I can stay up to date with events/wine tastings and other news
- As a user I want to see Social Media links so that I easily can follow and be part of their community
    - In the footer users can sign up to Supercazzolas newsletter that has been embedded by Mailchimp and which will store all signed up emails. Also Social Media links can be found here, Facebook links to Supercazzolas Facebook Business page.

    ![Footer Mailchimp and Social Media links](/misc/readme_images/footer.png)

- As a user I want to see a navigation menu so that I can easily navigate on the site
    - The navbar consists of Shop - My Account and My Wishilist. On mobile version there is a burger menu with a dropdown to Home and Shop. 

    ![Mobile navbar](/misc/readme_images/navbar_mobile.png)


- As a user I want to be notified by messages when on the site so I know about alerts/errors/success
    - Djangos built in messages module is popping up with errors-, warnings-, success- and alert-messages in top right corner rthroughout the site. The message box can be closed down by the user manually. 

    ![Successmessage](/misc/readme_images/message_box.png)


- As a bar/restaurant owner I want see contact information so that I can potentially buy your wine for my business
    - A link to contact form can be found on the homepage which takes the user to a new page with a contact form.

    ![Contact form](/misc/readme_images/contactform.png)
