# Johans Kök

## Azure related

[Passing env vars to the app](https://learn.microsoft.com/en-us/azure/developer/python/walkthrough-tutorial-authentication-05#environment-variables)

## Run the container

Assuming `STRIPE_KEY` stores the Stripe secret key.

```bash
podman secret create --env=true stripe-secret STRIPE_KEY
podman run  -p 5000:5000 -e HOST=127.0.0.1 --pull=always --rm --secret=stripe-secret,type=env,target=STRIPE_SECRET_KEY --name johan ghcr.io/jsliacan/johans-kok:0.1.0
```
Run `curl 127.0.0.1:5000` to get the index page. Or visit the address in the browser. 

## Options

Add `-d` option if you want to detach. Run `podman exec -it johan bash` to get into the running container. Default `HOST` is `0.0.0.0`.

## Work on the project

1. Start virtual environment in the project folder: `python3 -m venv .venv` (create virt env with `.venv` being the config folder, placed in the current location)
2. Activate virt env: `source .venv/bin/activate`
3. Make sure you have up-to-date pip: `python3 -m pip install --upgrade pip`
4. Resume where you left off: `python3 -m pip install -r requirements.txt`
5. Do the coding.
6. Save the state: `python3 -m pip freeze > requirements.txt`
7. Leave: `deactivate`.
