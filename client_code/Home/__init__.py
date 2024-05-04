from ._anvil_designer import HomeTemplate
from anvil import *
from ..State_gov_schemes import State_gov_schemes


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    state_gov_schemes = State_gov_schemes()
    open_form(state_gov_schemes)
    print("clicked on form")
  
    pass
