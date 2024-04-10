1) We have SBI stock Open, high, low, close and volume data for every minute for every day
2) The data is from 1st Jan 2024 till 31st Jan 2024 ( Each day having 375 rows of data i.e. 915 am till 329 pm)
3) We have to rank the volume in a such a way that it checks the exact same time for every day and for the last 5 days, it gives us the rank of volume ( rank 1 means highest volume)


so if we are analysing on 31st Jan 930 am volume, so we will compare the 930 am volume of 30th Jan, 29th Jan, 28th Jan, 27th Jan and 26th Jan ( working days) and then give a rank to it 
The output shall be stored in the current dataframe as  a new column "rank"
