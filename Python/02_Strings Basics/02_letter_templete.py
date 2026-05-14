# Fill the letter template with name and date.
# letter = '''
#          Dear <|Name|>,
#          You are selected!
#          <|Date|>
#          '''
         

letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''
print(letter.replace("Name","Hammad Ali").replace("Date","14-Mar-2006"))

# It replaces Name and Date as string