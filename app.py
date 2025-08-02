from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Main Routes
@app.route('/')
def index():
    return render_template('index.html')  # Changed from 'pages/index.html'

@app.route('/about')
def about():
    process_steps = [
        {
            "number": "01",
            "title": "Farm",
            "subtitle": "Fairtrade & organic coffee",
            "description": "Welcome to a world of coffee where the well-being of the farmers and the land is just as important as the final product in your cup. We work hand in hand with Puro Coffee, our Fairtrade and Organic coffee brand. Puro works directly with farmers to support communities and help preserve the rainforest.",
            "image": "https://ext.same-assets.com/176798368/391877538.webp",
        },
        {
            "number": "02",
            "title": "Protect",
            "subtitle": "Saving the rainforest",
            "description": "When you choose the Office Coffee Company, you're helping to protect the rainforest. We can safeguard 19m² of this precious landscape for every kilo of Puro coffee you purchase. Through our partnership with the World Life Trust, Puro gives back to the Earth, honouring Indigenous sustainability principles.",
            "image": "https://ext.same-assets.com/176798368/1738676429.webp",
        },
        {
            "number": "03",
            "title": "Community",
            "subtitle": "Puro social projects",
            "description": "Through Puro's community initiatives, the Office Coffee Company tangibly improves the lives of local people. We currently contribute to three charitable initiatives: Trees 4 Schools, Coffee Growers of Congo, and Orangutans of Borneo.",
            "image": "https://ext.same-assets.com/176798368/2168801396.webp",
        },
        {
            "number": "04",
            "title": "Create",
            "subtitle": "Coffee roasting",
            "description": "Not just another coffee supplier. Our strength is sourcing coffee worldwide. We are part of Miko Coffee, a family business established over two hundred years. Here in the UK, we roast speciality coffee in one of the regional small-batch coffee roasteries.",
            "image": "https://ext.same-assets.com/176798368/3463438347.webp",
        },
        {
            "number": "05",
            "title": "Balance",
            "subtitle": "Cutting carbon emissions",
            "description": "From growing, processing, and then shipping the beans, the coffee business certainly racks up the miles. That's why the Office Coffee Company believes so strongly in offsetting our carbon emissions. In fact, Puro Coffee is already carbon neutral up until 2024.",
            "image": "https://ext.same-assets.com/176798368/3028666614.webp",
        },
        {
            "number": "06",
            "title": "Taste",
            "subtitle": "Coffee tasting sessions",
            "description": "We love arranging coffee tastings - they're a chance for us to showcase our delicious coffee and build a relationship with you and your team. We'll take you on a fun and engaging journey around the world of our coffee.",
            "image": "https://ext.same-assets.com/176798368/1633516096.webp",
        },
        {
            "number": "07",
            "title": "Install",
            "subtitle": "Getting you started",
            "description": "Following a simple over-the-phone assessment of where you would like your coffee machine installed, we deliver and install your new machine free of charge. On the day, we'll ensure everything is up and running smoothly.",
            "image": "https://ext.same-assets.com/176798368/3963286956.webp",
        },
        {
            "number": "08",
            "title": "Recycle",
            "subtitle": "Sustainable practices",
            "description": "No one likes adding more waste to landfills. To keep your used coffee grounds out of the bin, we can arrange for First Mile and Bio-Bean to collect them from your office. They will process your used grounds into carbon-neutral fuels.",
            "image": "https://ext.same-assets.com/176798368/3469026329.webp",
        },
        {
            "number": "09",
            "title": "Care",
            "subtitle": "Simple, responsive aftercare",
            "description": "Now that you have your new coffee machine, you need top-notch support to keep it running smoothly. Our Total Care package includes all emergency repair calls and regularly scheduled maintenance.",
            "image": "https://ext.same-assets.com/176798368/1486691892.webp",
        },
        {
            "number": "10",
            "title": "Enjoy",
            "subtitle": "Incredible working culture",
            "description": "There's nothing like chatting with colleagues and brainstorming over a great cup of coffee - the ideas just flow more smoothly. At the Office Coffee Company, we believe that great coffee, great times, and great work go hand in hand.",
            "image": "https://ext.same-assets.com/176798368/592214265.webp",
        },
    ]
    return render_template('about.html', process_steps=process_steps)  # Changed from 'pages/about.html'

