# installation

## prereqs

setup a free (or you can pick a paid option, but there's no need for our purposes) account with [IBM's quantum platform](https://quantum.ibm.com)
>NOTE that IBM also offers a "cloud" channel, which has no free option and looks like it may well be for chumps.  just use the url given here and you'll be fine.

once you have an account (easily setup btw), go to the dashboard (should take you there automatically) and note the api key, which will be easily found in the upper right of the screen.  to use the scripts in this repo without modification, save your api key to the env variable `IBM_Q_API_KEY`.

## setup python venv

from the root directory of this repo, execute the following (assumes python 3 is installed as `python`.  adjust if needed):

```sh
$ python -m venv .venv
$ . .venv/bin/activate

(.venv) $ pip install --upgrade pip
(.venv) $ pip install -r requirements.txt

```

## save your ibm creds locally and verify

```sh
$ python ./setup_local_creds.py  # note the output indicates where your api key is stored locally (in plaintext)
$ python ./check_runtime.py

```
if you see "huzzah!  you have just run an actual quantum program!" then you are good to go.  you did it, great job.  if you don't see this line, then you fucked up somewhere, so probably wanna try to fix that.

## jupyter

jupyter will be installed from the `requirements.txt`.  if you followed the above instructions, then it's already installed.  to run it (assuming your python virtual env is activated already):

```sh
(.venv) $ jupyter notebook
```




