# oTree-rankingSubmission
A widget in oTree for submitting an ordered ranking over a finite set of options

# Description

This widget allows for subjects to submit an ordered list, of arbitrary maximum length, over a given set of options. Examples of uses include:

* The submission of preferences over a set of options
* The submission of a choice over a set of options
* The selection of a subset of objects

The use of the widget is as follows. In the left pane are listes the set of options available. When the user clicks on an option, that is moved to the right pane. Objects are ordered in the right pane in the order in which they are clicked. Once the maximum number of options are chosen, no more can be added.

The user may change the ranking by:

* Clicking in a selected option in the right pane. This will remove it and put it back to the left pane.
* By dragging and dropping the options in the right pane (currently this only works in Google Chrome)

# Usage

When defining the model for the player, you can define the use of the widget as follows:


```python
preference = models.TextField(widget=school_choice_widgets.OrderedChoice(choices=objectChoicesParams))
```

The parameter `objectChoicesParams` is a dictionary with two items:

```python
objectChoicesParams ={
        'itemsToChoose':choicesButtons,
        'maxNumOptions':3
    }
```

`maxNumOptions` is the maximum number of items a user can select, and `itemsToChoose` is a list of tuples with 3 items:

```python
choicesButtons =[
        ('val1','Label 1','#009EA0'),
        ('val2','Label 2','#FB3640'),
        ('val3','Label 3','#FB3640')
    ]
```

The first value is a string representing the value associated with the item. This is the value that will be sent back in oTree. The second value is the string used in the button. The third item is the color of the button.

The value returned by the widget are the values, separated by commas. For example:

```preference='val2,val3,val1'```


