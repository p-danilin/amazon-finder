# Amazon Product Finder ChatGPT Plugin

This project is a ChatGPT plugin that allows users to search for Amazon products. It uses the Amazon Product Advertising API to search for products based on keywords, retrieve product details, and generate links.

## Setup Locally

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com.
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in localhost:5003 since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "Find me a book about machine learning on Amazon" and the plugin will return a list of products related to your query.

## Note

This plugin is designed to work in conjunction with the ChatGPT plugins documentation. If you do not already have plugin developer access, please join the waitlist.

## Disclaimer

This project is not affiliated with, endorsed by, or in any way associated with OpenAI or Amazon. Use at your own risk.
