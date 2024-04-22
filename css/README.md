## CSS - Cascading Style Sheets

<br>

- color : text color
- width / height : px / %
- padding : how much space should be left inside element
- margin : how much space should be left outside element
- font-family : type of font for text on page
- font-size : px
- border : size type(solid, dashed, etc.) color

### Ways to determine HTML elements

- element type : styling all elements of same type
- id : no 2 elements can have same id & no element can have more than 1 id

``` html
    <h1 id= "first-header">Hello</h1>
```

<br>

- class : can be shared by more than 1 element & single element can have more than 1 class

```html
<!--page-text & muted class-->
<h1 class= "page-text muted">Hello</h1>
```

<br>

### Specificity orer

1. In-line styling
2. id
3. class
4. element type

<br>

### speifying elements

- a, b : multiple element selector
- a b : descendant selector
- a > b : child selector
- a + b : adjacent sibling selector
- [a = b] : attribute selector
- a : b : pseudoclass selector
- a :: b : pseudoelement selector

<br>

### CSS pseudoclass

- provides additional styling during special circumstances
- element looks like under certain conditions
