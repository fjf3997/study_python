import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img = req.read()
    with open("images/"+img_name+".jpg", "wb") as f:
        f.write(img)


def main():
    gevent.joinall([
        gevent.spawn(download, "1.jpg", "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2156421975,3337537785&fm=26&gp=0.jpg"),
        gevent.spawn(download, "2.jpg", "https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3925233323,1705701801&fm=26&gp=0.jpg")
    ])


if __name__ == "__main__":
    main()
