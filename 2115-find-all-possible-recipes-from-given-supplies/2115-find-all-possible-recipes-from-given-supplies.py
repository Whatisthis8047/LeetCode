class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        reci_dict = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        result = []

        while True:
            found_recipe = False
            
            for recipe, ingredient_list in list(reci_dict.items()):
                if set(ingredient_list) <= set(supplies):
                    result.append(recipe)
                    supplies.append(recipe) 
                    del reci_dict[recipe]  
                    found_recipe = True  
            
            if not found_recipe: 
                break

        return result