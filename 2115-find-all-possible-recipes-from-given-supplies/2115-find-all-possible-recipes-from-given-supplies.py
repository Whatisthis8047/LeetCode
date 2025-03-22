class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)  # 빠른 조회를 위해 set 사용
        reci_dict = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        result = []

        while True:
            found_recipe = False
            
            for recipe, ingredient_list in list(reci_dict.items()):
                if all(ing in supplies for ing in ingredient_list):
                    result.append(recipe)
                    supplies.add(recipe) 
                    del reci_dict[recipe]  
                    found_recipe = True  
            
            if not found_recipe: 
                break

        return result