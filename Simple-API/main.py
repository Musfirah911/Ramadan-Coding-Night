from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - start offering your skills online",
    "Dropshipping - start an online store with print on demand",
    "Affiliate Marketing - promote products and earn commissions",
    "Etsy - sell handmade or vintage items",
    "Amazon FBA - start a dropshipping business on Amazon",
    "Youtube - start a channel and monetize with ads",
    "Print on demand - start a print on demand business",
    "Social media marketing - start a social media marketing business",
    "Graphic design - start a graphic design business",
    "Video editing - start a video editing business",
    "Web development - start a web development business",
    "SEO - start a SEO business",
    "Content creation - start a content creation business",
    "Crypto trading - start a crypto trading business",
    "Stock market - Invest and watch your money grow",
    "Real estate - Buy a property and rent it out",
    "Online courses - share your knowledge and make money",
    "Blogging - Create content and earn through ads and sponsorships",
    "Podcasting - Start a podcast and monetize with ads",
    "Videography - Start a videography business",
    "Photography - Start a photography business",
    "Virtual assistant - Start a virtual assistant business",
    "Data entry - Start a data entry business",   
]

money_quotes = [
    "The only way to do great work is to love what you do. by Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. by Albert Einstein",
    "I've failed over and over and over again in my life and that is why I succeed. by Thomas Edison",
    "Don't watch the clock; do what it does. Keep going. by Charles Schultz",
    "The best way to predict the future is to invent it. by Alan Kay",
    "The only limit to our realization of tomorrow is our doubts of today. by Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. by Eleanor Roosevelt",
    "The only way to do great work is to love what you do. by Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. by Albert Einstein",
    "I've failed over and over and over again in my life and that is why I succeed. by Thomas Edison",
    "Don't watch the clock; do what it does. Keep going. by Charles Schultz  ",
    "The best way to predict the future is to invent it. by Alan Kay",
    "The only limit to our realization of tomorrow is our doubts of today. by Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. by Eleanor Roosevelt",
]


@app.get("/side_hustles")
def get_side_hustles():
    """Return a random side hustle idea"""
    return {"side_hustles": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Return a random money quote"""
    return {"money_quotes": random.choice(money_quotes)}