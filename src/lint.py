# In order to add a check you just have to create a function that 
# receives an instance of ITXMap and returns a boolean and a fixer.
# Of course, the boolean indicates if the check was successful
# (i.e. the map complies with it)
# After that, add your function to the `checks` list in the
# `lint` function!

def map_trace_off(itx_map):
    correct = itx_map.tree().find('./Map/MapSettings/MapTrace').get('Switch') == 'OFF'
    fixer = lambda map: map.tree().find('./Map/MapSettings/MapTrace').set('Switch', 'OFF')
    return correct, fixer

def lint(itx_map):
    checks = [
        map_trace_off,
    ]

    return map(lambda check: check(itx_map), checks)

def fix(itx_map, results):
    for result in results:
        successful, fixer = result
        if not successful:
            fixer(itx_map)
    
    return itx_map
