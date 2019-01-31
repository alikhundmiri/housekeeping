# importing the general posting post from forms folder.
# THIS SCRIPT IS WORKING FINE - 12/september/2018

from forms.general_form_filler import post_advert



PUBLISH = False

page_link = 'https://www.expatriates.com/scripts/posting/poststep_region.epl?region_id=1055-Jeddah&category_id=229&category_title=Education'

locality = "Azzizyah - Near Chennai Darbar"

title_text = "Tuitions for Girls by a Female Instructor (Kindergarten to 6th standards)."

mobile = '0565179202'

description = '''
Taught by a friendly female coach, looking to improve girls education understanding.

Available for classes from Kindergarten up to 6th class.

Openings open for limited seats.


S U B J E C T S :

* English Reading & Writing,
* Social Studies,
* Mathematics,
* Science.



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