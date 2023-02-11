# **SIBI- Detection**
>Object Detection Abjad SIBI (Sistem Isyarat Bahasa Indonesia)
>- Creator : `Hamka Satria`
>- Github : `https://github.com/hamkasatria`


### *Fast Run*
- Local : `make sibi.all`

- Docker : `make docker.all`


### **Download models with command**
```
make download.model.all
```

## *A. **Manual** Run in Local*

1. Install IceVision and Gradio with `make setup.all`
2. run app with `make sibi.run`
3. hit open port and enjoy it


## B. ***Manual** Run With Docker*

1. To build the icevision image, run the following command:`docker-compose build`

2. Once the icevision image has been successfully built, run the icevision service:`docker-compose run --rm -d icevision`


>**Note**
> - For more detailed instructions on how to use this icevision docker container as well how connect it to Visual Studio Code, check out this in-depth [blog post](https://francescopochetti.com/developing-inside-a-docker-container-in-visual-studio-code/).
>-  change the models type to run with change the `selection` in app.py files