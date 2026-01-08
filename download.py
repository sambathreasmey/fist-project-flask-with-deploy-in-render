import requests

def start():
  # The URL of the image
  url = "https://p16-common-sign.tiktokcdn-us.com/tos-alisg-p-0037/oYE3PQEBwBmQxBxYsaMIHzAg5vLVBiUiAj4iV~tplv-tiktokx-origin.image?dr=9636&x-expires=1767945600&x-signature=93GWIJ22K0E61vqwjjiGfr3V%2BlU%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=useast5"
  
  # Setting a User-Agent is often required to avoid a 403 Forbidden error
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
  }
  
  try:
      response = requests.get(url, headers=headers, stream=True)
      
      # Check if the request was successful
      if response.status_code == 200:
          # Open a local file in binary write mode
          with open("tiktok_image.jpg", "wb") as file:
              for chunk in response.iter_content(1024):
                  file.write(chunk)
          print("Download successful! Image saved as 'tiktok_image.jpg'")
      else:
          print(f"Failed to download. Status code: {response.status_code}")
  
  except Exception as e:
      print(f"An error occurred: {e}")
