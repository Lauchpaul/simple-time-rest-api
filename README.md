# Simple Time REST API

This is a simple REST API that returns the current server time. That's it. Nothing crazy.

I built this to learn Python, Flask and some Docker. I commented most of the code in `app.py` so if you're also learning, go read that file, I explained everything in there. I know it's a lot of comments, but I wanted to make sure I understood everything before moving on.

If you just want the clean version without my rambling, check out `app_uncommented.py`



## What I Learned

- OOP (Object-Oriented Programming) - Classes, Objects, Instances and Methods
- Modules & Imports in Python
- Decorators and how Flask uses them for routing
- `__name__` and `__main__` - when and why to use that weird thingy
- Why `host='0.0.0.0'` matters when running inside a container
- Version control with Git and GitHub
- Docker basics
- Flask basics
- REST API basics


Here is a video that helped me understand OOP: https://www.youtube.com/watch?v=08CWw_VD45w

All of this is explained in detail inside `app.py` - go check the comments there.



## Docker Guide

Here's the whole lifecycle. Build the thing, run it, use it, then clean up after yourself.

### Build the Image

```bash
sudo docker build -t simple-time-rest-api .
```
This reads the `Dockerfile`, installs everything, and creates an image called `simple-time-rest-api`.

### Run the Container

**If you wanna see the logs in your terminal:**
```bash
docker run -p 5000:5000 simple-time-rest-api
```

**If you want it running in the background:**
```bash
docker run -d -p 5000:5000 simple-time-rest-api
```
The `-d` flag = detached mode. It'll give you back the container ID and free up your terminal. Doesn't bind the stdout of the container to the terminal you're using.

The `-p 5000:5000` maps port 5000 on your machine to port 5000 inside the container.

### Hit the API

Open your browser and go to: **http://localhost:5000/time**

Or if you're a terminal person:
```bash
curl http://localhost:5000/time
```

You'll get something like:
```json
{
  "status": "success",
  "server_time": "2026-05-25 01:52:02",
  "timezone": "UTC"
}
```

---

### Clean Up

Alright you're done playing around, time to clean up.

**1. Find your container:**
```bash
docker ps -a
```
This shows all containers, even stopped ones. Grab the Container ID.

**2. Stop it:**
```bash
docker stop <Container_ID>
```

**3. Remove the container:**
```bash
docker rm <Container_ID>
```

**4. Check what images you have:**
```bash
docker images
```

**5. Remove the image:**
```bash
docker rmi <Image_ID>
```

Pro tip: you don't need to type the whole ID, just the first few characters work. Docker's smart enough to figure it out.

---

That's it. Simple project, but I learned a ton from it. If you're reading this and also learning - keep going, it clicks eventually :)
