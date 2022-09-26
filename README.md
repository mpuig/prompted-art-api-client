# An API REST client for Prompted.art

This is a simple API client to send your generated art to prompted.art.

## Get a token

Go to https://prompted.art, sign up and you'll have a private token to use the API.

## Install client

To send images to prompted.art from your code, you first need to install the package:

```bash
pip install prompted-art-api
```

## Generate Art

From your python code (locally, google colab,...), you only need to setup the client using a valid token:

```python
from prompted_art_api.client import PromptedArtAPI

client = PromptedArtAPI(
    api_key="334d39db1f0d43859419bf5039a49a1b206062e5"
)
```

And you can start sending your generated images to prompted.art.

First thing is to encode the image to base64:

```python
import base64
encoded_string = base64.b64encode(image_file.read())
```

If you print the `encoded_string` should contain a string similar to this:

```terminal
"image/png;base64,iVBORw0KGgoAAA..."
```

This string can be used to send the miage to the prompted.art API using this payload:

```python
data = {
    "prompt": "test from colab",
    "source": "stable diffusion",
    "image": encoded_string
}
client.create_prompt(data=data)
```

If you have images generated somewhere else (e.g. dall-e, midjourney, etc) you can salso send them using this payload:

```python
data = {
    "prompt": "test from colab",
    "source": "midjourney",
    "url": "https://cdn.discordapp.com/attachments/1005626976016531567/1005858741767372873/-n_9_-i_-S_3792373097_ts-1659885810_idx-4.png",
}
client.create_prompt(data=data)
```