@app.route('/coffee')
def coffee():
    coffee_ranges = [
        {
            "title": "Puro Coffee",
            "subtitle": "Premium Fairtrade & Organic",
            "description": "Our signature range of ethically sourced, premium coffee beans. Every purchase helps protect the rainforest and supports farming communities.",
            "image": "https://ext.same-assets.com/176798368/862006938.webp",
            "link": "/coffee/puro",
            "features": ["Fairtrade Certified", "Organic", "Rainforest Protection", "Carbon Neutral"],
        },
        {
            "title": "Office Origins",
            "subtitle": "Single Origin Excellence",
            "description": "Discover the unique flavors and characteristics of coffee from specific regions around the world. Perfect for the discerning coffee enthusiast.",
            "image": "https://ext.same-assets.com/176798368/1554632211.webp",
            "link": "/coffee/origins",
            "features": ["Single Origin", "Expertly Roasted", "Unique Profiles", "Premium Quality"],
        },
    ]
    
    sustainability = [
        {
            "icon": "🌳",
            "title": "Rainforest Protection",
            "description": "19m² of rainforest protected for every kilo of Puro coffee purchased",
        },
        {
            "icon": "👥",
            "title": "Community Support",
            "description": "Direct partnerships with farming communities across 8 countries",
        },
        {
            "icon": "♻️",
            "title": "Carbon Neutral",
            "description": "Puro Coffee is carbon neutral through verified offset programs",
        },
        {
            "icon": "🌱",
            "title": "Organic Farming",
            "description": "Supporting regenerative agricultural practices that heal the land",
        },
    ]
    
    tasting_benefits = [
        "Try before you buy - no obligation",
        "Expert-guided tasting experience",
        "Learn about our coffee origins",
        "Tailored recommendations for your business",
        "Meet our coffee specialists",
    ]
    
    return render_template('coffee.html',  # Changed from 'pages/coffee.html'
                         coffee_ranges=coffee_ranges,
                         sustainability=sustainability,
                         tasting_benefits=tasting_benefits)

@app.route('/contact')
def contact():
    offices = [
        {
            "name": "Head Office",
            "location": "Cheltenham",
            "address": "Office Coffee Company, Cheltenham, Gloucestershire",
            "phone": "0203 763 4035",
            "email": "hello@office-coffee.co.uk",
            "hours": "Monday - Friday: 8:00 AM - 6:00 PM",
            "link": "/contact/cheltenham",
        },
        {
            "name": "Scotland",
            "location": "Glasgow",
            "address": "Office Coffee Company, Glasgow, Scotland",
            "phone": "0203 763 4035",
            "email": "scotland@office-coffee.co.uk",
            "hours": "Monday - Friday: 8:00 AM - 6:00 PM",
            "link": "/contact/scotland",
        },
        {
            "name": "North",
            "location": "Sheffield",
            "address": "Office Coffee Company, Sheffield, Yorkshire",
            "phone": "0203 763 4035",
            "email": "north@office-coffee.co.uk",
            "hours": "Monday - Friday: 8:00 AM - 6:00 PM",
            "link": "/contact/north",
        },
        {
            "name": "South West & Wales",
            "location": "Exeter",
            "address": "Office Coffee Company, Exeter, Devon",
            "phone": "0203 763 4035",
            "email": "southwest@office-coffee.co.uk",
            "hours": "Monday - Friday: 8:00 AM - 6:00 PM",
            "link": "/contact/south-west-wales",
        },
        {
            "name": "Cornwall",
            "location": "Redruth",
            "address": "Office Coffee Company, Redruth, Cornwall",
            "phone": "0203 763 4035",
            "email": "cornwall@office-coffee.co.uk",
            "hours": "Monday - Friday: 8:00 AM - 6:00 PM",
            "link": "/contact/cornwall",
        },
    ]
    
    contact_methods = [
        {
            "icon": "📞",
            "title": "Call Us",
            "description": "Speak to our coffee experts",
            "detail": "0203 763 4035",
            "action": "Call Now",
        },
        {
            "icon": "✉️",
            "title": "Email Us",
            "description": "Get in touch via email",
            "detail": "hello@office-coffee.co.uk",
            "action": "Send Email",
        },
        {
            "icon": "📍",
            "title": "Visit Us",
            "description": "Find your nearest office",
            "detail": "5 locations across the UK",
            "action": "Find Location",
        },
    ]
    
    return render_template('contact.html',  # Changed from 'pages/contact.html'
                         offices=offices,
                         contact_methods=contact_methods)

