# SIBI- Detection
`creator : Hamka Satria`
<br><br>

## Download models with command
```
wget https://dl.dropboxusercontent.com/s/dlww6malzd6pwtj/FRCNN-R18.pth

wget https://dl.dropboxusercontent.com/s/y3jmxt69p9uswnc/FRCNN-R50.pth
```

`Note`

change the models type with change the `selection` in app.py files


<br><br>

## A. Setup Local
<br>

### 1. Install IceVision

```
pip install icevision[all]
```

### 2. Install Gradio
```
pip install gradio
```
### 3. run app
```
python3 app.py
```

<br>


## B. Run With Docker
<br>

To build the icevision image, run the following command:
```
docker-compose build
```

Once the icevision image has been successfully built, run the icevision service:
```
 docker-compose run --rm -d icevision
```

**Note**
For more detailed instructions on how to use this icevision docker container as well how connect it to Visual Studio Code, check out this in-depth [blog post](https://francescopochetti.com/developing-inside-a-docker-container-in-visual-studio-code/).