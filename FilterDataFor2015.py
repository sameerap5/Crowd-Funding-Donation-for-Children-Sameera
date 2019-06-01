# This files filters all datasets for year 2015
# Write the outcome to excel files

import sys
import pandas as pd

# Filter data for 2015
giftcards = pd.read_csv('D:\\USF\Selenium\opendata_giftcards000.gz', escapechar='\\', names=['_giftcardid', 'dollar_tier', '_buyer_acctid', 'buyer_city', 'buyer_state', 'buyer_zip', 'date_purchased', '_buyer_cartid', '_recipient_acctid', 'recipient_city', 'recipient_state', 'recipient_zip', 'redeemed', 'date_redeemed', '_redeemed_cartid', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched'])
giftcards_2015=giftcards[(giftcards['date_purchased'].apply(lambda x:x[0:4]) == '2015')]                #year = 2015
giftcards_2015.to_csv('D:\\USF\Selenium\giftcards_2015_modified1.csv')

# Filter data for 2015
projects = pd.read_csv('D:\\USF\Selenium\opendata_projects000.gz', escapechar='\\', names=['_projectid', '_teacher_acctid', '_schoolid', 'school_ncesid', 'school_latitude', 'school_longitude', 'school_city', 'school_state', 'school_zip', 'school_metro', 'school_district', 'school_county', 'school_charter', 'school_magnet', 'school_year_round', 'school_nlns', 'school_kipp', 'school_charter_ready_promise', 'teacher_prefix', 'teacher_teach_for_america', 'teacher_ny_teaching_fellow', 'primary_focus_subject', 'primary_focus_area' ,'secondary_focus_subject', 'secondary_focus_area', 'resource_type', 'poverty_level', 'grade_level', 'vendor_shipping_charges', 'sales_tax', 'payment_processing_charges', 'fulfillment_labor_materials', 'total_price_excluding_optional_support', 'total_price_including_optional_support', 'students_reached', 'total_donations', 'num_donors', 'eligible_double_your_impact_match', 'eligible_almost_home_match', 'funding_status', 'date_posted', 'date_completed', 'date_thank_you_packet_mailed', 'date_expiration'])
projects_2015=projects [(projects ['date_posted'].apply(lambda x:x[0:4]) == '2015')]
projects_2015.to_csv('D:\\USF\Selenium\projects_2015_modified1.csv')

#donations
donations = pd.read_csv('D:\\USF\Selenium\opendata_donations000.gz', escapechar='\\', names=['_donationid', '_projectid', '_donor_acctid', '_cartid', 'donor_city', 'donor_state', 'donor_zip', 'is_teacher_acct', 'donation_timestamp', 'donation_to_project', 'donation_optional_support', 'donation_total', 'donation_included_optional_support', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched', 'is_teacher_referred', 'giving_page_id', 'giving_page_type', 'for_honoree', 'thank_you_packet_mailed'])

donations.to_csv('D:\\USF\Selenium\donations_2015_old.csv') #//converted to csv file
projects.to_csv('D:\\USF\Selenium\projects_2015_old.csv')      #//converted to csv file
df=pd.merge(projects,donations,how='inner', on ='_projectid')		#merge 2 files for common id = project id and date_completed
don_projects_2015=df [(df['date_posted'].apply(lambda x:x[0:4]) == '2015')]
don_projects_2015.to_csv('D:\\USF\Selenium\don_projects_2015_old.csv') 

# resources
resources = pd.read_csv('D:\\USF\Selenium\opendata_resources000.gz', escapechar='\\', names=['_resourceid', '_projectid', 'vendorid', 'vendor_name', 'item_name', 'item_number', 'item_unit_price', 'item_quantity'])

#essays
essays = pandas.read_csv('opendata_essays000.gz', escapechar='\\', names=['_projectid', '_teacherid', 'title', 'short_description', 'need_statement', 'essay', 'thankyou_note', 'impact_letter'])
essay_project=pd.merge(projects,essays,how='inner', on ='_projectid')
essay_project=essay_project [(essay_project['date_posted'].apply(lambda x:x[0:4]) == '2015')]
essay_project.to_csv('D:\\USF\Selenium\essay_projects_2015_old.csv') 

#giving pages
giving_pages = pd.read_csv('opendata_giving_pages000.gz', escapechar='\\', names=['giving_page_id', '_creator_acctid', 'created_date', 'is_active', 'most_recent_donation', 'amount_raised', 'number_of_donors', 'number_of_students', 'number_of_projects_supported', 'number_of_teachers', 'number_of_schools'])
giving_project=pd.merge(projects,giving_pages,how='inner', on ='_projectid')
giving_project=giving_project [(giving_project['date_posted'].apply(lambda x:x[0:4]) == '2015')]
giving_project.to_csv('D:\\USF\Selenium\essay_projects_2015_old.csv') 

#giving_page_projects
giving_page_projects = pd.read_csv('opendata_giving_page_projects000.gz', escapechar='\\', names=['giving_page_id', '_projectid'])
giving_page_projects_merge=pd.merge(projects,giving_page_projects,how='inner', on ='_projectid')
giving_page_projects_merge=giving_page_projects_merge [(giving_page_projects_merge['date_posted'].apply(lambda x:x[0:4]) == '2015')]
giving_page_projects_merge.to_csv('D:\\USF\Selenium\essay_projects_2015_old.csv') 