@app.route('/machines')
def machines():
    machine_types = [
        {
            "title": "Office Coffee",
            "description": "Provide your employees with convenient and delicious bean-to-cup coffee.",
            "link": "/machines/office",
            "image": "https://ext.same-assets.com/176798368/894159796.webp",
        },
        {
            "title": "Professional",
            "description": "Commercial coffee machines that can handle the rush.",
            "link": "/machines/commercial",
            "image": "https://ext.same-assets.com/176798368/1638910467.webp",
        },
        {
            "title": "Water",
            "description": "Hot and cold filtered water on demand, perfect for hot tea and cold drinks.",
            "link": "/machines/water",
            "image": "https://ext.same-assets.com/176798368/2351809614.webp",
        },
    ]
    
    quick_links = [
        {
            "title": "Office Machines",
            "subtitle": "View our range",
            "link": "/machines/office",
            "image": "https://ext.same-assets.com/176798368/2446004184.webp",
        },
        {
            "title": "Professional Machines",
            "subtitle": "View our range",
            "link": "/machines/commercial",
            "image": "https://ext.same-assets.com/176798368/4007591754.webp",
        },
        {
            "title": "Coffee Tasting",
            "subtitle": "Start now",
            "link": "/coffee/tasting",
            "image": "https://ext.same-assets.com/176798368/1092627970.webp",
        },
        {
            "title": "Coffee Shop",
            "subtitle": "Shop now",
            "link": "/shop",
            "image": "https://ext.same-assets.com/176798368/1752043403.webp",
        },
        {
            "title": "Brita Water",
            "subtitle": "Stay hydrated",
            "link": "/machines/water",
            "image": "https://ext.same-assets.com/176798368/2990761560.webp",
        },
        {
            "title": "Our Brochure",
            "subtitle": "Download",
            "link": "#",
            "image": "https://ext.same-assets.com/176798368/3130119963.webp",
        },
    ]
    
    return render_template('machines.html',  # Changed from 'pages/machines.html'
                         machine_types=machine_types,
                         quick_links=quick_links)

