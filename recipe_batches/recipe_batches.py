#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 100000000
  ingVals = list(ingredients.values())
  recipeVals = list(recipe.values())

  if len(ingVals) < len(recipeVals):
    batches = 0
  elif len(ingVals) == 1 and len(recipeVals) == 1:
    batches = ingVals[0] / recipeVals[0]
  else:
    for i in range(len(recipe) - 1):
      if ingVals[i] / recipeVals[i] < batches:
        batches = ingVals[i] / recipeVals[i]

  return math.floor(batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))