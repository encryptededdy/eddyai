# eddyaibot

This is a fun Telegram bot, that completes sentences.

## Adding a model

### Training a model

Not sure how this works, tbh

### Converting your model to right format

Extract your .tar, and then run the following command:

```
python3 gpt2convert.py path/to/your/model gpt2_yourmodel.bin
```

### Test it out

Run the following command to validate that the model is working

```
./gpt2tc -m 345M -f gpt2_yourmodel.bin -T 1 g "Hello, my name is"
```

### Add it to the bot

You want to modify gpt2bot.py.

## Build & Deployment

We use Docker to package, and Kubernetes to deploy. Make sure you mount in `telegramkey.txt` with your Telegram API key.

- `docker build . -t eddyaibot:latest`
- `kubectl apply -f deployment.yaml`
