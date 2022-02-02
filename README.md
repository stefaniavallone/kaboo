# KTaboo

## Build the app with Docker
Use the docker container as specified in the guide.
Clone the repository (in other directory) from the official repo and run the build command.

```bash
git clone https://github.com/kivy/buildozer
cd buildozer
docker build --tag=buildozer .
```

When you change the `buildozer.spec` you always need to run a `buildozer appclean`.
Then you can 
```bash
docker run --volume "<absolute_path>":/home/user/hostcwd buildozer appclean
docker run --volume "<absolute_path>":/home/user/hostcwd buildozer android debug # choose (debug|release) 
```

### Build the app with aab support
```bash
git clone --single-branch --branch feat/aab-support https://github.com/misl6/buildozer.git
cd buildozer
docker build --tag=buildozer-aab .
```
Make sure you have in your `buildozer.spec`, the following lines:  
```
android.archs = arm64-v8a, armeabi-v7a
android.release_artifact = aab
p4a.branch = develop
```

Create a keystore
```bash
mkdir -p /path/to/keystores/
keytool -genkey -v -keystore /path/to/keystores/<keystore>.keystore -alias <keystore-alias> -keyalg RSA -keysize 2048 -validity 10000
keytool -importkeystore -srckeystore /path/to/keystores/<your-new-key>.keystore -destkeystore /path/to/keystores/<keystore>.keystore -deststoretype pkcs12
```

```bash
docker run --volume "<absolute_path>":/home/user/hostcwd buildozer-aab -v init
docker run --volume "<absolute_path>":/home/user/hostcwd buildozer-aab appclean
docker run \
     --volume "<app-project-folder>":/home/user/hostcwd \
     --volume "<absolute_path>\keystores":/home/user/keystores \
     -e P4A_RELEASE_KEYSTORE=/home/user/keystores/<keystore>.keystore \
     -e P4A_RELEASE_KEYSTORE_PASSWD="<your-password>" \
     -e P4A_RELEASE_KEYALIAS_PASSWD="<your-password>" \
     -e P4A_RELEASE_KEYALIAS="<keystore-alias>" \
     buildozer-aab -v android release
```
### Bundletools + ADB
Put your generated .aab file into the bin folder. 
Verify
```bash
bundletool validate --bundle bin/kaboo-release.aab
```
Create APK 
To have it signed you have to pass also keystore
```bash
bundletool build-apks --mode universal --bundle bin/kaboo-release.aab --output bin/kaboo-release.apks --ks keystores/ktaboo.keystore --ks-key-alias ktaboo --ks-pass pass:ktaboo.11
```
Install
```bash
bundletool install-multi-apks --apks bin/kaboo-release.apks
```


# Debug with android
```bash
adb devices  # ensures the device is connected and appears in the list
adb logcat | findstr com.kames.kaboo  # or python
```