@app.route('/shop')
def shop():
    top_benefits = [
        "Next Day Delivery on orders placed by 12pm",
        "Free Delivery on all orders over £75",
        "Collect Reward Points when you purchase",
    ]
    
    shop_categories = [
        {
            "title": "Coffee",
            "subcategories": [
                {"name": "Fresh Beans", "link": "/shop/coffee/beans"},
                {"name": "Fresh Ground", "link": "/shop/coffee/ground"},
                {"name": "Instant", "link": "/shop/coffee/instant"},
            ],
        },
        {
            "title": "Tea",
            "subcategories": [
                {"name": "Everyday", "link": "/shop/tea/everyday"},
                {"name": "Envelopes", "link": "/shop/tea/envelopes"},
                {"name": "Green Tea", "link": "/shop/tea/green"},
            ],
        },
        {
            "title": "Sundries",
            "subcategories": [
                {"name": "Milk", "link": "/shop/sundries/milk"},
                {"name": "Hot Chocolate", "link": "/shop/sundries/hot-chocolate"},
                {"name": "Sugar", "link": "/shop/sundries/sugar"},
                {"name": "Syrups", "link": "/shop/sundries/syrups"},
                {"name": "Biscuits", "link": "/shop/sundries/biscuits"},
                {"name": "Cleaning", "link": "/shop/sundries/cleaning"},
            ],
        },
        {
            "title": "Disposables",
            "subcategories": [
                {"name": "Cups", "link": "/shop/disposables/cups"},
                {"name": "Stirrers", "link": "/shop/disposables/stirrers"},
                {"name": "Filter Papers", "link": "/shop/disposables/filter-papers"},
            ],
        },
    ]
    
    featured_products = [
        {
            "name": "Puro Fuerte Espresso Coffee Beans",
            "price": "£92.59",
            "image": "https://ext.same-assets.com/176798368/862006938.webp",
            "link": "/shop/product/puro-fuerte-espresso",
        },
        {
            "name": "Puro Fino Espresso Coffee Beans",
            "price": "£83.88",
            "image": "https://ext.same-assets.com/176798368/1554632211.webp",
            "link": "/shop/product/puro-fino-espresso",
        },
        {
            "name": "White (Fairtrade) Sugar Sticks x 1000",
            "price": "£14.28",
            "image": "https://ext.same-assets.com/176798368/1158155308.webp",
            "link": "/shop/product/fairtrade-sugar",
        },
        {
            "name": "Border Biscuits Multi Pack Box",
            "price": "£31.12",
            "image": "https://ext.same-assets.com/176798368/483893217.webp",
            "link": "/shop/product/border-biscuits",
        },
        {
            "name": "SHOTT Hazelnut Syrup 1 litre",
            "price": "£12.35",
            "image": "https://ext.same-assets.com/176798368/1461230917.webp",
            "link": "/shop/product/shott-hazelnut-syrup",
        },
    ]
    
    hero_slides = [
        {
            "title": "Great tasting coffee that protects the rainforests",
            "image": "https://ext.same-assets.com/176798368/4062412544.webp",
            "link": "/shop/coffee/beans",
        },
        {
            "title": "Introducing SHOTT real fruit syrups for coffee",
            "image": "https://ext.same-assets.com/176798368/172753487.webp",
            "link": "/shop/sundries/syrups",
        },
        {
            "title": "Great tasting ethical tea",
            "image": "https://ext.same-assets.com/176798368/2665720121.webp",
            "link": "/shop/tea/envelopes",
        },
    ]
    
    quick_links = [
        {
            "title": "Coffee",
            "subtitle": "Shop for coffee",
            "image": "https://ext.same-assets.com/176798368/3254887432.webp",
            "link": "/shop/coffee",
        },
        {
            "title": "Tea",
            "subtitle": "Shop for tea",
            "image": "https://ext.same-assets.com/176798368/2199519007.webp",
            "link": "/shop/tea",
        },
        {
            "title": "Coffee Machines",
            "subtitle": "Show now",
            "image": "https://ext.same-assets.com/176798368/1285433229.webp",
            "link": "/machines",
        },
        {
            "title": "Water Machines",
            "subtitle": "Show now",
            "image": "https://ext.same-assets.com/176798368/3179388369.webp",
            "link": "/machines/water",
        },
        {
            "title": "Sundries",
            "subtitle": "Shop now",
            "image": "https://ext.same-assets.com/176798368/679811487.webp",
            "link": "/shop/sundries",
        },
        {
            "title": "Disposables",
            "subtitle": "Shop now",
            "image": "https://ext.same-assets.com/176798368/3111505968.webp",
            "link": "/shop/disposables",
        },
    ]
    
    return render_template('shop.html',  # Changed from 'pages/shop.html'
                         top_benefits=top_benefits,
                         shop_categories=shop_categories,
                         featured_products=featured_products,
                         hero_slides=hero_slides,
                         quick_links=quick_links)

# API Routes
@app.route('/api/contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        data = request.get_json()
        # Here you would normally process the form data
        # For now, just return a success response
        return jsonify({"status": "success", "message": "Form submitted successfully!"})

# Error handlers - COMMENTED OUT since 404.html and 500.html don't exist
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
