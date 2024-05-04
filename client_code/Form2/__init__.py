from ._anvil_designer import Form2Template
from anvil import *


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
