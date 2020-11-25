def namelist(names):
    str = ''
    if len(names) != 0:
      arr = []
      for i in range(0, len(names) - 1):
          arr.append(names[i]['name'])
      str = ', '.join(arr)
      str += ' & ' + names[-1]['name'] if str != '' else names[-1]['name']
     
    return print(str)










namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'
