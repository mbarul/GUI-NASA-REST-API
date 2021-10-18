<div align="center">
  <a href="https://www.python.org/">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg"
      alt="API stability" />
  </a>
</div>

<div align="center">
  <!-- Contributors -->
  <a href="https://github.com/somrajchowdhury/Python_GUI_tkinter/graphs/contributors">
    <img src="https://img.shields.io/badge/contributor(s)-1-red.svg"
      alt="API stability" />
  </a>

  <!-- Python Version -->
  <a href="https://github.com/somrajchowdhury/PythonCodes/">
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg"
      alt="API stability" />
  </a>
  
  <!-- Number of Codes -->
  <a href="https://github.com/somrajchowdhury/PythonCodes/">
    <img src="https://img.shields.io/badge/1-codes-brightgreen.svg"
      alt="API stability" />
  </a>
</div>

<h1 align="center">tkinter GUI</h1>

# Python GUI programming using tkinter

> tkinter is a standard Python GUI package.

## Program List

- NASA 

## NASA - Picture of day

*NASA - Picture of day* application uses an API to extract Astronomy Picture of the Day data using URL requests and displays the relevant retrieved data from the API on to the GUI.

### API used:

![NASA API](https://miro.medium.com/max/452/1*0tPTi7jNKZbV05A2m0i3Bg.png)

The **NASA** API is a RESTful web service to obtain movie information. By default all NASA API responses are formatted as JSON.

### Libraries used:

- **tkinter** - *to design the GUI*
- **pillow (PIL)** - *to make images compatible with tk GUI*
- **io** - *to encode and use images from URL*
- **requests** - *to request and read data from the API response*
- **urllib** - *to request and read data from the API response*
- **json** - *to load and retrieve required fields from the API response*

### Screenshots :camera: :

The first window that shows up is where you enter the name of the movie whose info you want to display on the GUI.

![enter movie name.png](https://i.imgur.com/VV3UFUL.png)

Suppose I enter **avatar** in the entry field,

![enter avatar](https://i.imgur.com/X9tKG55.png)

If the movie is found, the response is sent and the GUI looks like this,

![avatar](https://i.imgur.com/xoRt4u4.png)

If the entered movie is not found, it is notified in the GUI using a *validation message*,

![not found](https://i.imgur.com/ZzvzpUW.png)

Also, at times there might be some issues connecting to the API service, in that case you get a *message* to resumbit, where you just need to click the `SUBMIT` button again

![resubmit](https://i.imgur.com/8feFmAK.png)

*Some more screenshots*

| ![harry potter](https://i.imgur.com/5gggJ2Y.png) | ![stranger things](https://i.imgur.com/OLSyySN.png) |
|:--:|:--:|
| ![uri](https://i.imgur.com/AUSQp2X.png) | ![3 idiots](https://i.imgur.com/L2n0ZbD.png) |


---


