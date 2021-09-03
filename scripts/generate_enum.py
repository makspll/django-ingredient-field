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
    props = np.genfromtxt(
        os.path.join(os.path.dirname(sys.argv[1]),'props.csv'),
        delimiter=',',
        dtype=None,
        encoding='utf-8')

    processed = []

    for idx,ing in enumerate(data):
        if str(ing) in INGREDIENT_BLACKLIST or len(str(ing)) < MIN_LENGTH:
            continue
        
        clean = ''.join([c for c in str(ing).upper().replace(' ','_') if c.isalnum() or c == '_'])

        row = None
        for r in props:
            if clean == r[0]:
                row = r
                break
        else:
            raise Exception("{} does not have an entry in props.csv".format(clean))

        this_props = {props[0][idx]:row[idx] for idx in range(1,props.shape[1])} 
        processed.append({
            'original':str(ing),
            'capitalized':'I_'+clean,
            'db_rep':clean,
            'form_rep':str(ing).title(),
            'props': {**this_props}
        })

    # sort it for nice enum.py formatting
    processed.sort(key= lambda x: x['original'])

    # output python file
    with open(sys.argv[2],'w+') as out_file:
        out_file.write('from django.utils.translation import gettext_lazy as _\n')
        out_file.write('from django.db import models\n')
        out_file.write('class IngredientName(ChoicesWithProperties):\n')
        
        for ingredient in processed:
            out_file.write("\t{capitalized} = '{db_rep}', _('{form_rep}'),{{ {props} }} #{original}\n"
                .format(**{**ingredient,
                    "props":",".join(["'{}':{}".format(k,ingredient['props'][k] if ingredient['props'][k] else None) for k in ingredient['props']])
                    }))