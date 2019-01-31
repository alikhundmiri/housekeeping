# importing the general posting post from forms folder.
# THIS SCRIPT IS WORKING FINE - 12/september/2018

from forms.general_form_filler import post_advert



PUBLISH = False

page_link = 'https://www.expatriates.com/scripts/posting/poststep_region.epl?region_id=1055-Jeddah&category_id=3002&category_title=Businesses%20For%20Sale'

locality = "Azzizyah - Near Sameera polyclinic"

title_text = "A profitable Kindergarten for sale, with all essential furniture and teaching materials."

mobile = '0593427719'

description = '''
A Well established and profitable Kindergarten is for sale.

The deal includes:

> Tables and chairs, enough to seat more than 30 students.
> Projector with Screen.
> Kid's toys.
> Kid's small swing, and slide.
> All the unique teaching material, written by us, for students of
---> Nursery
---> LKG
---> UKG


School is currently teaching to students of Indian, Pakistani and even Saudi education system.

You can start generating revenue right away.

Visit us to inquire about the revenue, profits and other financial details.

Location: 
Behind Chennai Darbar. 
Near to Sameera polyclinic. Al Aziziyah. 

Visiting hours: 
1:00 PM - 4:00 PM 

Call to book an appointment: 059 342 7719
'''

e_address = "salikhundmiri@gmail.com"


if __name__ == '__main__':
    post_advert(page_link, locality, title_text, mobile, description, e_address, PUBLISH)