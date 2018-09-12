# importing the general posting post from forms folder.
# THIS SCRIPT IS WORKING FINE - 12/september/2018

from forms.general_form_filler import post_advert



PUBLISH = False

page_link = 'https://www.expatriates.com/scripts/posting/poststep_region.epl?region_id=1055-Jeddah&category_id=229&category_title=Education'

locality = "Azzizyah - Near Chennai Darbar"

title_text = "Tutions for 5th to 10th Girls by female a teacher."

mobile = '0565179202'

description = '''
Taught by a friendly female teacher, looking to help girls study better, for classes from 5th up to 10th.

Slots open for limited seats.


S U B J E C T S :

* Social Studies,
* Science,
* Maths,
* 



L O C A T I O N :

Behind Chennai Darbar. 
Near to Sameera polyclinic. Al Aziziyah. 



T I M I N G S :

1:00 PM - 4:00 PM



C O N T A C T    U S :

You can call us for More Information: 056 517 9202
(click on the number in Advert post)
'''

e_address = "salikhundmiri@gmail.com"


if __name__ == '__main__':
    post_advert(page_link, locality, title_text, mobile, description, e_address, PUBLISH)