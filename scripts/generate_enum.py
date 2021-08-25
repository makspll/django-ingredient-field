import numpy as np
import sys
import os

INGREDIENT_BLACKLIST= set([
    's',
    'sun-dried tomatoes',
    '1% low-fat milk',
    'a'
])

MIN_LENGTH = 2

if __name__ == "__main__":

    # prepare data
    data = np.load(sys.argv[1])

    processed = []

    for idx,ing in enumerate(data):
        if str(ing) in INGREDIENT_BLACKLIST or len(str(ing)) < MIN_LENGTH:
            continue

        clean = ''.join([c for c in str(ing).upper().replace(' ','_') if c.isalnum() or c == '_'])
        processed.append({
            'original':str(ing),
            'capitalized':'I_'+clean,
            'db_rep':clean,
            'form_rep':str(ing).title(),
        })

    # sort it for nice enum.py formatting
    processed.sort(key= lambda x: x['original'])

    # output python file
    with open(sys.argv[2],'w+') as out_file:
        out_file.write('from django.utils.translation import gettext_lazy as _\n')
        out_file.write('from django.db import models\n')
        out_file.write('class IngredientName(models.TextChoices):\n')
        
        for ingredient in processed:
            out_file.write("\t{capitalized} = '{db_rep}', _('{form_rep}') #{original}\n"
                .format(**ingredient))