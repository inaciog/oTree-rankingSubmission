from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from . import widgets as school_choice_widgets

import random

author = 'Your name here'

doc = """
Demo for preference submission widget.
"""


class Constants(BaseConstants):
    name_in_url = 'school_choice'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ### Here is the part where you define the options available for the participant.
    ###
    # Randomly generate items
    styleColor={}
    styleColor[0]="#009EA0"
    styleColor[1]="#FB3640"
    styleColor[2]="#605F5E"
    styleColor[3]="#F46036"
    styleColor[4]="#FFBA49"
    choicesButtons=[]
    for i in range(40):
        colorNum=random.choice([0,1,2,3,4])
        choicesButtons.append((i,'Object '+str(i),styleColor[colorNum]))
    objectChoicesParams ={
        'itemsToChoose':choicesButtons,
        'maxNumOptions':5
    }


    preference = models.TextField(widget=school_choice_widgets.OrderedChoice(
        choices=objectChoicesParams))
