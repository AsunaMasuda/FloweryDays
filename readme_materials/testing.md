# Testing
## Table of Contents

1. [Manual Testing](#)
    - [Responsiveness](#responsiveness)

2. [Automated Testing](#)
    - [](#)

3. [Validators](#)
    - [](#)

4. [Compatibility and Responsiveness](#)
    - [](#)

5. [Other Testing](#)

6. [Bugs](#)


# Manual Testing
These tests were conducted on the deployed site on Heroku.

## Responsiveness
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site User/ Shopper | access the website with any devices | Use the website anytime and anywhere |
| Shopper | All the important services are accesible from nav bar| Don't need to scroll to find important information | 
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want | 
### Test conducted:
- Access each page in the site with different screen sizes by Google Dev Tool's Emulator and check the layout and format of site elements
### Result:
1. Navbar: I have the search bar to be collapsed for smaller than medium screen size (width < 992px) because search Bar with input field conflicted with other navbar components. 
'My Account' pulldown list is included to toggle menu for smaller than medium screen size.
2. Home page: The image size responsiveness on Carousel at landing(home) page was adjusted by media queries.
### Verdict:
The bug is fixed. Test passed.

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
Test Passed.

## Navbar
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- | 
| Shopper | Have a shopping cart icon on nav bar | Always check the current order and checkout when I want | 
| Shopper | Search a product with keywords (Search Bar) | Find the most appropriate products |  
### Test conducted:
### Result:
### Verdict:

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
Test Passed.

## Onlineshop
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Search a product with keywords | Find the most appropriate products |  
| Shopper | Sort the search results by the prices | Find the most appropriate products for the target price range | 
| Shopper | View individual product pages that have prices, descriptions, sizes, etc | Get detailed information about the product before purchasing | 
| Shopper | Filter with a specific category of product | Easily find products in a specific category | 
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular by the other customers | 
### Test conducted:
- The online shop page / the individual product page is displayed without breaking the layout for common screensizes.
- 
### Result:
- 'click' event by JQuery used for Quantity counter was not working on mobile devices. To resolve this issue, vclick event was added by JQuery Mobile.
- The layout of single_product page for screens less than 992px width was overwrapped. It was fixed by changing the appropriate bootstrap grid system.
- As width of the product image is set to 400 px, the layout was overwrapped in single_product page. This was fixed by changing it to smaller image size.
- The link to previous page of the pagination bar had a wrong attribute `value`. This was fixed by replacing it with `href`.
### Verdict:


## Blog
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site Owner | Post a blog about flower arrangement and gardening | Give site visitors interesting information of flowers | 
| Site Owner | Let the site users log in when they leave comments/reviews | Track who left comments/reviews | 
| Site User | Add comments to the blog posts | Write down my thoughts to the post | 
### Test conducted:
- Change the screen sizes to check if the images are displayed properly
- Click all the links in this section: links to each post, the category link on the side bar, the breadcrumb menu
- **Post/Delete Comment on each post on the deployed site**
### Result:
- The comment section on individual blog post was placed on the right side for smaller screen sizes. This was because of the class `blog-comment-section`. I enabled this class for bigger screen sizes only.
### Verdict:
Test Passed.

## Cart
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Shopper | Easily select the size and quantity of a product after adding a product to a cart | Ensure I don't accidentally select the wrong product and the quantity | 
### Test conducted:
### Result:
### Verdict:

## Checkout & Checkout Success Page
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- |  
| Shopper | Automatically suggest to log in if I did not log in, when proceeding with checkout | Smoothly proceed with my purchase | 
### Test conducted:
- 
### Result:
- Boolean Field with crispy form template (`{{ order_form.is_gift_wrapping | as_crispy_field }}`) just rendered a checkbox and the default value `False`. So I 
### Verdict:

## SignIn/Login, Order History
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

## Profile, Order History
### User Stories Tested:
### Test conducted:
### Result:
### Verdict:

## Admin Product Management
### User Stories Tested:
| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... | 
| ----------- | ----------- | ----------- | 
| Site Owner | Easity add a new product | Make sure the online site has the latest lineups | 
### Test conducted:
- Add a product with w/o image and check if they are acceptable
### Result:
### Verdict:


# Automated Testing
## Travis
[Tavis CI](https://travis-ci.org/) was also used for the automated unit testing of this project. 
Travis CI is a hosted continuous integration service to build and test software projects hosted at GitHub and Bitbucket.
Travis CI is configured by adding a file named .travis.yml and you need to set a seclet key in the setting in Travis. 
How to set Travis CI can be found in [this documentation](https://docs.travis-ci.com/).


## LightHouse on Google DevTool
Lighthouse is .... I used Lighthouse on  Landing Page, Online Shop Page/Single Product Page, Blog Page, Cart Page.
- Landing Page
Result: It reported the file size of some images are not appropriate, even after I used service called []() to reduce the file size. 
 I'd like to investigate this as feature improvements because of the time constraints.
- Blog Page
Result: The same issue of image file sizes is reported to the Blog Page. 
- Online Shop
Result: 

## Peer Code Review
I got feedback from other students in Code Institute asking on Peer Code Review in Slack community.
- Suggest to improve the readability of the text on hero image on landing page, since it's a bit hard to see.
This is fixed by adding a dark color layer onto the image.