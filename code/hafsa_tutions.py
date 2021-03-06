# importing the general posting post from forms folder.
# THIS SCRIPT IS WORKING FINE - 12/september/2018

from forms.general_form_filler import post_advert



PUBLISH = False

page_link = 'https://www.expatriates.com/scripts/posting/poststep_region.epl?region_id=1055-Jeddah&category_id=229&category_title=Education'

locality = "Azzizyah - Near Sameera polyclinic"

title_text = "Tuitons for LKG to 6th Grade Girls by a female Instructor."

mobile = '0565179202'

description = '''
Taught by a friendly female teacher, looking to help girls study better, for classes from LKG - 6th grade.
Slots open for limited seats.


I can help your child study, the following subjects,:
* Social Studies,
* Science,
* Maths.
(and more, if requested.)


My location:
Behind Chennai Darbar.
Near to Sameera polyclinic. Al Aziziyah. 


Classes timing:
1:00 PM - 4:00 PM



To get in touch, with me, contact using this number:
056 517 9202
or simply byclick on the number in Advert post.
'''

e_address = "salikhundmiri@gmail.com"


if __name__ == '__main__':
    post_advert(page_link, locality, title_text, mobile, description, e_address, PUBLISH)