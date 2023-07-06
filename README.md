
# Proxy Service

An Http Proxy Service written using Flask,Python. The Service sends the post request taken from the client to upstream api and returns the response.











## Run locally

Once cloned, Go to the project directory

```bash
  cd proxy-service
```

Build

```bash
  make build
```

Start the container

```bash
  make up
```

Run the application

```bash
  make run
```

## API Reference

#### Post request

```http
  POST /proxy
```
Post the data coming from the client.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username` | `str` | **Required**. Name of the User. |

#### Get status

```http
  GET /status
```
Returns time from start and total number of requests processed.






