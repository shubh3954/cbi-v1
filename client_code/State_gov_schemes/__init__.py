from ._anvil_designer import State_gov_schemesTemplate
from anvil import *


class State_gov_schemes(State_gov_schemesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
