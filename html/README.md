## HTML

- Markup lang defines structure of web page
- Interpreted by web browser in order to display content on screen
- HTML elements can include attributes 

&emsp; &emsp;&emsp;&emsp; -> give browser extra information about element

<br>

### Document Object Model - DOM

- Convenient way of visualizing the way HTML elements relate to each other using a tree-like structure


<br>

### Meta

- Meta tags are used to hold information about data within HTML file

``` html
<meta name="viewport" content="initial-scale=1, width=device-width">
```
- This set of meta attributes makes page mobile-friendly

<br><br>

``` html
<meta property="og:title" content="ITM">
<meta property="og:description" content="Introduction to HTML">
<meta property="og:image" content="pochacco.png"> 
```
- Key value pairs relate to title and description of page

<br><br>

### Form

```html
        <form action="https://www.google.com/search" method="get">
            <input name="q" type="search">
            <input type="submit" value="Google Search">
        </form>
```
- Can create forms reminiscent of Google's search
- Form tag opens and provides attribute of what action it will take
- Input field is included, passing the name 'q' and type as 'search'

<br><br>

##### \<form>

- action : choose script file of server to send form
- name : set name to identify
- accept-charset : set charset encoding using for sending forms
- method : set http method to send form to server
- target : set to open script file that set by action in other location (not current window)

<br>

##### \<input>

- type : text, checkbox, email, radio, password, button, hidden, submit, reset, etc.
- name : name of tag
- maxlength : set maximum number of char length of tag
- required : the tag is set to essential tag (print error message if user do not input)
- placeholder : give hint of input value of tag
- pattern : use regular expression to get valid value within specific range

##### \<div>
- used to divide up HTML file into specific regions
- everything inside body is child of body

<br><br>

