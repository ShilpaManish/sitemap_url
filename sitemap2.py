import requests

def download_sitemap(url):
    try:
        # Check if the URL contains a sitemap.xml or wp-sitemap.xml file
        sitemap_urls = [f"{url}/sitemap.xml", f"{url}/wp-sitemap.xml"]

        for sitemap_url in sitemap_urls:
            response = requests.get(sitemap_url)
            if response.status_code == 200:
                # Download the sitemap.xml file
                with open('sitemap.xml', 'wb') as f:
                    f.write(response.content)
                print(f"Sitemap.xml downloaded successfully from {sitemap_url}")
                return

        print("No sitemap.xml or wp-sitemap.xml found.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Example usage:
url = input("Enter the URL to check and download sitemap.xml: ")
download_sitemap(url)
