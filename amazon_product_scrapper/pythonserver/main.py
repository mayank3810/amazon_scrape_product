from selenium import webdriver
from time import sleep

def get_details(websiteurl):

    ref_link ="""&tag=festivalkart2-21"""
    ####### Change Website Seeded Here #####

    website = websiteurl


    #***************************************

    # VARIABLES
    image_url0 = []
    image_url1 = []
    image_url2 = []
    image_url3 = []
    image_url4 = []
    image_url5 = []
    image_url6 = []
    image_url7 = []
    image_url8 = []
    image_url_all = []
    driver = webdriver.Chrome(executable_path='C:\Projects\Web Scrapping\Amazon Products\Drivers\chromedriver')
    driver.get(website)
    sleep(1)

    # PROUDUCT URL

    product_url = website + ref_link

    #  PRODUCT NAME
    product_tag = driver.find_element_by_id("productTitle")
    product_name = product_tag.get_attribute('innerHTML').strip()

    # AMAZON FULFILLED
    try:
        driver.find_element_by_xpath('//*[@id="price-shipping-message"]/i')
        amazon_fulfilled = 'Yes'
    except Exception:
        amazon_fulfilled = 'No'
    # PRODUCT MRP
    product_mrp_tag = driver.find_element_by_class_name('priceBlockStrikePriceString')
    tail = product_mrp_tag.get_attribute('innerHTML').strip()
    head, sep, product_mrp = tail.partition('₹&nbsp;')
    # PRODUCT PRICE
    try:
        product_price_tag = driver.find_element_by_id('priceblock_ourprice')
    except Exception:
        product_price_tag = driver.find_element_by_id('priceblock_saleprice')
    tail1 = product_price_tag.get_attribute('innerHTML').strip()
    head1, sep1, product_price = tail1.partition('₹&nbsp;')
    product_price.replace('₹&nbsp;','')

    # EMI OPTION
    try:
        driver.find_element_by_class_name('inemi-options-activate-popover')
        emi_option = 'EMI Option Avaliable'
    except Exception:
        emi_option = 'EMI Option Not Avaliable'

    # RATING STAR
    rating = driver.find_element_by_class_name('a-icon-alt').get_attribute('innerHTML')
    head4, sep4, tail4 = rating.partition(' out')
    if tail4 == " of 5 stars":
        product_rating = head4
    else:
        product_rating ="Not Rated"
    #head4 = head4 + ' Stars'
    # NUMBER OF REVIEWS
    try:
        head5 = driver.find_element_by_id('acrCustomerReviewText').get_attribute('innerHTML') 
        number_of_reviews, sep5, tail5 = head5.partition(' ratings')
        number_of_reviews = number_of_reviews + ' Reviews'
    except Exception:
        number_of_reviews = "No Reviews"

    # PRODUCT DESCRIPTION
    product_description_final = []
    product_descriptionl = driver.find_elements_by_xpath('//*[@id="feature-bullets"]/ul/li')
    for i in range(0 , len(product_descriptionl)):
        product_descriptiont = product_descriptionl[i].find_element_by_class_name('a-list-item')
        product_description = product_descriptiont.get_attribute('innerHTML').strip()
        product_description_final.append(product_description)
    product_description_final = str(product_description_final)

    # PRODUCT IMAGE
    next_image = driver.find_elements_by_class_name('imageThumbnail')
    for i in range(0,len(next_image)):
        next_image[i].click()
        sleep(0.2)
    for i in range(0,len(next_image)):
        if (i==0):
            image_url_list = driver.find_element_by_class_name("itemNo0")
            image_url_t1 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            header_image = str(image_url_t1)
        elif (i==1):
            image_url_list = driver.find_element_by_class_name("itemNo1")
            image_url_t2 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url1 = str(image_url_t2)
            image_url_all = image_url1 + '|'
        elif (i==2):
            image_url_list = driver.find_element_by_class_name("itemNo2")
            image_url_t2 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url2 = str(image_url_t2)
            image_url_all =image_url_all + image_url2 + '|'
        elif (i==3):
            image_url_list = driver.find_element_by_class_name("itemNo3")
            image_url_t3 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url3 = str(image_url_t3)
            image_url_all =image_url_all + image_url3 + '|'
        elif (i==4):
            image_url_list = driver.find_element_by_class_name("itemNo4")
            image_url_t4 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url4 = str(image_url_t4)
            image_url_all =image_url_all + image_url4 + '|'
        elif (i==5):
            image_url_list = driver.find_element_by_class_name("itemNo5")
            image_url_t5 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url5 = str(image_url_t5)
            image_url_all =image_url_all + image_url5 + '|'
        elif (i==6):
            image_url_list = driver.find_element_by_class_name("itemNo6")
            image_url_t6 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url6 = str(image_url_t6)
            image_url_all =image_url_all + image_url6 + '|'
        elif (i==7):
            image_url_list = driver.find_element_by_class_name("itemNo7")
            image_url_t7 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url7 = str(image_url_t7) 
            image_url_all =image_url_all + image_url7 + '|'
        elif (i==8):
            image_url_list = driver.find_element_by_class_name("itemNo8")
            image_url_t8 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
            image_url8 = str(image_url_t8)
            image_url_all =image_url_all + image_url8 + '|'
    # PRINTING PRODUCT DETAILS TO CONSOLE
    print("NAME:                 ",product_name)
    print("URL:                  ",product_url)
    print("MRP:                  ",product_mrp)
    print("PRICE:                ",product_price)
    print("HEADER IMAGE:         ",header_image)
    print("IMAGE URLS:           ",image_url_all)
    print("DESCRIPTION:          ",product_description_final)
    print("REVIEWS:              ",number_of_reviews)
    print("RATING:               ",product_rating)
    print("AMAZON FULFILLED:     ",amazon_fulfilled)
    print("EMI OPTION:           ",emi_option)
    
    
    

    driver.close()

