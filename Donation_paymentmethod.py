#
import pandas as pd
donations = pd.read_csv('D:\\USF\Selenium\opendata_donations000.gz', escapechar='\\', names=['_donationid', '_projectid', '_donor_acctid', '_cartid', 'donor_city', 'donor_state', 'donor_zip', 'is_teacher_acct', 'donation_timestamp', 'donation_to_project', 'donation_optional_support', 'donation_total', 'donation_included_optional_support', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched', 'is_teacher_referred', 'giving_page_id', 'giving_page_type', 'for_honoree', 'thank_you_packet_mailed'])
donations.to_csv('D://USF/Selenium/donations.csv')    #loading file into csv


#distinguising according to the year
donations_01=donations[(donations['donation_timestamp'].apply(lambda x:x[0:4]) == '2001')]
donations_01.head()

#selecting only 2 columns
donations_01=donations_01[['donation_timestamp','payment_method']]

#split the date 
donations_01["donation_timestamp"]= donations_01["donation_timestamp"].str.split(" ", n = 1, expand = True) 

# to display data according to the payment_method of the particular year
data01=donations_01.groupby(['payment_method'])['donation_timestamp'].count()
data01