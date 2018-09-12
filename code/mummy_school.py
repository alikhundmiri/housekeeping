# importing the general posting post from forms folder.
# THIS SCRIPT IS WORKING FINE - 12/september/2018

from forms.general_form_filler import post_advert



PUBLISH = False

page_link = 'http://expatriates.com/scripts/posting/poststep_region.epl?region_id=1055-Jeddah&category_id=158&category_title=Nursery%20Schools'

locality = "Azzizyah - Near Chennai Darbar"

title_text = "Star Play Group - Best Kindergarten for your kids"

mobile = '0565179202'

description = '''
The Best Kindergarten for your kids has moved to a *new* location! 

We are accepting new students now! 

* Lots of toys and props for kids to play with. 
* Taught by Affectionate Indian teachers, 
* Suitable Furniture for the kids, 
* Study Material is provided. 
* Overhead projector, 

Curiosity starts here. 
Nurturing starts here. 
Learning starts, here. 

Official Star Play Group website: https://goo.gl/iW6LLj 

Location: 
Behind Chennai Darbar. 
Near to Sameera polyclinic. Al Aziziyah. 

Visiting hours to be followed STRICTLY: 
1:00 PM - 4:00 PM 

Call to book an appointment: 056 517 9202

'''
e_address = "salikhundmiri@gmail.com"


if __name__ == '__main__':
	post_advert(page_link, locality, title_text, mobile, description, e_address, PUBLISH)