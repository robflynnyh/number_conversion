# number_conversion

For use with num2words (pls install)

- num2words converts numbers to their alphabetic form
- it only handles numbers, i.e you can't pass it a text document that includes numbers and text
- use this lib to do just that, it will convert a text document with numbers in to just text
- I make the assumption that 4 digit numbers i.e 1978 between 1500 and 2100 are dates, otherwise I treat stuff as regular numbers
- my use-case if for prepping ASR training datasets where you typically don't want numbers in there numeric form
- won't work for weird edge cases
- WiP

# usage

> import number_conversion 
> 
> text = "it is the year 2022 and this is a 2test string"
> 
> text = number_conversion.convert_doc(text)
> 
> print(text) # it is the year twenty twenty-two and this is a two test string
