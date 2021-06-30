# Web Scraping Script

Download the "web_scrape_script.zip" file and unzip it in the required directory.

Open the **Command Prompt** and navigate to the web_scrape_script folder using the `cd` command.

Run the web_scrape_script.exe file using the following command:

`web_scrape_script.exe`

The program will initially prompt the user to enter the URL for the webpage.


Next, the program will request the user to select the type of the **parent tag**. 
+ **Class Tag**: *e.g.* `div class='contact-info`
+ **ID Tag** : *e.g.* `div id='contact-info`
+ **CSS Selector Tag**:Tags such as `p` `a`, `body`, `tr`

The **parent tag** refers to the html tag which encloses the contact information of each faculty member. 

E.g.
Consider this code extract from <https://www.uno.edu/academics/colaehd/la/english/faculty>

Each faculty member's contact information has been enclosed in a *div* with the class tag `personal-info`. 
```html
<div class="personal-info">
  <div class="name"><a href="/profile/faculty/ayana_olatunji">Ayana Olatunji, M.Ed.</a></div>
  <div class="professional-titles">Coordinator Associate of First-Year Writing, Creative Writing Workshop, and Foreign Language Programs</div>
  <div class="personal-url">  </div>
      <div class="email"> <a href="mailto:anolatu1@uno.edu">anolatu1@uno.edu</a> </div>
  <div class="phone"> <a href="tel:504-280-6275">504-280-6275</a> </div>
</div>
```

In this example, the **parent tag** would be `personal-info`.

Next, the user will be prompted for the **child tags**. The user can enter **class tags** or **CSS selector tags**. In the above example, the possible child class tags would be `name`, `professional-titles`,`email` and `phone`.

The user can press `Enter` to decline entering either the class tags or CSS selector tags. 
