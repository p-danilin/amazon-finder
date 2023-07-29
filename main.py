import json
import quart
import quart_cors
from quart import request
from amazon_paapi import Paapi5PythonSdk

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Initialize the Amazon Product Advertising API client
amazon = Paapi5PythonSdk.ProductsApi(
    access_key=YOUR_AMAZON_ACCESS_KEY,
    secret_key=YOUR_AMAZON_SECRET_KEY,
    host="webservices.amazon.com",
    region="us-west-2",
    partner_tag=YOUR_AMAZON_ASSOC_TAG,
)

@app.get("/products/<string:query>")
async def get_products(query):
    # Search for products using the Amazon Product Advertising API
    search_request = Paapi5PythonSdk.SearchItemsRequest(
        keywords=query,
        resources=["Images.Primary.Small", "ItemInfo.Title", "Offers.Listings.Price"],
        partner_tag=YOUR_AMAZON_ASSOC_TAG,
        partner_type="Associates",
        marketplace="www.amazon.com",
    )
    response = amazon.search_items(search_request)

    # Extract the product details and generate the affiliate links
    products = []
    for item in response.search_result.items:
        product = {
            "name": item.item_info.title.display_value,
            "description": "Product from Amazon",
            "affiliate_link": item.detail_page_url,
        }
        products.append(product)

    # Return the product recommendations
    return quart.Response(response=json.dumps(products), status=200)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
