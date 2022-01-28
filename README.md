# KTaboo

## Build the app with Docker
Use the docker container as specified in the guide.
Clone the repository (in other directory) from the official repo and run the build command.

```bash
git clone https://github.com/kivy/buildozer
docker build --tag=buildozer .
```

When you change the `buildozer.spec` you always need to run a `buildozer appclean`.
Then you can 
```bash
docker run --volume "<absolute_path>":/home/user/hostcwd buildozer appclean
docker run --volume "<absolute_path>":/home/user/hostcwd buildozer android debug # choose (debug|release) 
```


# Debug with android
```bash
adb devices  # ensures the device is connected and appears in the list
adb logcat | findstr com.kames.kaboo  # or python
```