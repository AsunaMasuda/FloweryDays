# Testing
## Table of Contents

1. [Manual Testing](#manual-testing)
    - [Responsiveness](#responsiveness)
    - [Landing Page](#landing-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Onlineshop](#onlineshop)
    - [Blog](#blog)
    - [Cart](#cart)
    - [Checkout and Checkout Success Page](#checkout-and-checkout-success-page)
    - [SignIn and Order History](#signin-and-order-history) 
    - [Profile and Order History](#profile-and-order-history) 
    - [Admin Product Management](#admin-product-management) 
    - [Bugs](#bugs)
    - [Peer Code Review](#peer-code-review)

2. [Automated Testing](#automated-testing)
    - [Travis](#travis)
    - [Django tests](#django-tests)
    - [LightHouse on Google DevTool](#lighthouse-on-google-devtool)

3. [Code Valication and Formatting](#code-valication-and-formatting )
    - [Validation Tools](#validation-tools)
    - [Formatter](#formatter)

4. [Compatibility and Responsiveness](#compatibility-and-responsiveness)

# Manual Testing
These tests were conducted on the deployed site on Heroku.

## Responsiveness
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User/ Shopper | access the website with any devices | Use the website anytime and anywhere |
| Shopper | All the important services are accessible from nav bar| Don't need to scroll to find important information | 
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want | 
### Test conducted:
- Access each page in the site with different screen sizes with Google Dev Tool's Emulator and check the layout and format of site elements
### Result:
1. Navbar: I have the search bar collapsed for smaller than medium screen size (width < 992px) because the search bar with input field conflicted with other navbar components. 
'My Account' pulldown list is included to toggle menu for smaller than medium screen size.
2. Home page: The image size responsiveness on Carousel at landing(home) page was adjusted by media queries.
### Verdict:
Passed all tests.

## Landing Page
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Easily see what services are offered | Find the service I want to use |
### Test conducted:
- Click all the buttons and links on the page
- Click carousel items (indicator, previous/nect button)
- Submit contact Form to see if the admin receives an email
### Result:
- All the buttons and links are working as expected. 
- The carousel items are working as expected.
- The email was sent after submitting the contact form.
### Verdict:
Passed all tests.


## Navbar
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- | 
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want |  
### Test conducted:
- Click the menu links and see if all the links work properly.
- Change the screensizes and check if the menu and the keyword search get collapsed not to overwrap each other.
### Result:
- The items on the navbar do not overwrap with the common screensizes.
### Verdict:
Passed all tests.

## Footer
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Easily see what services are offered | Find the service I want to use |
### Test conducted:
- Click all the links to see it they work as expected.
- Click the social media icons to see if the links work as expected.
- The layout changes upon different screen sizes.
### Result:
- The link 'Contact' was connected to a wrong link. This issue was fixed upon beding found.
### Verdict:
Passed all tests.

## Onlineshop
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Search a product with keywords | Find the most appropriate products |  
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing | 
| Shopper | Filter with a specific category of product | Easily find products in a specific category | 
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular by the other customers | 
### Test conducted:
- Use various keywords in keyword search and check if it works as expected.
- Check if the online shop page / the individual product page is displayed without breaking the layout for common screensizes.
- Navigations such as paginations, breadcrumb, back to previous page button etc don't break accessing by different paths.
- Check if the quantity counter and the color options work as expected and gives an informative error message if the number is outside of the range (1-99).
### Result:
- The layout of single_product page for screens less than 992px width was overwrapped. It was fixed by changing the appropriate bootstrap grid system.
- As width of the product image is set to 400 px, the layout was overwrapped in single_product page. This was fixed by changing it to smaller image size.
- The link to previous page of the pagination bar had a wrong attribute `value`. This was fixed by replacing it with `href`.
### Verdict:
Passed all tests.

## Blog
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site Owner | Post a blog about flower arrangement and gardening | Give site visitors interesting information about flowers | 
| Site Owner | Let the site users log in when they leave comments/reviews | Track who left comments/reviews | 
| Site User | Add comments to the blog posts | Write down my thoughts to the post | 
### Test conducted:
- Change the screen sizes to check if the images are displayed properly.
- Click all the links in this section: links to each post, the category link on the side bar, the breadcrumb menu.
- Post/Delete Comment on each post on the site.
### Result:
- The comment section on individual blog post was placed on the right side for smaller screen sizes. This was because of the class `blog-comment-section`. I enabled this class for bigger screen sizes only.
### Verdict:
Passed all tests.

## Cart
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Easily select the quantity and the color (if applicable) of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
### Test conducted:
- Check if the quantity counter works propely and gives an error message if the number is out side of the range (1-99).
- Check if Remove/Update link works properly.
### Result:
- The quantity counter works as expected.
- Remove/Update link works as expected.
### Verdict:
Passed all tests.

## Checkout and Checkout Success Page
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- |  
| Shopper | The delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Shopper | Automatically suggest to log in if I did not log in | Smoothly proceed with my purchase | 
### Test conducted:
- Access the checkout page after adding some items to the cart with/without logging in.
- Complete the check out process with various type of products e.g. with different product categories, with color options, etc
### Result:
- The delivery information form is prefilled if logged in.
- If not logged in, a message appears at the end of the form: "Create an account or login to save this information".
- All the webhooks in Stripe returned success after the checkout.
- The customer received the order confirmation email to the email address that was added to the checkout page.
### Verdict:
Passed all tests.

## SignIn and Order History
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site User | Easily register for an account | Have a personal account and be able to view my profile and ability to check order history |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
### Test conducted:
- Sign up with an email and check if the account receives an email and Log in with the created account.
- Use `forgot password?` link to check if recovering the password works.
### Result:
- Email Address Confirmation email contains `site_name` and `site_domain` and they returned the default value 'example.com'. These were changed to the deployed site `flowerydays.herokuapp.com/` in Django Admin > Sites.
- The font color of the submit button on Password Reset page was set as the same color as the back ground. It was fixed after this test.
### Verdict:
Passed all tests.

## Profile and Order History
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information |  
| Site User | View my order history | Purchase the same product again in the next order |
### Test conducted:
- Create a new account and edit the delivery information.
- Order History Page renders as expected accessing from My Account page.
### Result:
- Delivery information is updated as expected after alternation in My Account page.
- In Order History, the order date and color option were missed. This was fixed immediately to modify the template.
### Verdict:
Passed all tests.

## Admin Product Management
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site Owner | Easily add a new product | Make sure the online site has the latest lineups | 
| Site Owner | Easily add a new blog | Manage blog posts easily on website | 
### Test conducted:
- Add a product with/without image and check if they are acceptable
- If the user is not superuser and accessed to the direct url to Admin Product/Blog Management, they get redirected and informed.
### Result:
- The rating option was included to the add product form. I deleted this because reviews are not needed when adding a new product.
- They get redirected to the landing page and get information on the toast.
### Verdict:
Passed all tests.
* However, as a feature left to implement, `Category` and `Occasion` should be `Select` menu instead of `Text Input`, in the product management form. At the moment, the admin can input any text for `Category` and `Occasion` and even if inputting the same `Category` or `Occasion`, these two are recognized as different categories or occassions in the system. I acknowledge that this is an important feature, but after a lot of researches, I found that this was complex to create a form selection from values in a field (in this case, Category and Occasion) in a certain model(Product). After spending some time on this project, I found the data modeling scheme I made for this project at the beginning was not the best choice, so for the next Django project, I want to think about these aspects of data management when I am building the data modeling.

## Bugs
Minor bugs are reported at the relevant section as you can see above. Here I will write down some interesting bugs I came accross in the testing.
- `$(document).on()` does not work on mobile device
 `$(document).on()` was initially used for product quantity counter was not working on mobile devices. To resolve this issue, once I used JQuery Mobile to use `vclick` event. However, JQuery Mobile is not compatible with the updated JQuery and gave an error in console. So in the end, I found out if you use `$('.plus').click(function(){...`, the issue would not occur.
- During CSS validation, I got an error `Property padding-inline-start doesn't exist : 0` for the class `carousel-indicators-extension ol` to modify `-webkit-padding-start: 40px` which is from the user-agent stylesheets of every browser. This was replaced with `margin-left: -40px;`, which is advised [here](https://stackoverflow.com/questions/29307357/get-rid-of-webkit-padding-start-40px).
- Some HTML files used in this project contain `style=` that specifies css. I acknowledge that having this in HTML is not the best practice though it does not give errors, but it was inevitable to implement some features such as displaying product review score stars (e.g. line in .html), since the percentage for the score is calculated in the views.py and passed to the template. 

## Peer Code Review
I got feedback from other students in Code Institute by asking on the Peer Code Review channel in the Slack community.
- A fellow student spotted the filter options return as a query set after using a key search function. This was immediately fixed after her feedback.

# Automated Testing
## Travis
[Travis CI](https://travis-ci.org/) was also used for the automated unit testing of this project. 
Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket.
Travis CI is configured by adding a file named .travis.yml and you need to set a secret key in the settings in Travis. 
How to set up Travis CI can be found in [this documentation](https://docs.travis-ci.com/).

## Django tests
I have run tests for the models and views in all apps, where applicable. For Django testing, I have downloaded packages: `coverage` and `django-nose`.
I have tried to automate the tests as much as possible, but could not reach 100% coverage, since some parts in views.py are complicated and it was difficult to test automatically so I chose manual testing. I also learned [Test-Driven Development](https://www.guru99.com/test-driven-development.html) while learning Django Testing, next time when I build a Django application, I want to try this approach.


## LightHouse on Google DevTool
I used Lighthouse by Google on Landing Page, Online Shop Page/Single Product Page, Blog Page, Cart Page.
<br>Result: `Landing Page` - It reported the file size of some images are not appropriate, even after I used service called [tinypng](https://tinypng.com/) to reduce the file size. I'd like to investigate this as feature improvements because of the time constraints.


# Code Valication and Formatting 
### Validation Tools
I used these validation tools below for each file.
- HTML: [W3C HTML Validator](https://validator.w3.org/) *For HTML validator, I passed each URI to validator since the html files contain Django templates.
- CSS: [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
- JavaScript: [JSHint](https://jshint.com/)
- Python: [PEP8 online](http://pep8online.com/)

Result:
- In CSS validation, there are warnings for button elements. I did not address this since the color should be kept for the design purpose and it does not affect any other functions/elements.
- There is an error `Duplicate ID` when validating in cart view, but it's expected since there are Cart View for Desktop and Mobile devices and these IDs won't be rendered at the same time.

### Formatter
- HTML: [HTML Formatter](https://codebeautify.org/htmlviewer/) - Set the tab size to 4.
- CSS: [CSS Formatter](https://webformatter.com/css) - Set the tab size to 4.
- JavaScript: [Online JavaScript Beautifier](https://beautifier.io/)
- Python:[PEP8 online](http://pep8online.com/)

Note:
- I used HTML formatter but there are Django templates in the html files which broke the format. In these cases, I manually formatted the html files referring to html files used in [botique ado project](https://github.com/ckz8780/boutique_ado_v1/tree/9ed36dc2c07228041b56b28174dd96ee56e6c59a).

# Compatibility and Responsiveness
The device emulator by Google Chrome's developer tool is used to check the responsiveness across all the different screen sizes and devies to ensure compatibility and responsiveness. Also, this website has been tested on multiple browsers (Chrome, Safari, Opera, FireFox) on macOS Mojave (Version 10.14.6).  iPhone XR (iOS 14.1) is used to test for mobile testing.
