#to check the essay text message written
import sys
import pandas as pd

#argv[1]='D:\\USF\Selenium\opendata_essays000.gz'
#argv[2]='D:\\USF\Selenium\opendata_projects000.gz'
#argv[3]='D:\\USF\Selenium\funding_status.csv'

#essay
essay = pd.read_csv(sys.argv[1], escapechar='\\', names=['_projectid', '_teacherid', 'title', 'short_description', 'need_statement', 'essay', 'thankyou_note', 'impact_letter'])

#projects 
projects = pd.read_csv(sys.argv[2], escapechar='\\', names=['_projectid', '_teacher_acctid', '_schoolid', 'school_ncesid', 'school_latitude', 'school_longitude', 'school_city', 'school_state', 'school_zip', 'school_metro', 'school_district', 'school_county', 'school_charter', 'school_magnet', 'school_year_round', 'school_nlns', 'school_kipp', 'school_charter_ready_promise', 'teacher_prefix', 'teacher_teach_for_america', 'teacher_ny_teaching_fellow', 'primary_focus_subject', 'primary_focus_area' ,'secondary_focus_subject', 'secondary_focus_area', 'resource_type', 'poverty_level', 'grade_level', 'vendor_shipping_charges', 'sales_tax', 'payment_processing_charges', 'fulfillment_labor_materials', 'total_price_excluding_optional_support', 'total_price_including_optional_support', 'students_reached', 'total_donations', 'num_donors', 'eligible_double_your_impact_match', 'eligible_almost_home_match', 'funding_status', 'date_posted', 'date_completed', 'date_thank_you_packet_mailed', 'date_expiration'])

#merge essay and project
newdata=pd.merge(projects,essay,how='inner',on='_projectid')

# Filter the data for respective year from donations data
projects_2015=newdata[(newdata['date_posted'].apply(lambda x:x[0:4]) == '2015')]

#save it as funding_status.csv
newdata.to_csv(sys.argv[3], sep='\t', encoding='utf-8' )