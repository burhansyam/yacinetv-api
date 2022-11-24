# Yacine Live TV API

This is an unofficial api wrapper for yacineapp.tv in python. With this api you are able to browse tv categories and get stream links.

## API Reference

#### Get all categories

```bash
  GET /categories
```

#### Get category channels

```bash
  GET /categories/${id}/channels
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of category  |

#### Get channel

```bash
  GET /channel/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of channel  |

## Run Locally

Clone the project

```bash
  git clone https://github.com/burhansyam/yacinetv-api
```

Go to the project directory

```bash
  cd yacinetv-api
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the FastAPI Application Server using:

```bash
  bash run.sh
```

## Feedback

If you have any feedback, contact me on telegram https://t.me/aimadnet

## Support Us

ETH: 0x7c0564bfCFe48ffCdee95ee137e33367C0077429
