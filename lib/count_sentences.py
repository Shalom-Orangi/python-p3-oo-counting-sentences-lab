#!/usr/bin/env python3

class MyString:
  def __init__(self,initial_value=None):
    self._value=None
    if initial_value is not None:
          self.value = initial_value

    @property
    def value(self):
      return self._value
    
    @value.setter
    def value(self,new_value):
      if isinstance(new_value,str):
        self._value=new_value

      else:
        print("Value must be a string")

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    sentences = [sentence.strip() for sentence in sentences.split(r'[.!?]', self._value) if sentence]
      return len(sentences)