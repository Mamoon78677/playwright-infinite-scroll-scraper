import os
os.system('cls')
import asyncio
import json
import random
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
scraped_cars = []
async def handle_responce(responce):
    if responce.status == 200 and 'test-sites-ajax?' in  responce.url:
        data = await responce.text()
        print(f"Clean data {data}")

async def run():
    try:
        async with async_playwright() as ap:
            browser = await ap.chromium.launch(
                headless=False,
                slow_mo=600,
                channel='chrome'
            )
            context = await browser.new_context(
                            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                            viewport={'width':1920,'height':1080},
                            locale='en-US',
                            timezone_id='America/New_York'
            )
            page = await context.new_page()
            await Stealth().apply_stealth_async(page)
            
            await page.goto('https://webscraper.io/test-sites/scroll')
            await asyncio.sleep(random.uniform(1,3))
            last_height = await page.evaluate("document.body.scrollHeight")
            while True:
                await page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
                await asyncio.sleep(random.randint(2,3))
                new_height = await page.evaluate("document.body.scrollHeight")
                if new_height == last_height:
                    print('Ended...!')
                    break
                else:
                    last_height = new_height
            car_elements = page.locator('div.col-md-4')
            total_cars = await car_elements.count()
            print('Total cars:',total_cars)
            for car in await car_elements.all():
                title = await car.locator('h3.card-title').text_content()
                link = await car.locator('h3.card-title a').get_attribute('href')
                description = await car.locator('[itemprop="description"]').text_content()
                price = await car.locator('[itemprop="price"]').text_content()
                year = await car.locator('p.card-text').filter(has_text="Year:").text_content()
                year = year.replace('Year:','').strip()
                country = await car.locator('p.card-text').filter(has_text="Country of origin:").text_content()
                country = country.replace('Country of origin:','').strip()
                mileage = await car.locator('p.card-text').filter(has_text="Mileage").text_content()
                mileage = mileage.replace('Mileage:','').strip()
                car_data = {
                    "Title":title.strip(),
                    "Details":{"Description":description.strip(),
                    "Price":price.strip(),
                    "Year":year,
                    "Country": country,
                    "Mileage":mileage,
                    "For more info link is here":{"Link":link}}


                }
                scraped_cars.append(car_data)
                

            with open("car2.json","w",encoding='utf-8') as my_file:
                json.dump(scraped_cars,my_file,indent=4)
            await context.close()
            await browser.close()
    except Exception as e:
        print(f'Erorr {e}')
if __name__ == '__main__':
    asyncio.run(run())
